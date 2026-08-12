# Daytona Words 1–50

A timed sight-word reading race for a second grader.

Press **GO**, read all 50 words out loud, then hit the checkered flag to stop
the clock. It keeps a track record and recent laps so she can watch herself get
faster week to week.

**Play it:** https://jasonh80.github.io/daytona-words/

## Two modes

- **I'll tap the flag** — a grown-up presses FINISH when she reads the last word.
  Works on every device.
- **Listen to me read** — the microphone checks words off as she says them and the
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
| `manifest.webmanifest` | Home-screen install metadata |
| `sw.js` | Offline caching. Page is network-first, assets cache-first |
| `make-icon.py` | Regenerates `icon-512.png` (no image library needed) |

Best times and settings live in each browser's local storage, so every device
keeps its own record.
