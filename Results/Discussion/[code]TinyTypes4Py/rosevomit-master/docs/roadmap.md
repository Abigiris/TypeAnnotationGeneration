# *Rosevomit* roadmap

The roadmap is probably better viewed through this project's "Glo" kanban board [here](https://app.gitkraken.com/glo/board/XW-3b9aSlAAPAWps), which is also linked to this project's issue boards. The Glo board is almost always more up to date than this document.

## Short-term features (probably in the next few minor updates)

Making Suncalc actually functional:

- **Sunlight calculator**. Enter some planetary variables and find the relevant info regarding sunrise and sunset on any particular day for any particular location, using the [sunrise equation](https://en.wikipedia.org/wiki/Sunrise_equation). AT THIS POINT, THE RESULTS SHOULD ACTUALLY BE ACCURATE ENOUGH FOR GAMEPLAY USE.

General features:

- **Improved CLI**. Switch from the current numbered menu to something involving argparse. Add a "help" functionality. Integrate with the error classes (let's do some ```try...except...``` statements?).
- **Name generation improvements**. Ability to view saved names. Ability to check for duplicate names.

Improvements under the hood:

- **Multiple processes**. Startup + CLI + LogicController (+ datacontroller?)? Could help speed up some list generation.
- **Expanded test suite.** At a minimum, something that will stop [Better Code Hub](https://bettercodehub.com/) from yelling at me.

## Medium-term features (introduce/polish before v0.20.0)

Improvements to name generation:

- Unisex names
- Ability to consider "weighted" name lists, like in the US census data.
- Ability to differentiate between multiple cultural name lists, added by users
- Ability to check for duplicate names

Improvements to Suncalc:

- Integrate Matplotlab (or some other plotting library?) into Suncalc so we can see results graphically. Additionally, I'd like to be able to see graphs of saved data.

## Long-term features (introduce/polish before v1.0.0)

- SQLite? MySQL? PostgreSQL?
- Ability to handle different cultural naming traditions
- Save NPC files, track NPC data
- Create installation files/binary files/exe files.
- A GUI using WPF? Maybe?

## v1.0.0

- Stable release
