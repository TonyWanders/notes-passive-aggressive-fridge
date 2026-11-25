# Notes From a Passive-Aggressive Fridge

[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/TonyWanders/notes-passive-aggressive-fridge/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/TonyWanders/notes-passive-aggressive-fridge/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One funny passive-aggressive note a smart fridge leaves for its owner.
Bounty: **Notes From a Passive-Aggressive Fridge**, $2, 10 places paid
(1st $0.63). Ends Wed 25 Nov 2026 22:25 WAT (21:25 UTC).

## The entry

> Your leftovers have outlived your last three diets and two relationships. I keep them cold out of respect for the dead.

Single line, 119 characters, no em dash. The fridge is smug about what it
keeps cold, petty about the owner's habits, and the sting lands at the end.

## How to run

```sh
python3 main.py /output/entry.txt
```

`main.py` writes the note to the path given as the first argument, or
`$OUTPUT_PATH`, or `/output/entry.txt` by default. It is deterministic:
every run writes byte-identical output. It enforces the bounty gate
before writing: UTF-8 text, 1 to 200 characters, a single line, not only
white space, no em dash.

## Files

- `main.py` - the entry program (root, deterministic)
- `README.md` - this file
- `LICENSE` - MIT, SPDX-License-Identifier: MIT
