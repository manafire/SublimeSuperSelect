import sublime, sublime_plugin

key = "super_select"
first_selected_region = None
last_selected_region = None

class SuperSelect(sublime_plugin.TextCommand):

  def run(self, edit):
    global first_selected_region, last_selected_region
    # do things like grab selected words, figure start and end, bounds, skipped, wrap, etc.

    if self.view.sel()[0].size() > 0: # don't run if there's no selection

      # set up defaults
      if first_selected_region == None:
        first_selected_region = self.view.sel()[0]
        last_selected_region = self.view.sel()[-1]

      self.go(edit)
    else:
      first_selected_region = None
      last_selected_region = None


class ExpandPrevCommand(SuperSelect):
  def go(self, edit):
    global first_selected_region

    # TODO: we are emulating the way Sublime selects words, wish there was a way to grab Sublime's regions.
    self.view.erase_regions(key)
    # separatorString = self.view.settings().get('word_separators') + u" \n\r"

    pattern = "(?<!\w)" + self.view.substr(first_selected_region) + "(?![\w])"
    matching_regions = self.view.find_all(pattern)

    print "Matching Regions: ", matching_regions

    # highlight all matching regions # sublime does this by default - (for debugging)
    self.view.add_regions(key, matching_regions, 'comment', sublime.DRAW_OUTLINED)

    # back up one to previous match
    prev_region_index = matching_regions.index(first_selected_region) - 1
    first_selected_region = matching_regions[prev_region_index]
    print prev_region_index
    print matching_regions[prev_region_index]

    # add previous region to selection
    self.view.sel().add(matching_regions[prev_region_index])


# Selects next word relative to last selection
class ExpandNextCommand(SuperSelect):
  def go(self, edit):
    global first_selected_region, last_selected_region

    # find all regions matching currently selected text
    selected_text = self.view.substr(self.view.sel()[0])
    pattern = "(?<!\w)" + selected_text + "(?![\w])"
    matching_regions = self.view.find_all(pattern)

    # find next occurence AFTER last_selected_region in matching_regions
    region_count = len(matching_regions)
    index = (matching_regions.index(last_selected_region) + 1) % region_count
    self.view.sel().add(matching_regions[index])

    last_selected_region = matching_regions[index]

