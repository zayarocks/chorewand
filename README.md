# $\color{red}{\textbf{T}}\color{orange}{\textbf{h}}\color{gold}{\textbf{e}}\ \color{green}{\textbf{M}}\color{blue}{\textbf{a}}\color{purple}{\textbf{g}}\color{red}{\textbf{i}}\color{orange}{\textbf{c}}\ \color{gold}{\textbf{C}}\color{green}{\textbf{h}}\color{blue}{\textbf{o}}\color{purple}{\textbf{r}}\color{red}{\textbf{e}}\ \color{orange}{\textbf{W}}\color{gold}{\textbf{a}}\color{green}{\textbf{n}}\color{blue}{\textbf{d}}$ 🪄 

**Imaginary Budget**: $20 USD / 0.00033696 BTC

An ESP32-based handheld device that uses NFC tags to record the completion of household tasks. The wand provides audiovisual feedback through a NeoPixel LED ring and an MP3 playback module while synchronizing task completion through a custom API.

## The Magic Wand 🪄
The wand reads a chore card's NFC tag and sends its unique ID to the API. Upon successful completion, the NeoPixel ring lights up and the DFPlayer Mini plays a celebratory sound.

## Chore Cards
Chore cards are customizable cards backed with NFC stickers, each associated with a specific household task. Tapping a card with the wand records task completion and triggers audio-visual feedback.

Each chore card is registered by scanning its NFC sticker and assigning its unique ID to a chore in the system. Subsequent scans send that ID to the API, which records the task's completion timestamp.


## Cost Breakdown

| Component | Unit Price |
|---|---:|
| ESP32 | $1.09 |
| WS2812B NeoPixel ring | $1.44 |
| PN532 NFC reader | $1.22 |
| NTAG215 NFC stickers (x37) | $0.17 each|
| DFPlayer Mini | $2.40 |
| 8GB microSD card | $4.25 |
| 8Ω 1W miniature speaker | $0.90 |
| Momentary push button (home-made) | $0.50 |
| 3D-printed enclosure | $0.86 |
| Miscellaneous electronic components | < $1.00 |

| **Total** | | **$19.95** |

_Assumes enough power cables are had to recharge batteries for free._
 
❤️🧡💛 **HOORAY! UNDER BUDGET!** 💚💙💜

## Repo Structure
- `wand/` — ESP32 firmware, STL files, and wiring instructions.
- `api/` — web-based progress tracking (python3)
- `assets/` — Printable chore cards and MP3 sound effects.

## In the Wild
- [Chorecast](https://github.com/KenWeTech/Chorecast) - Open-source, self-hosted NFC chore management system (JavaScript, Node.js, MQTT).
- [TappRFID](https://tapprfid.com/) - NFC-based routine and habit tracking.
- [TagTrack](https://tag-track.app/) - Gamified NFC and QR-based habit tracking.
- [Ritlum](https://ritlum.com/app/) - NFC habit tracking with a physical progress display.
- [Done When](https://donewhen.pro/features) - NFC-enabled household chore management.
- [NFC Smart Chore Tracker](https://github.com/lvlarco/chore-tracker) - Open-source Raspberry Pi and Flask chore tracker.
- [TaskMate](https://github.com/tempus2016/taskmate) - Home Assistant-based NFC chore and reward system.
