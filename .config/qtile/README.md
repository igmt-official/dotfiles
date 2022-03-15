# Qtile (Arch Based)

## Installing My Qtile

If you want to use my own config, then follow all my steps.

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles/.config/qtile.git
```

Copy my configs:

```bash
cp -r dotfiles/.config/qtile ~/.config
```

Install Dependencies:

First download the font that i'm using **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**.

Now install ```Python Pip``` and ```Psutil```:

```bash
sudo pacman -S python-pip # This is for pip installer.
pip install psutil # Required for some widget on the bar.
```

## My Qtile Application

If you only want specific features from my qtile customized, you can check it below.

### Application Launcher

Install **[Rofi](https://wiki.archlinux.org/title/Rofi)**:

```bash
sudo pacman -S rofi
```

If you want to use dracula theme like on my rofi,
just follow the steps **[here](https://github.com/igmt-official/dotfiles/tree/main/.config/rofi)**.

### File Manager

Install **[Thunar](https://wiki.archlinux.org/title/thunar)**:

```bash
sudo pacman -S thunar
```

### Browser

Install **[QuteBrowser](https://wiki.archlinux.org/title/Qutebrowser)**:

```bash
sudo pacman -S qutebrowser
```

### Theme

Download **[Dracula](https://www.gnome-look.org/s/Gnome/p/1687249)**

### Fonts

Download **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**
