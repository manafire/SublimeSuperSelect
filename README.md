SuperSelect
==================

Extended selection functionality such as select previous match, skip to next(or prev) match, and invert selection.

See this [30 second vid](http://youtu.be/8SQi-Fvhp-Q) for a brief demo. *outdated - missing sequential select demos*

Installation
------------

With [Package Control](https://sublime.wbond.net/):

1. Run the "Package Control: Install Package" command, find and install SuperSelect plugin.
2. Restart Sublime (if required)

OR:

1. Open the Sublime Text 3 Packages folder (change path for ST2 if needed)
    - OS X: `~/Library/Application Support/Sublime Text 3/Packages/`
    - Windows: `%APPDATA%/Sublime Text 3/Packages/`
    - Linux: `~/.Sublime Text 3/Packages/`
2. Clone this repo
3. Configure your keybindings, if required

Commands
--------

+ `expand_prev` <kbd>&#8984;+shift+,</kbd>: Looks backwards and selects the next match of current selection or selects current word if nothing selected.
+ `expand_next` <kbd>&#8984;+shift+.</kbd>: Looks forwards and selects the next match of current selection or selects current word if nothing selected.
+ `skip_and_select_prev` <kbd>&#8984;+shift+alt+,</kbd>: Skips over current selection (de-selects) and moves backwards to select next match.
+ `skip_and_select_next` <kbd>&#8984;+shift+alt+.</kbd>: Skips over current selection (de-selects) and moves forwards to select next match.
+ `invert_selections` <kbd>&#8984;+shift+i</kbd>: Inverts current selections, restricted to matching regions.
+ `select_sequential_string` <kbd>&#8984;+shift+0</kbd>: Selects other strings resembling the current selection that have trailing digit(s).  "Sequential" might be misleading as there is no actual checking for this - I just look for digit(s).  *(If you have a better name for this, I'd love to hear it.)*
+ `select_strict_sequential_string` <kbd>&#8984;+shift+1</kbd>: Like select sequential string, but actually checks for proper sequence (I should probably rename that).  If you have "Item 5" selected, this will select "Item 6", "Item 7", ..., excluding regions that don't match the sequence (e.g. if "Item 99" appeared between 6 and 7.  **Note**: Invert selections will invert the selection to 99 currently).


TODO
--------
- Different colour indicators to show selection end-points.  It's easy to get lost once we start skipping.
- Update video to show 'sequential' selection and 'strict sequential' selection modes.
- ~~select sequential string~~