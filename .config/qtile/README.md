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

## Fonts

I'm using **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**

## Application Launcher

For my launcher i use **[Rofi](https://wiki.archlinux.org/title/Rofi)**:

```bash
sudo pacman -S rofi
```

## File Manager

I'm using Nautilus:

```bash
sudo pacman -S nautilus
```

## Browser

I'm using **[QuteBrowser](https://wiki.archlinux.org/title/Qutebrowser)**:

```bash
sudo pacman -S qutebrowser
```
