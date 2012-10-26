SuperSelect
==================

Extended selection functionality such as select previous match, skip to next(or prev) match, and invert selection.

See this [30 second vid](http://youtu.be/8SQi-Fvhp-Q) for a brief demo.

Installation
------------

1. Open the Sublime Text 2 Packages folder
    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/
2. Clone this repo
3. Configure your keybindings, if required

Commands
--------

* `expand_prev` (*&#8984;+shift+,*): Looks backwards and selects the next match of current selection or selects current word if nothing selected.
* `expand_next` (*&#8984;+shift+.*): Looks forwards and selects the next match of current selection or selects current word if nothing selected.
* `skip_and_select_prev` (*&#8984;+shift+alt+,*): Skips over current selection (de-selects) and moves backwards to select next match.
* `skip_and_select_next` (*&#8984;+shift+alt+.*): Skips over current selection (de-selects) and moves forwards to select next match.
* `invert_selections` (*&#8984;+shift+i*): Inverts current selections, restricted to matching regions.

TODO
--------