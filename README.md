my dotfiles inspired by: https://github.com/antoniosarosi/dotfiles

# Repository

Clone my repository, and go to this folder **[.config](https://github.com/igmt-official/dotfiles/tree/main/.config)**,
and find what you want config, each config already have installion guide.

```bash
https://github.com/igmt-official/dotfiles.git
```

# Table of Contents

- [Overview](#overview)
- [Arch installation](#arch-installation)
- [Qtile Installation](#qtile-installation)
- [Qtile Basic System Utilities](#qtile-basic-system-utilities)
  - [Wallpaper](##wallpaper)
  - [Font](#font)
  - [Audio](#audio)
  - [Brightness](#brightness)
  - [Monitors](#monitors)
  - [Network](#network)
  - [Systray](#systray)
  - [Xinitrc](#xinitrc)
  - [File Manager](#file-manager)
  - [Trash](#trash)
  - [Multimedia](#multimedia)
    - [Images](#images)
    - [Video and audio](#video-and-audio)
  - [Color Picker](#color-picker)
- [AUR Helper](#aur-helper)
- [GTK Theming](#gtk-theming)
- [Custom Script](#custom-script)

# Overview

This guide will walk you through the process of building a desktop environment
starting with a fresh Arch based installation. I will assume that you are
comfortable with Linux based operating systems and command line interfaces.
Because you are reading this, I will also assume that you've looked through some
"tiling window manager" videos on Youtube, because that's where the rabbit hole
starts. You can pick any window managers you want, but I'm going to use Qtile
as a first tiling window manager because that's what I started with. This is
basically a description of how I made my desktop environment from scratch.

# Arch installation

The starting point of this guide is right after a complete clean Arch based
distro installation, i've been searching a lot guide for installation Arch Linux,
and i read the documents about **[Arch Wiki](https://wiki.archlinux.org/index.php/Installation_guide)**
here's my way to install Arch Linux, this is not fully completed installation because, this is the only
that i did on my installation.

### Reminder
This is only for Non-UEFI (MBR) installation, i told you before, this is my way to install Arch Linux, 
i just based on my specs desktop, if you are UEFI users then go to youtube there's a lot tutorial for UEFI.

Make sure you have an internet, if you have response for that website, then proceed to the next step.
And if you don't have response on that ping, you don't have an internet, or you're not connected in Ethernet Lan Cable,
for that search on youtube, because remember this is only my way, i didn't setup my internet in wireless.

```bash
ping archlinux.org
```

Update the system clock
Use timedatectl to ensure the system clock is accurate:

```bash
timedatectl set-ntp true 
# To check the service status, use timedatectl status.
```

Partition the disks
When recognized by the live system, disks are assigned to a block device such as /dev/sda, /dev/nvme0n1 
or /dev/mmcblk0. To identify these devices, use lsblk or fdisk.

```bash
fdisk -l
# And my block device is "/dev/sda"
```

Use fdisk or parted to modify partition tables. For example:

```bash
fdisk /dev/the_disk_to_be_partitioned
# Remember to check your block device such as /dev/sda, /dev/nvme0n1 or /dev/mmcblk0
# For me is "fdisk /dev/sda"
```

Now, jus follow my command line, to make our partition.

```bash
# Type "o" to create MBR partition.
# Type "n" then press enter until you see the second "default with random numbers" then type "+2GB" this is will create our "Swapfile Partition".
# Type "n" again then press enter until the end, because this is our "Root Parition" so the rest of our disk size will be put in here.

# Remember the first one is "Swapfile Partition" that partition name is "/dev/sda1/ and the second one is our "Root Partition" "/dev/sda2/".
# Now type "t" to change our partition type, type "1" for our "Swapfile Partition (/dev/sda1)" and then type "L" to check all list partition type, find the type of "Linux Swap" then enter that code.
# And do it again on our "Root Partition" type "t", now type "2" this is our "Root Partition (/dev/sda2/)" and then type "L" again check all list partition type, find the type of "Linux" then enter that code.

```

Format the partitions
Once the partitions have been created, each newly created partition must be formatted with an appropriate file system.

```bash
 mkfs.ext4 /dev/root_partition # This is the our "Root Partition" for me is "mkfs.ext4 /dev/sda2/.
 mkswap /dev/swap_partition # And this is our "Swapfile Partition" for me is "mkswap /dev/sda1/.
 ```
 
 And now we done formatting our partition, next step is to turn on our "Swapfile" and mount "mnt" in our "Root Partition".
 
 ```bash
 swapon /dev/swap_partition # To turn on our "Swapfile Partition", for me is "swapon /dev/sda1".
 mount /dev/root_partition /mnt # To mount our "mnt" in our "Root Partition", for me is "mount /dev/sda2 /mnt".
 ```
 
Install essential packages
Use the pacstrap script to install the base package, Linux kernel and firmware for common hardware:

```bash
pacstrap /mnt base linux linux-firmware
# Wait for the download completed.
```

Fstab
Generate an fstab file (use -U or -L to define by UUID or labels, respectively):

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```

Chroot
Change root into the new system:

```bash
arch-chroot /mnt
```

Time zone
Set the time zone:

```bash
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime # For me is "ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime".
# To check available Region, type "ls /usr/share/zoneinfo/Region" and find your Region".
# To check available City, type "ls /usr/share/zoneinfo/Your_Region/City" and find your City".
```

Run hwclock to generate /etc/adjtime:

```bash
hwclock --systohc
```

Now installed our text editor ```nano or vim``` which one you prefer.

```bash
pacman -S nano
```

Localization.

```bash
nano /etc/locale.gen
# Edit "/etc/locale.gen" and uncomment "en_US.UTF-8 UTF-8" and other needed locales. 
```

Generate the locales by running:

```bash
locale-gen
```

Create the locale.conf file, and set the LANG variable accordingly:

```bash
nano /etc/locale.conf
# Now write this "LANG=en_US.UTF-8" according to your localization then save it.
```

Create the hostname file:

```bash
nano /etc/hostname
# Write your prefer hostname for me is "myArch"
```

Edit the hosts file:

```bash
nano /etc/hosts
# Now you will see two lines that already writed in there, below of that two lines write this:
127.0.0.1 localhost
::1 localhost
127.0.1.1 yourHostname # for me is "127.0.1.1 myArch"
```

Root password
Set the root password:

```bash
passwd
# Type your prefer password.
```

Add user and password

```bash
useradd -m yourUserName # For me is "useradd -m myArch".
passwd yourUserName # And type your prefer password.
```

User groups

Non-root workstation/desktop users often need to be added to some of following groups to allow access to hardware peripherals and facilitate system administration:
```bash
usermod -aG wheel,audio,video,optical,storage,input,disk yourUserName
```

Now installed sudo:
```bash
pacman -S sudo
```

Edit **Sudo** with nano or vim:

```bash
EDITOR=nano visudo
```

Uncommenting this line:

```bash
# Find this line:

## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL

# And now uncomment "# %wheel ALL=(ALL) ALL".
# This should be the result:

## Uncomment to allow members of group wheel to execute any command
%wheel ALL=(ALL) ALL
```

Follow this step this is essentials, this is only for None-UEFI (MBR).

```bash
grub-install --target=i386-pc /dev/sda
# "/dev/sda" is the main disk not the one we created partition.
# "--target=i386-pc" is only for Non-UEFI (MBR).

grub-mkconfig -o /boot/grub/grub.cfg # Remember this is only for Non-UEFI (MBR)
```

Installed our essentials and optional package:
```bash
pacman -S base-devel xorg xorg-xinit git nodejs npm networkmanager alacritty firefox rofi mesa

# Essential List:
# networkmanager (For our internet)
# firefox (Or your prefer browser)
# alacritty (or your prefer terminal (cmd))
# rofi (To launch our apps)
# mesa (For Intel and Amd only)

# Optional List:
# base-devel (This is a package group that includes tools needed for building (compiling and linking)).
# xorg and xorg-xinit (For me this is a essential because for the one didn't want to use a "Display Manager" like me use this to start your "Window Manager").
# git, nodejs, npm (For me this is also essential because sometimes we install modules or packages is needed git, nodejs, or npm).
```

Before we reboot, enable first ```networkmanager```.

```bash
systemctl enable NetworkManager
```

Now all the setup is finish we will exit and umount and try to reboot and unplug the bootable usb, let see if our Arch Linux will boot normal.

```bash
exit
umount /mnt
reboot
```

And now we boot normally, try to login your "User and Pass".

# Qtile installation
Now installed our ```Window Manager``` which is ```Qtile```.

```bash
sudo pacman -S qtile
```

And setup our ```Qtile``` in ```.xinitrc``` so we can enter in window manager.

```bash
# Edit your .xinitrc using your text editor like "nano or vim"
nano .xinitrc

# Now go to the bottom of all codes in there, and put this line:
exec qtile start
```

To enter in our ```Qtile``` window manager, enter this line:
```bash
startx
```

Now that you're in Qtile, you should know some of the default keybindings.

| Key                  | Action                     |
| -------------------- | -------------------------- |
| **mod + return**     | launch xterm               |
| **mod + k**          | next window                |
| **mod + j**          | previous window            |
| **mod + w**          | kill window                |
| **mod + [asdfuiop]** | go to workspace [asdfuiop] |
| **mod + ctrl + r**   | restart qtile              |
| **mod + ctrl + q**   | logout                     |

Before doing anything else, if you don't have a US keyboard, you should
change it using *setxkbmap*. To open xterm use **mod + return**. For example to
change your layout to spanish:

```bash
setxkbmap es
```

Now open the config file:

```bash
nano ~/.config/qtile/config.py
```

At the beginning, after imports, you should find an array called *keys*,
and it contains the following line:

```python
Key([mod], "Return", lazy.spawn("xterm")),
```

Change that line to launch your terminal emulator:

```python
Key([mod], "Return", lazy.spawn("alacritty")),
```

Then add keybindings for rofi programs that we are installed lately:

```python
Key([mod], "m", lazy.spawn("rofi -show run")),
Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
```

Now restart Qtile with **mod + control + r**. You should be able to open your
menu and terminal emulator with keybindings. If you picked rofi, you can
change its theme like so:

```bash
sudo pacman -S which
rofi-theme-selector
```

That's it for Qtile, now you can start hacking on it and make it your own.
Checkout my custom Qtile config
[here](https://github.com/igmt-official/dotfiles/config/.config/qtile).
But before that I would recommend configuring basic utilities like audio,
battery, mounting drives, etc.

# Qtile Basic System Utilities
In this section we will cover some software that almost everybody needs on their system.

## Wallpaper

First things first, your screen looks empty and black, so you might want to have
a wallpaper not to feel so depressed. You can open ```firefox``` through ```rofi```
using **mod + m** and download one. Then install
**[feh](https://wiki.archlinux.org/index.php/Feh)** or
**[nitrogen](https://wiki.archlinux.org/index.php/Nitrogen)**
and and set your wallpaper:

```bash
sudo pacman -S feh
feh --bg-scale path/to/wallpaper
```

## Font

Download Nerd-Font:
Go to **[NerdFont](https://www.nerdfonts.com/font-downloads)** and hit downloads. This will give you a page where you can preview different fonts.
Once you find a font you like, hit Download on the font to save it as a .zip.

Setup the File Path:
Make a folder for fonts in defaulit path: ```~/.local/share/(fonts)```
and go to that folder fonts location.x
```bash
mkdir ~/.local/share/fonts && cd ~/.local/share/fonts
```
Extract Files and Install:
Now that we have our directory set-up we can locate our .zip file and copy it over:
```bash
cp ~/Downloads/SampleNerdFont.zip ~/.local/share/fonts
```

Now that we are in the directory fonts we will extract the file:
```bash
unzip SampleNerdFont.zip
# Note if you don't installed unzip yet, then installed it by "sudo pacman -S unzip"
```
Finalization
Now that your font files are in a directory recognized by fontconfig they should be loaded automatically on boot and made available to applications in your window manager.

To reload the fonts without rebooting you can run as root:
```bash
fc-cache -fv
```

Now try to change your font in terminal and try to copy and paste icon from **[NerdFont](https://www.nerdfonts.com/font-downloads)**.

## Audio

There is no audio at this point, we need
**[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**.
I suggest also installing a graphical program to control audio like
**[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**,
because we don't have keybindings for that yet:

```bash
sudo pacman -S pulseaudio pavucontrol
```

On Arch,
[pulseaudio is enabled by default](https://wiki.archlinux.org/index.php/PulseAudio#Running),
but you might need to reboot in order for it to actually start. After rebooting,
you can open *pavucontrol* through *rofi*, unmute the audio, and you should be
just fine.

Now you can set up keybindings for *pulseaudio*, open Qtile's config.py and add
these keys:

```python
# Volume
Key([], "XF86AudioLowerVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ -5%"
)),
Key([], "XF86AudioRaiseVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ +5%"
)),
Key([], "XF86AudioMute", lazy.spawn(
    "pactl set-sink-mute @DEFAULT_SINK@ toggle"
)),
```

For a better CLI experience though, I recommend using
**[pamixer](https://www.archlinux.org/packages/community/x86_64/pamixer/)**:

```bash
sudo pacman -S pamixer
```

Now you can turn your keybindings into:

```python
# Volume
Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
```

Restart Qtile with **mod + control + r** and your keybindings should work.

## Brightness

If
you're on a laptop, you might also want to control the brightness of your screen,
and for that I recommend
**[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**:

```bash
sudo pacman -S brightnessctl
```

You can add these keybindings and restart Qtile after:

```python
# Brightness
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
```

## Monitors

If you have a multi-monitor system, you surely want to use all your screens.
Here's how **[xrandr](https://wiki.archlinux.org/index.php/Xrandr)** CLI works:

Install xrander:
```bash
sudo pacman -S xrander
```

List all available outputs and resolutions
```bash
xrandr
# Now because this is my setup, i have different situation, i have external monitor, and my laptop display is broke, so here's my settings.
xrandr --output LVDS-1 --off --output HDMI-1 --mode 1920x1080 --primary # This will turn off my laptop display and make it primary my external monitor.
```

Now here's the thing, this is only my optional, because i don't use multi monitor,
but if you want to activate multi monitor then procceed in this steps.

We need to specify the position for each output, otherwise it will default to
0x0, and all your outputs will be overlapped. Now if you don't want to calculate pixels
and stuff you need a GUI like
**[arandr](https://www.archlinux.org/packages/community/any/arandr/)**:

```bash
sudo pacman -S arandr
```

Open it with *rofi*, arrange your screens however you want, and then you can
save that layout, which will basically give you a shell script with the exact
*xrandr* command that you need. Save that script, but don't click "apply" just
yet.

For a multi-monitor system, it's recommended to create an instance of a
*Screen* object for each monitor in your Qtile config.

You'll find an array called *screens* which contains only one object
initialized with a bar at the bottom. Inside that bar you can see the default
widgets that come with it.

Add as many screens as you have and copy-paste all widgets, later you can
customize them. Now you can go back to arandr, click *apply*, and then restart
Qtile.

Now your multi-monitor system should work.

## Network

We have configured the network through *nmcli*, but a graphical frontend is
more friendly. I use
**[nm-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**:

```bash
sudo pacman -S network-manager-applet
```

## Systray

By default, you have a system tray in Qtile, but there's nothing running in it.
You can launch the programs we've just installed like so:

```bash
nm-applet &
```

Now you should see icons that you can click to configure drives and networking.
Optionally, you can install tray icons for volume and battery:

In qtile we have default systray, this is only optional
Installed volume and battery:

```bash
sudo pacman -S volumeicon cbatticon
```

Launch it:

```bash
volumeicon &
cbatticon &
```

## Xinitrc

As I have mentioned before, all these changes are not permanent. In order to
make them permanent, we need a couple things. First, install
**[xinit](https://wiki.archlinux.org/index.php/Xinit)**:


```bash
sudo pacman -S xorg-xinit
```

Now you can use *~/.xinitrc* to run programs before your window manager starts:

```bash
touch ~/.xinitrc
```

For example, if you place this in *~.xinitrc*:

```bash
xrandr --output LVDS-1 --off --output HDMI-1 --mode 1920x1080 --primary &
setxkbmap es &
nm-applet &
volumeicon &
cbatticon &
```

Every time you login you will have all systray utilities, your keyboard layout
and monitors set.

## File Manager

We've done all files stuff through a terminal up to this point, but you can
install graphical or terminal based file managers.
For a graphical one, I suggest
**[thunar](https://wiki.archlinux.org/index.php/Thunar)**
and for a terminal based one,
**[ranger](https://wiki.archlinux.org/index.php/Ranger)**, although this one
is very vim-like, only use it if you know how to move in vim.

```bash
sudo pacman -S thunar
```

## Trash

If you don't want to *rm* all the time and potentially lose files, you need a
trashing system. Luckily, that's pretty easy to do, using
[some of these tools](https://wiki.archlinux.org/index.php/Trash_management#Trash_creation)
such as **[glib2](https://www.archlinux.org/packages/core/x86_64/glib2/)**,
and for GUIs like *thunar* you need **[gvfs](https://www.archlinux.org/packages/extra/x86_64/gvfs/)**:

```bash
sudo pacman -S glib2 gvfs
# CLI usage
gio trash path/to/file
# Empty trash
gio trash --empty
```

With *thunar* you can open the trash clicking on the left panel, but on the command
line you can use:

```bash
ls ~/.local/share/Trash/files
```

## Multimedia

There are dozens of programs for multimedia stuff, check
[this page](https://wiki.archlinux.org/index.php/List_of_applications/Multimedia).

### Images

For image previews, one of the best that I could find is
[geeqie](https://www.archlinux.org/packages/extra/x86_64/geeqie/):

```bash
sudo pacman -S geeqie
```

### Video and audio

No doubt
[vlc](https://wiki.archlinux.org/index.php/VLC_media_player_(Espa%C3%B1ol))
is exactly what you need:

```bash
sudo pacman -S vlc
```
## Color Picker

For who want to build their own palette, install color picker.
```bash
sudo pacman -S gcolor3
```

# AUR Helper

Now that you have some software that allows you tu use your computer without
losing your patience, it's time to do more interesting stuff. First, install an
**[AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers)**, I use
**[yay](https://github.com/Jguer/yay)**:

```bash
sudo pacman -S base-devel git # (Which is we installed lately in our installation arch linux)
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R username:username yay-git/
cd yay-git
makepkg -si
```

With an *Arch User Repository helper*, you can basically install
any piece of software on this planet that was meant to run on Linux.

# GTK Theming

Install ```Gtk2``` and ```Gtk3```:

```bash
sudo pacman -S gtk2 gtk3
```

You can find GTK themes [on this page](https://www.gnome-look.org/browse/cat/135/).
Once you have your theme folders downloaded, this is what you do:

```bash
cd Downloads/
sudo pacman -S unzip # For unzipping .zip file.
unzip Sample-Theme.zip
unzip Sample-Theme-Icon.zip
rm Sample-Theme*.zip # To delete all Sample-Theme zip file.
```

Make your themes available

```bash
sudo mv Sample-Theme /usr/share/themes
sudo mv Sample-Theme-Icon /usr/share/icons
```

Now edit **~/.gtkrc-2.0** and **~/.config/gtk-3.0/settings.ini** by adding
these lines:

```ini
# ~/.gtkrc-2.0
gtk-theme-name = "Sample-Theme"
gtk-icon-theme-name = "Sample-Theme-Icon"

# ~/.config/gtk-3.0/settings.ini
gtk-theme-name = Sample-Theme
gtk-icon-theme-name = Sample-Theme-Icon
```

Make sure not to mistype the names of your themes and icons, they should
match the names of the directories where they are located, the ones you can
see in this output:

```bash
ls /usr/share/themes
ls /usr/share/icons
```

Remember that you will only see the new theme if you log in again.
There are also graphical frontends for changing themes, I just prefer the
traditional way of editing files though, but you can use
**[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**,
which is a desktop environment independent GUI for this task, and it lets you
preview themes.

Installing ```Lxappearance```:

```bash
sudo pacman -S lxappearance
```

# Custom Script

To use your custom script, make a directory where you put your **Custom Script**, example:

```bash
mkdir -p $HOME/.local/bin # This will create a bin folder in .local
```

Now we should export that path in our **$PATH**, put this line in our **.bashrc**:

```bash
export PATH=$HOME/.local/bin:$PATH
```

Take note! I'm not talking about executable script, i'm talking about custom script that can access in any package,
like **Scrot**, **Dunst** or **Volume**.
