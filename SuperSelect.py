import sublime, sublime_plugin


class SelectPreviousCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # self.doSearch(self.view, False)
    # (sublimer).sublimer.
    # TODO: we are selecting more here than sublime does naturally.. fix this
    self.view.erase_regions("test")
    # separatorString = self.view.settings().get('word_separators') + u" \n\r"

    first_sel_region = self.view.sel()[0]
    pattern = "(?<!\w)" + self.view.substr(first_sel_region) + "(?![\w])"
    print pattern
    matching_regions = self.view.find_all(pattern)

    print "Matching Regions: ", matching_regions

    # highlight all matching regions # sublime does this by default - (for debugging)
    self.view.add_regions("test", matching_regions, 'comment', sublime.DRAW_OUTLINED)

    # back up one to previous match
    prev_region_index = matching_regions.index(first_sel_region) - 1
    print prev_region_index
    print matching_regions[prev_region_index]
    # print [y[0] for y in matching_regions].index(first_sel_region)

    # add previous region to selection
    self.view.sel().add(matching_regions[prev_region_index])

    #TODO: fix loop around