import sublime, sublime_plugin

key = "super_select"
first_selected_region = None
last_selected_region = None

# TODO: we are emulating the way Sublime selects words, wish there was a way to grab Sublime's regions.
class SuperSelect(sublime_plugin.TextCommand):

  def run(self, edit):
    global first_selected_region, last_selected_region
    # do things like grab selected words, figure start and end, bounds, skipped, wrap, etc.

    # don't run if there's no selection
    # TODO: OR don't run if everything that has been selected already has
    if (self.view.sel()[0].size() > 0):

      # set up defaults
      if first_selected_region == None:
        first_selected_region = self.view.sel()[0]
        last_selected_region = self.view.sel()[-1]

      self.go(edit)
    else:
      first_selected_region = None
      last_selected_region = None


  def get_matching_regions(self, pattern = None):
    # find all regions matching currently selected text
    # separatorString = self.view.settings().get('word_separators') + u" \n\r"
    selected_text = pattern or self.view.substr(self.view.sel()[0])
    matcher = "(?<!\w)" + selected_text + "(?![\w])"
    return self.view.find_all(matcher)



class ExpandPrevCommand(SuperSelect):
  def go(self, edit):
    global first_selected_region

    # grab regions matching selected text
    matching_regions = self.get_matching_regions()

    # highlight all matching regions # sublime does this by default - (for debugging)
    # self.view.add_regions(key, matching_regions, 'comment', sublime.DRAW_OUTLINED)

    # back up one to previous match
    prev_region_index = matching_regions.index(first_selected_region) - 1
    first_selected_region = matching_regions[prev_region_index]

    # add previous region to selection
    self.view.sel().add(matching_regions[prev_region_index])


# Selects next word relative to last selection
class ExpandNextCommand(SuperSelect):
  def go(self, edit):
    global first_selected_region, last_selected_region

    # find all regions matching currently selected text
    matching_regions = self.get_matching_regions()

    # find next occurence AFTER last_selected_region in matching_regions
    region_count = len(matching_regions)
    index = (matching_regions.index(last_selected_region) + 1) % region_count
    self.view.sel().add(matching_regions[index])

    last_selected_region = matching_regions[index]

