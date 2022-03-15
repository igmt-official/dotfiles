# Qtile (Arch Based)
If you want to use my own config, then follow all my steps.

Install Dependencies:

```bash
sudo pacman -S python-pip # This is for pip installer.
yay -S nerd-fonts-ubuntu-mono # This is the font im using.
pip install psutil # Required for some widget on the bar.
```

Clone this repository and copy my configs:

```bash
git clone https://github.com/igmt-official/dotfiles.git
cp -r dotfiles/.config/qtile ~/.config
```

If you only want specific features from my qtile customized, you can check it below.

## Application Launcher

For my launcher i use rofi:

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

## File Manager

I'm using Nautilus:

```bash
sudo pacman -S nautilus
```
