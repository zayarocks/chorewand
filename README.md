# Magic Chore Wand

An ESP32-based handheld device that uses NFC tags to record the completion of household tasks. The wand provides audiovisual feedback through a NeoPixel LED ring and an MP3 playback module while synchronizing task completion through a custom API.

## Cost Breakdown

**IMAGINARY BUDGET**: $20 USD 

| Component | Unit Price |
|---|---:|
| ESP32 | $1.09 |
| WS2812B NeoPixel ring | $1.44 |
| PN532 NFC reader | $1.22 |
| NTAG215 NFC stickers (37) | $0.17 each|
| DFPlayer Mini | $2.40 |
| 8GB microSD card | $4.25 |
| 8Ω 1W miniature speaker | $0.90 |
| Momentary push button (home-made) | $0.50 |
| Miscellaneous electronic components | $1.00 |
| 3D-printed enclosure | $0.86 |
| **Total** | | **$19.95** |


_Assumes enough power cables are had to recharge batteries for free._
 
❤️🧡💛 **HOORAY! UNDER BUDGET!** 💚💙💜

## Repo Structure
- `wand/` — ESP32 firmware, STL files, and wiring instructions.
- `api/` — web-based progress tracking
- `assets/` — Printable chore cards and MP3 sound effects.

## In the Wild
- [Chorecast](https://github.com/KenWeTech/Chorecast) - Open-source, self-hosted NFC chore management system (JavaScript, Node.js, MQTT).
- [TappRFID](https://tapprfid.com/) - NFC-based routine and habit tracking.
- [TagTrack](https://tag-track.app/) - Gamified NFC and QR-based habit tracking.
- [Ritlum](https://ritlum.com/app/) - NFC habit tracking with a physical progress display.
- [Done When](https://donewhen.pro/features) - NFC-enabled household chore management.
- [NFC Smart Chore Tracker](https://github.com/lvlarco/chore-tracker) - Open-source Raspberry Pi and Flask chore tracker.
- [TaskMate](https://github.com/tempus2016/taskmate) - Home Assistant-based NFC chore and reward system.
