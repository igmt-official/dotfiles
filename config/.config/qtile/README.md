# Qtile (Arch Based)
If you want to use my own config, then follow all my steps.

## Application Launcher
For my launcher i use rofi, to installed rofi use this command:

```bash
sudo pacman -S rofi
```

For customizing rofi, just go to this link **[Adi1090x](https://github.com/adi1090x/rofi#installation)** and follow the steps.

After you pick your own theme, add this line in your keybinding:

```python
([mod], "m", lazy.spawn(os.path.expanduser('~/.config/rofi/launchers/colorful/launcher.sh'))),
```
