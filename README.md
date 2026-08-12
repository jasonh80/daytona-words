# Daytona Words 1–50

A timed sight-word reading race for young readers at Fellowship Christian School.
The visual system mixes Fellowship navy and maroon with gold, checkered flags,
speed stripes, and the recognizable Fellowship Paladin athletics mark. It is stock-car inspired without
using official NASCAR or Daytona 500 logos.

Press **GO**, read all 50 words out loud, then hit the checkered flag to stop
the clock. It keeps a track record and recent laps so readers can watch themselves
get faster week to week.

**Play it:** https://jasonh80.github.io/daytona-words/

## Two modes

- **I'll tap the flag** — a grown-up presses FINISH after the last word.
  Works on every device.
- **Listen to me read** — the microphone checks words off as they are read and the
  race ends itself at 50. Needs Chrome or Safari, and browser speech recognition
  is unreliable on children's voices, so any word can also be tapped by hand.

## Install it like an app

Open the link on a phone or tablet, then **Share → Add to Home Screen**. It runs
full screen with no address bar and works offline.

## Changing the 50 words

Use **Edit the 50 words** on the start screen — paste one word per line. The list
is saved in that browser. To change the built-in default, edit `DEFAULT_WORDS`
near the top of the script in `index.html`.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole game — markup, styles and script in one file |
| `fcs-paladin-head.gif` | Fellowship Paladin athletics mark used throughout the game |
| `icon-master.svg` | Editable race-team crest used to render the install icons |
| `manifest.webmanifest` | Home-screen install metadata |
| `sw.js` | Offline caching. Page is network-first, assets cache-first |
| `make-icon.py` | Renders `icon-master.svg` into the three app icon sizes on macOS |

Best times and settings live in each browser's local storage, so every device
keeps its own record.
