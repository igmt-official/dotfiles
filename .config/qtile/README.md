# Qtile (Arch Based)

![2022-03-17-13:01:04-screenshot](https://user-images.githubusercontent.com/96023410/158740629-9960d26f-6fb0-479d-9d6c-ac4a26809ec3.png)
![2022-03-17-12:55:33-screenshot](https://user-images.githubusercontent.com/96023410/158740646-7eb3fb8f-626c-46c6-8ed2-36faa710e765.png)
![2022-03-17-00:38:15-screenshot](https://user-images.githubusercontent.com/96023410/158740655-76166b97-1cdb-4a86-8ae3-6d568a11174b.png)

# Table of Contents
- [About](#about)
- [One Time Installation](#one-time-installation)
- [Installing My Qtile](#installing-my-qtile)
- [My Qtile Features](#my-qtile-features)

# About

Why i use **Qtile**?
so i am new in arch linux and installing of display manager or window manager,
i tried to install different window manager and it took me weeks to expirement each different window manager,
and i'm and stuck and struggle because i don't know how i will customize it from scratch because i don't understand what language they are,
so while i'm exploring different window manager, i fount **Qtile** is written **Python** language, now here's the thing why i decide to use **Qtile**,
it because i am a **Python Developer** so it easy to me to understand what code inside their config, and i can customize it from scratch.

# One Time Installation

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles.git && cd dotfiles
```

Now we have to change permission our script to be a excutable:

```bash
chmod +x install.sh
```

# Installing My Qtile

If you want to use my own config, then follow all my steps.

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles.git
```

First Install Our Dependencies:

Download the font that i'm using **[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip)**.
And follow this **[installation guide](https://github.com/igmt-official/dotfiles#font)**.

Now install **Python Pip** and **Psutil**:

```bash
sudo pacman -S python-pip # This is for pip installer.
pip install psutil # Required for some widget on the bar.

sudo pacman -S network-manager-applet volumeicon # This is for my System Tray.
```

Copy my configs:

```bash
cp -r dotfiles/.config/qtile ~/.config
```

Test it with **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile
```

# My Qtile Features

If you only want specific features from my qtile customized, you can check it below.

- [Alacritty](https://github.com/igmt-official/dotfiles/tree/main/.config/alacritty)
- [ZSH](#zsh)
- [Neofetch](https://github.com/igmt-official/dotfiles/tree/main/.config/neofetch)
- [Neovim](https://github.com/igmt-official/dotfiles/tree/main/.config/nvim)
- [Rofi](#application-launcher)
- [Thunar](#thunar)
- [QuteBrowser](https://github.com/igmt-official/dotfiles/tree/main/.config/qutebrowser)
- [Dunst](https://github.com/igmt-official/dotfiles/tree/main/.config/dunst)
- [Scrot](https://github.com/igmt-official/dotfiles/tree/main/.config/scrot)
- [Spotify](#spotify)
- [Theme](#theme)

# Zsh

Install **[Zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)**:

```bash
sudo pacman -S zsh
```

Setup our zsh and make it default shell:

```bash
zsh
0 # To create .zshrc file for customizing.

chsh -l # To list all installed shells.
chsh -s /usr/bin/zsh # And to set one as default for your user do.

# And now reboot your pc.
```

Now if you want to customize your **zsh**, we need to install **Oh My Zsh** and **Powerlevel10k Theme**:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" # This is for installing "Oh My Zsh".

git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k # Next install our "powerlevel10k theme".

# Set "ZSH_THEME="powerlevel10k/powerlevel10k" in "~/.zshrc".

# Now restart your terminal, and follow all step in p10k for configuring your style. 
```
If you want my theme which is dracula theme with semi modified by me, copy my **.p10k.zsh**:

```bash
cp -r dotfiles/.p10k.zsh ~
```

Next is we can install plugin in **zsh** like **autosuggestion**, **syntax highlighting** and **completions**,
just follow my steps.

```bash
# First Install Autosuggestion.
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
# Then edit your ".zshrc", find this line "plugins=(git)" then paste this line below that code.
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

# Second Install Syntax Highlighting.
git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.zsh/zsh-syntax-highlighting
# Then paste it again this line in below of "plugins=(git)".
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# For the final Install Completion.
git clone https://github.com/zsh-users/zsh-completions ~/.zsh/zsh-completions
# Then paste it again this line in below of "plugins=(git)".
source ~/.zsh/zsh-completions/zsh-completions.plugin.zsh
```

If you want to use my **syntax-highlighting** theme which is dracula theme just copy my **.zshrc**, and make sure you already installed all plugins above.

```bash
cp -r dotfiles/.zshrc ~
```

# Thunar

Install **[Thunar](https://wiki.archlinux.org/title/thunar)**:

```bash
sudo pacman -S thunar
```

# Spotify

Install **[Spotify](https://wiki.archlinux.org/title/spotify)**:

```bash
yay -S spotify # Make sure you already setup your "AUR Helper" you can find my tutorial in home page of this dotfiles repository.
```

Now let's customize our **Spotify**, first install **[Spicetify](https://github.com/spicetify/spicetify-cli/wiki/Installation#shell-pre-built-binary---recommended)**:

```bash
yay -S spicetify-cli
```

**Note for Linux users**
**Spotify installed from AUR**

Before applying Spicetify, you need to gain write permission on Spotify files, by running command:

```bash
sudo chmod a+wr /opt/spotify
sudo chmod a+wr /opt/spotify/Apps -R
```

**Note:** Your Spotify client location might be different.

After that we are going to clone **[Spicetify Themes](https://github.com/spicetify/spicetify-themes)**:

```bash
git clone https://github.com/spicetify/spicetify-themes.git
```

Copy the files into the **Spicetify Themes** folder. Run:

```bash
cd spicetify-themes
cp -r * ~/.config/spicetify/Themes
```

Now let's apply our themes, which is mine is **[Dribbblish](https://github.com/spicetify/spicetify-themes/tree/master/Dribbblish)**:

```
cd "$(dirname "$(spicetify -c)")/Themes/Dribbblish"
mkdir -p ../../Extensions
cp dribbblish.js ../../Extensions/.
spicetify config extensions dribbblish.js
spicetify config current_theme Dribbblish color_scheme base
spicetify config inject_css 1 replace_colors 1 overwrite_assets 1
spicetify apply
```

You can pick what you one **[Spicetify Themes](https://github.com/spicetify/spicetify-themes)**.

# Theme

Download **[Dracula](https://www.gnome-look.org/s/Gnome/p/1687249)**.
And follow this **[installation guide](https://github.com/igmt-official/dotfiles#gtk-theming)**.

You can also copy my config:

```bash
cp -r dotfiles/.gtkrc-2.0 ~ # This will be placed on Root Folder.
cp -r dotfiles/.config/gtk-3.0 ~/.config
```
