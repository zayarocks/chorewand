# Magic Chore Wand

An ESP32-based handheld device that uses NFC tags to record the completion of household tasks. The wand provides audiovisual feedback through a NeoPixel LED ring and an MP3 playback module while synchronizing task completion with a web-based chore tracker.

## Parts List

| Component | Unit Price |
|---|---:|
| ESP32 | $3.00* |
| WS2812B NeoPixel ring | $2.00* |
| PN532 NFC reader | $4.00* |
| NTAG215 NFC sticker | $0.25* |
| DFPlayer Mini | $2.40 |
| 8GB microSD card | $4.25 |
| 8Ω 1W miniature speaker | $0.90 |
| Momentary push button (homemade) | $0.50 |
| Miscellaneous electronic components | $1.00* |
| 3D-printed enclosure | $1.00* |
| **Total** | 🟢 **$19.30** |

**IMAGINARY BUDGET**: $20 USD  

## Repository Structure

- `wand/` — ESP32 firmware, wiring instructions, and 3D-printable enclosure.
- `app/` — Chore tracker, web interface, and API.
- `assets/` — Printable chore cards and MP3 sound effects.

## In the Wild

- [Chorecast](https://github.com/KenWeTech/Chorecast) - Open-source, self-hosted NFC chore management system (JavaScript, Node.js, MQTT).
- [TappRFID](https://tapprfid.com/) - NFC-based routine and habit tracking.
- [TagTrack](https://tag-track.app/) - Gamified NFC and QR-based habit tracking.
- [Ritlum](https://ritlum.com/app/) - NFC habit tracking with a physical progress display.
- [Done When](https://donewhen.pro/features) - NFC-enabled household chore management.
- [NFC Smart Chore Tracker](https://github.com/lvlarco/chore-tracker) - Open-source Raspberry Pi and Flask chore tracker.
- [TaskMate](https://github.com/tempus2016/taskmate) - Home Assistant-based NFC chore and reward system.
