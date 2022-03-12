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

Now, jus follow my command line, to make our partition
```bash
# Type "o" to create MBR partition.
# Type "n" then press enter until you see the second "default with random numbers" then type "+2GB" this is will create our "Swapfile Partition".
# Type "n" again then press enter until the end, because this is our "Root Parition" so the rest of our disk size will be put in here.

# Remember the first one is "Swapfile Partition" that partition name is "/dev/sda1/ and the second one is our "Root Partition" "/dev/sda2/".
# Now type "t" to change our partition type, type "1" for our "Swapfile Partition (/dev/sda1)" and then type "L" to check all list partition type, find the type of "Linux Swap" then enter that code.
# And do it again on our "Root Partition" type "t", now type "2" this is our "Root Partition (/dev/sda2/)" and then type "L" again check all list partition type, find the type of "Linux" then enter that code.

```
