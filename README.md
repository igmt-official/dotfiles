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




