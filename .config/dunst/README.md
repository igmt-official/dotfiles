Install **[Dunst](https://wiki.archlinux.org/title/Dunst)**.

And if you want to use my config, just copy my config **[Dunst](https://github.com/igmt-official/dotfiles/tree/main/.config/dunst)**

```bash
sudo pacman -S dunst
```

First copy the default **dunstrc** file on our config folder:

```bash
cp /etc/dunst/dunstrc .config/dunst/dunstrc
```

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles.git
```

Copy my configs:

```bash
cp -r dotfiles/.config/dunst ~/.config
```

Also i have **[Custom Scripts](https://github.com/igmt-official/dotfiles/tree/main/.local/bin)**, for wifi, screenshot, and volume notificiation.
