SuperSelect
==================

Extended selection functionality such as select previous match, skip to next(or prev) match, and invert selection.

See this [30 second vid](http://youtu.be/8SQi-Fvhp-Q) for a brief demo.

Installation
------------

With [Package Control](http://wbond.net/sublime_packages/package_control):

1. Run the "Package Control: Install Package" command, find and install SuperSelect plugin.
2. Restart ST2 editor (if required)

OR:

1. Open the Sublime Text 2 Packages folder
    - OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
    - Windows: `%APPDATA%/Sublime Text 2/Packages/`
    - Linux: `~/.Sublime Text 2/Packages/`
2. Clone this repo
3. Configure your keybindings, if required

Commands
--------

+ `expand_prev` <kbd>&#8984;+shift+,</kbd>: Looks backwards and selects the next match of current selection or selects current word if nothing selected.
+ `expand_next` <kbd>&#8984;+shift+.</kbd>: Looks forwards and selects the next match of current selection or selects current word if nothing selected.
+ `skip_and_select_prev` <kbd>&#8984;+shift+alt+,</kbd>: Skips over current selection (de-selects) and moves backwards to select next match.
+ `skip_and_select_next` <kbd>&#8984;+shift+alt+.</kbd>: Skips over current selection (de-selects) and moves forwards to select next match.
+ `invert_selections` <kbd>&#8984;+shift+i</kbd>: Inverts current selections, restricted to matching regions.
+ `select_sequential_string` <kbd>&#8984;+shift+0</kbd>: Selects other strings resembling the current selection that have trailing digit(s).  "Sequential" might be misleading as there is no actual checking for this - I just look for digit(s).

TODO
--------
- Different colour indicators to show selection end-points.  It's easy to get lost once we start skipping.
- Update video to show 'sequential' selection
- ~~select sequential string~~