import sublime, sublime_plugin

key = "super_select"
last_selected_region = None

class SuperSelect(sublime_plugin.TextCommand):

  def run(self, edit):
    global last_selected_region
    # do things like grab selected words, figure start and end, bounds, skipped, wrap, etc.

    print last_selected_region
    if self.view.sel()[0].size() > 0: # don't run if there's no selection
      self.go(edit)
    else:
      last_selected_region = None


class SelectPreviousCommand(SuperSelect):
  def go(self, edit):
    global last_selected_region
    # TODO: we are emulating the way Sublime selects words, wish there was a way to grab Sublime's regions.
    self.view.erase_regions(key)
    # separatorString = self.view.settings().get('word_separators') + u" \n\r"

    first_sel_region = self.view.sel()[0]

    pattern = "(?<!\w)" + self.view.substr(first_sel_region) + "(?![\w])"
    matching_regions = self.view.find_all(pattern)

    print "Matching Regions: ", matching_regions

    # highlight all matching regions # sublime does this by default - (for debugging)
    self.view.add_regions(key, matching_regions, 'comment', sublime.DRAW_OUTLINED)

    # back up one to previous match
    prev_region_index = matching_regions.index(last_selected_region or first_sel_region) - 1
    last_selected_region = matching_regions[prev_region_index]
    print prev_region_index
    print matching_regions[prev_region_index]

    # add previous region to selection
    self.view.sel().add(matching_regions[prev_region_index])
