Install **[Scrot](https://wiki.archlinux.org/title/Screen_capture#scrot)**:

```bash
sudo pacman -S scrot
```

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles.git
```

Copy my configs:

```bash
cp -r dotfiles/.config/scrot ~/.config
```

And make it excutable script:

```bash
chmod +x screenshot
```

# KeyMap

| Key                                 | Action                             |
| ------------------------------------| -----------------------------------|
| **mod + s**                         | Screenshot                         |
| **mod + shift + s**                 | Screenshot Selected Area           |
| **mod + control + shift + s**       | Screenshot Focus Window            |

