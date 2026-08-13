# Daytona 50 of Words

A timed weekly spelling-word reading race for young readers at Fellowship Christian School.
The visual system uses the supplied Daytona 50 of Words artwork, Fellowship navy
and maroon, gold, checkered flags, racetrack curves, and the recognizable Paladin.

Press **GO**, read the current weekly words out loud, then hit the checkered flag to stop
the clock. It keeps a track record and recent laps so readers can watch themselves
get faster week to week.

**Play it:** https://jasonh80.github.io/daytona-words/

## Install it

Tap **Install App** on the start screen. On iPhone or iPad, open the link in
Safari, tap Share, choose **Add to Home Screen**, turn on **Open as Web App**,
and tap Add. On Android, the button opens the browser's native install prompt
when available. The installed app launches without normal browser chrome and
keeps the game shell available offline after the first visit.

## Two modes

- **I'll tap the flag** — a grown-up presses FINISH after the last word.
  Works on every device.
- **Listen to me read** — the microphone checks words off as they are read and the
  race ends after the complete weekly list. Needs Chrome or Safari, and browser speech recognition
  is unreliable on children's voices, so any word can also be tapped by hand.

## Changing the weekly words

Use **Edit weekly words** on the start screen — paste one word per line. The list
is saved in that browser. To change the built-in default, edit `DEFAULT_WORDS`
near the top of the script in `index.html`.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole game — markup, styles and script in one file |
| `brand-daytona-50-of-words.png` | Primary artwork used in the app and for its install icon |
| `manifest.webmanifest` | Home-screen install metadata |
| `sw.js` | Offline caching. Page is network-first, assets cache-first |
| `make-icon.py` | Renders the primary artwork into standard and maskable app icons on macOS |

Best times and settings live in each browser's local storage, so every device
keeps its own record.
