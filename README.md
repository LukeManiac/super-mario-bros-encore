# Super Mario Bros. Encore

**A full campaign mappack for [Mari0: Alesan99's Entities](https://github.com/alesan99/mari0_ae)**

A new journey for the heroes. Well, what awaits them?

---

## Overview

Super Mario Bros. Encore is a full campaign mappack for Mari0 AE by LukeManiac. It takes the classic Super Mario Bros. structure and builds a longer journey across themed worlds, with custom music, new systems and maximised multiplayer support, including a full world map.

The pack includes:

- Multiple themed worlds with their own music
- Full world map
- Checkpoint system
- Dialog / NPC system
- Custom flagpole behaviour
- 32 red coins in total (one per main-game course) — collect them all to unlock the post-game worlds
- Custom power-ups and enemy behaviour
- Animated tiles and event-driven animations
- Maximised multiplayer support (per-player animations for jumps, course clear, unducking, and more)

Author: **LukeManiac**

This mappack is perfectly compatible with the [Mari0 AE Legendary Edition](https://github.com/LukeManiac/mari0-ae-legendary-edition-mod/releases/latest) mod.

---

## Requirements

- [Mari0: Alesan99's Entities](https://github.com/alesan99/mari0_ae) **v13.2 or above**
- Or, preferably, [Mari0 AE Legendary Edition](https://github.com/LukeManiac/mari0-ae-legendary-edition-mod/releases/latest)
- LÖVE 11.x (the version that matches your Mari0 AE build)

This mappack only works on Mari0 AE v13.2 or newer. Older versions will not load it correctly.

---

## Installation

1. Download and extract this repository (or the release zip).
2. Place the entire folder into your Mari0 AE mappacks directory:

   ```
   mari0 / alesans_entities / mappacks /
   ```

   The folder should sit alongside any other mappacks and contain `settings.txt`, the course `.txt` files, `enemies/`, `animations/`, etc.

3. Launch Mari0 AE and select **Super Mario Bros. Encore** (or “smb encore”) from the mappack list.

On Android the path is usually inside the game’s data folder under `mappacks`. Make sure the pack is fully extracted as a normal folder, not left as a zip.

---

## Installation

### Method 1 — GitHub CLI (recommended)

If you have the [GitHub CLI](https://cli.github.com/) installed, you can download the mappack straight into your Mari0 AE mappacks folder.

Note: Installing this mappack while using the Mari0 AE Legendary Edition mod is no different. The mod uses the same directory structure as regular Mari0 AE.

1. Open a terminal.
2. Change into your mappacks directory, then run the clone command.

   **Windows (Command Prompt or PowerShell):**
   ```bash
   cd %APPDATA%\LOVE\mari0\alesans_entities\mappacks
   gh repo clone LukeManiac/super-mario-bros-encore
   ```

   **Mac:**
   ```bash
   cd ~/Library/Application Support/LOVE/mari0/alesans_entities/mappacks
   gh repo clone LukeManiac/super-mario-bros-encore
   ```

   **Linux:**
   ```bash
   cd ~/.local/share/love/mari0/alesans_entities/mappacks
   gh repo clone LukeManiac/super-mario-bros-encore
   ```

   If your Mari0 install uses a different location, navigate to that `mappacks` folder instead.

3. Launch Mari0 AE and select **Super Mario Bros. Encore** (or “smb encore”) from the mappack list.

To download only the latest release zip instead of cloning the full repo:

**Windows:**
```bash
cd %APPDATA%\LOVE\mari0\alesans_entities\mappacks
gh release download --repo LukeManiac/super-mario-bros-encore --pattern "*.zip"
```

**Mac:**
```bash
cd ~/Library/Application\ Support/LOVE/mari0/alesans_entities/mappacks
gh release download --repo LukeManiac/super-mario-bros-encore --pattern "*.zip"
```

**Linux:**
```bash
cd ~/.local/share/love/mari0/alesans_entities/mappacks
gh release download --repo LukeManiac/super-mario-bros-encore --pattern "*.zip"
```

Then extract the zip in place so the folder sits directly inside `mappacks`.

### Method 2 — Manual download

1. Download the repository or the latest release zip from GitHub.
2. Extract it if needed.
3. Place the entire folder into your Mari0 AE mappacks directory:

   ```
   mari0 / alesans_entities / mappacks /
   ```

   The folder should sit alongside any other mappacks and contain `settings.txt`, the course `.txt` files, `enemies/`, `animations/`, etc.

4. Launch Mari0 AE and select **Super Mario Bros. Encore** (or “smb encore”) from the mappack list.

On Android the path is usually inside the game’s data folder under `mappacks`. Make sure the pack is fully extracted as a normal folder, not left as a zip.

---

## Worlds

See the full world list and boss information in [worlds.md](https://www.github.com/LukeManiac/super-mario-bros-encore/blob/main/worlds.md).

### Main Game

| World | Theme       | Final Stage | Boss      |
|-------|-------------|-------------|-----------|
| 1     | Overworld   | Castle      | Larry     |
| 2     | Beach       | Airship     | Boom Boom |
| 3     | Desert      | Castle      | Morton    |
| 4     | Ghost House | Airship     | Wendy     |
| 5     | Jungle      | Castle      | Iggy      |
| 6     | Snow        | Castle      | Lemmy     |
| 7     | Volcano     | Airship     | Roy       |
| 8     | Mountain    | Castle      | Ludwig    |

### Post-game

Worlds 9–16 continue the adventure with new themes (Autumn, Garden, Space, Pipeland and more) and further boss encounters, culminating in a final confrontation with Bowser.

---

## Features & Systems

The mappack includes a large number of custom entities and animation-driven systems:

- **Full world map** – navigate between courses with multiplayer support
- **Checkpoint system** – save progress mid-course with visual feedback
- **Dialog system** – talk to NPCs (Talking Flower, Boo, and others)
- **Custom flagpole** – alternative course-clear behaviour
- **Red coins** – 32 in total (one per main-game course); collect all of them to unlock the post-game worlds
- **Player property changer** and helpers
- **Power-up** classes
- **Enemy baseclass** modifiers
- **Button detection** and hold/unhold logic for multiplayer
- **Course finish actions** (flag jump / flag walk variants per player)
- **Points pop-ups** and various prep / switch animations
- **Subzone loaders** and map-object helpers

Most of these are wired up via the course files and `objects.txt`.

---

## Credits

A full list of audio, graphics and coding contributors is available in [credits.md](https://www.github.com/LukeManiac/super-mario-bros-encore/blob/main/credits.md).

Major thanks go to:

- **JayhabStudios** – music
- **Lood** – majority of the graphics
- **WilliamFrog**, **Britdan**, **Oewertom**, **Skysometric** and others for key custom systems
- **Nintendo** – original sound effects (primarily from Super Mario Bros. Deluxe)
- Everyone who contributed sprites, animations or code

---

## Notes

- The game uses Super Mario Maker physics along with fast falling.
- Lives start at 5.
- Real-time mode, continued subzone music and no coin limit are enabled.
- Overridden sounds and disabled transitions are settings only recognised by the [Mari0 AE Legendary Edition](https://github.com/LukeManiac/mari0-ae-legendary-edition-mod/releases/latest) mod.
- Multiplayer support is maximised, including a full world map and per-player animations for jumps, flag clears, unducking, and more.

If something fails to load, make sure you are on Mari0 AE v13.2 or above (or Legendary Edition) and that no files were lost during extraction.

---

## Licence / Disclaimer

This is a fan-made mappack. Super Mario, related characters and assets belong to Nintendo.  
Please support the official games.

Mari0 itself is by Stabyourself. Alesan99’s Entities is maintained by Alesan99 and contributors.

---

Enjoy the encore.
