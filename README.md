# Czech-US ISO Keyboard Layout

A custom XKB keyboard layout for bilingual Czech/English typists who use US QWERTY but need to write Czech text efficiently.

## The Problem

If you have muscle memory for US keyboard layout but occasionally need to write in Czech, switching to a Czech keyboard is painful—all the symbols are in different places. This layout solves that problem.

## The Solution

This layout keeps your US keyboard muscle memory intact while making Czech diacritics easily accessible:

- **Czech letters** replace the number row: `+ěščřžýáíé`
- **US symbols** work normally with Shift: `!@#$%^&*()`
- **Numbers** are available via Level3 modifier: `1234567890`
- **Czech shifted symbols** also via Level3 (acts like Shift on Czech keyboard)

### Special Characters

| Key | Normal | Shift | Level3 |
|-----|--------|-------|--------|
| 1   | `+`    | `!`   | `1`    |
| 2   | `ě`    | `@`   | `2`    |
| 3   | `š`    | `#`   | `3`    |
| 4   | `č`    | `$`   | `4`    |
| 5   | `ř`    | `%`   | `5`    |
| 6   | `ž`    | `^`   | `6`    |
| 7   | `ý`    | `&`   | `7`    |
| 8   | `á`    | `*`   | `8`    |
| 9   | `í`    | `(`   | `9`    |
| 0   | `é`    | `)`   | `0`    |
| `[` | `[`    | `{`   | `ú`    |
| `;` | `;`    | `:`   | `ů`    |
| `\` | `\`    | `|`   | `ň`    |

### Level3 Modifier

The **extra key between Left Shift and Z** (present on ISO keyboards, often labeled `|\*&` or `<>|`) acts as the Level3 modifier. Hold it to access numbers and Czech shifted symbols.

## Requirements

- **ISO keyboard** (International English layout with extra key next to Left Shift)
  - Please open an issue if you'd like to use this layout on and ANSI keyboard.
- Linux with XKB support (tested on Fedora 43 GNOME Wayland)
  - If you know how layouts work on Windows, Mac, and would like to see it there please feel free to open a pull request!

## Installation

### Manual

```bash
# Create directories
mkdir -p ~/.config/xkb/rules ~/.config/xkb/symbols

# Copy files
cp symbols/cz_us_iso ~/.config/xkb/symbols/
cp rules/evdev.xml ~/.config/xkb/rules/
```

### Automated (for people too lazy to copy two files)

> [!CAUTION]
> Needs testing

**uv:**
```bash
uv run https://github.com/martinhoyer/xkb-cz-us-iso/raw/main/install.py
```

Then restart your session or reload XKB configuration.

## Activation

### GNOME (Wayland/X11)

1. Open **Settings** → **Keyboard** → **Input Sources**
2. Click **+** to add a new input source
3. Search for "Czech (US layout, ISO keyboard)" or "cs-en-iso"
4. Select it and click **Add**

### KDE Plasma

1. Open **System Settings** → **Input Devices** → **Keyboard** → **Layouts**
2. Click **Add** and search for "cz_us_iso"
3. Select and apply

## Usage Tips

- **Caps Lock** works normally for capitals: `Ě`, `Š`, `Č`, `Ú`, `Ů`, etc.
- **Dead keys** on backtick (´ acute) and equals (ˇ caron) allow combining diacritics
- All US keyboard shortcuts (`Ctrl+C`, `Ctrl+V`, etc.) work unchanged

## Full Layout Reference

See [LAYOUT.md](LAYOUT.md) for a complete visual keyboard layout and character mapping.

## Who This Is For

- Czech speakers who primarily use US keyboard layout
- Programmers who code in English but write documentation in Czech
- Anyone with US keyboard muscle memory who needs occasional Czech input
