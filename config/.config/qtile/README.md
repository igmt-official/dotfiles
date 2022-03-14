# Qtile (Arch Based)
If you want to use my own config, then follow all my steps.

## Application Launcher
For my launcher i use rofi, to installed rofi use this command:

```bash
sudo pacman -S rofi
```

If you want to use my theme, just go to this link **[Adi1090x](https://github.com/adi1090x/rofi#installation)** and follow the steps for installation.

After installation, copy my ```launcher.sh``` on this link **[rofi](https://github.com/igmt-official/dotfiles/tree/main/config/.config/rofi/launchers/colorful)**,
after that paste it to this directory ```~/.config/rofi/launchers/colorful/```.

And for my keybinding, i had it already on my ```keys.py``` but if you want to set it on your own ```.py``` files, add this line.
```python
([mod], "m", lazy.spawn(os.path.expanduser('~/.config/rofi/launchers/colorful/launcher.sh'))),
```
