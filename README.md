my dotfiles inspired by: https://github.com/antoniosarosi/dotfiles

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
here's my way to install Arch Linux, this is not fully completed installation because, this is all
that i did on my installation.

## Reminder
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
# To check available Region, type "ls /usr/share/zoneinfo/Region" and find your Region.
# To check available City, type "ls /usr/share/zoneinfo/Your_Region/City" and find your City.
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

Follow this step this is essentials, this is only for None-UEFI (MBR).
```bash
grub-install --target=i386-pc /dev/sda
# "/dev/sda" is the main disk not the one we created partition.
# "--target=i386-pc" is only for Non-UEFI (MBR).

grub-mkconfig -o /boot/grub/grub.cfg # Remember this is only for Non-UEFI (MBR)
```

Installed our essentials and optional package:
```bash
pacman -S base-devel xorg xorg-xinit git nodejs npm networkmanager alacritty qutebrowser dmenu

# Essential List:
# networkmanager (For our internet)
# qutebrowser (Or your prefer browser)
# alacritty (or your prefer terminal (cmd))
# dmenu (To launch our apps)

# Optional List:
# base-devel (This is a package group that includes tools needed for building (compiling and linking)).
# xorg and xorg-xinit (For me this is a essential because for the one didn't want to use a "Display Manager" like me use this to start your "Window Manager").
# git, nodejs, npm (For me this is also essential because sometimes we install modules or packages is needed git, nodejs, or npm).
```

Exit:
```bash
exit
```

Umount:
```bash
umount /mnt
```

Now all the setup is finish try to reboot and unplug the bootable usb, let see if our Arch Linux will boot normal.
```bash
reboot
```
