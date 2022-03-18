#!/bin/bash/

echo "#################################################"
echo "Welcome to Igmt-Official Dotfiles"
echo "Written by https://www.reddit.com/u/igmt-official"
echo "#################################################"

echo ""

echo "Note: Please follow the instruction carefully, to avoid cancelling this installation!"
echo "And also make sure you have already installed 'node', 'npm' and 'yay (Aur Helper).'"
echo "Make sure you have a good internet, because we are gonna download some dependencies and packages."
read -p "Do you want to procceed the installation? Type 'Y': " yN0

echo ""

if [ $yN0 == "Y" ]; then

    echo "Installing required dependecies..."
    sudo pacman -S python-pip
    pip install psutil
    sudo pacman -S network-manager-applet volumeicon

    echo ""

    echo "Copying fonts..."
    [ ! -d "$HOME/.local/share" ] && mkdir -p $HOME/.local/share
    cp -r $PWD/.local/share/fonts $HOME/.local/share/

    echo ""

    echo "Copying qtile configuration..."
    [ ! -d "$HOME/.config" ] && mkdir -p $HOME/.config
    cp -r $PWD/.config/qtile $HOME/.config/
    echo "Reloading fonts cache..."
    fc-cache -fv

    echo ""

    echo "Installing Zsh..."
    sudo pacman -S zsh

    echo ""

    echo "######################################"
    echo "Now open your terminal and type: 'zsh'"
    echo "to configure our '.zshrc', type: '0'"
    echo "######################################"

    echo ""

    read -p "If you already done type 'Y' to continue our configuration: "yN1

    if [ $yN1 == "Y" ]; then
        echo "Installing Oh My Zsh..."
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
        echo "Cloning Powerlevel10K Theme..."
        git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
        echo "Cloning Autosuggestion Plugin..."
        git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
        echo "Cloning Syntax Highlighting Plugin..."
        git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.zsh/zsh-syntax-highlighting
        echo "Cloning Auto Completions Plugin..."
        git clone https://github.com/zsh-users/zsh-completions ~/.zsh/zsh-completions
        echo "Copying zsh configuration (this is included p10k theme and syntax highlighting theme)..."
        cp -r dotfiles/.zshrc ~
        echo "Copying p10k configuration..."
        cp -r dotfiles/.p10k.zsh ~
        echo "Installing Neofetch..."
        sudo pacman -S neofetch
        echo "Copying neofetch configuration..."
        # [ ! -d "$HOME/.config/neofetch" ] && mkdir -p $HOME/.config/neofetch/
        cp -r $PWD/.config/neofetch $HOME/.config/

        echo ""
    fi

    echo "Installing Neovim..."
    sudo pacman -S neovim
    echo "Cloning Plugin Manager..."
    git clone --depth 1 https://github.com/wbthomason/packer.nvim\
    ~/.local/share/nvim/site/pack/packer/start/packer.nvim
    echo "Copying neovim configuration..."
    cp -r $PWD/.config/nvim $HOME/.config

    echo ""

    echo "########################################################################################"
    echo "Now follow this steps, to activate all plugins installed on my config."
    echo "Edit '.config/nvim/lua/packer-config/init.lua' in Neovim,"
    echo "to install packer plugin using this command: ':PackerSync'"
    echo "Next try to uncommenting all plugins that have '--' sign"
    echo "and try to install all plugins using this command: ':PackerSync'"
    echo "After that edit '.config/nvim/init.lua' and uncommenting all '--' sign,"
    echo "then save it and reload the Lua Config using this command: ':luafile %'"
    echo ""
    echo "For Lsp Config, you can install what you want language,"
    echo "to install your langauge server go find in Lsp Config documentation in thei github,"
    echo "and edit '.config/nvim/lua/lsp-config/language-servers.lua' to add your language server."
    echo ""
    echo "And for our Treesitter install what you want language,"
    echo "to install use this command: 'TSInstall (language)'"
    echo "Then edit treesitter config '.config/nvim/lua/treesitter-config/init.lua,"
    echo "to add your language ', and uncomment all '--' sign."
    echo "########################################################################################"

    echo ""

    echo "Make sure you followed already all steps to activate our all plugins."
    echo "To avoid error in our Neovim."

    echo ""

    read -p "If you done, type 'Y': "yN2

    echo ""

    if [ $yN2 == "Y" ]; then
        echo "Installing Rofi..."
        sudo pacman -S rofi
        echo "Copying rofi configuration..."
        cp -r $PWD/.config/rofi $HOME/.config

        echo ""

        echo "Installing Thunar..."
        sudo pacman -S thunar

        echo ""

        echo "Installing QuteBrowser..."
        sudo pacman -S qutebrowser
        echo "Copying qutebrowser configuration..."
        [ ! -d "$HOME/.config/qutebrowser" ] && mkdir -p $HOME/.config/qutebrowser
        cp -r dotfiles/.config/qutebrowser $HOME/.config

        echo ""

        echo "Installing Dunst..."
        sudo pacman -S dunst
        echo "Creating Symlink..."
        cp /etc/dunst/dunstrc $HOME/.config/dunst/dunstrc
        echo "Copying dunst configuration..."
        cp -r $PWD/.config/dunst $HOME/.config

        echo ""

        echo "Installing Scrot..."
        sudo pacman -S scrot
        echo "Copying scrot configuration..."
        [ ! -d "$HOME/.config/scrot" ] && mkdir -p $HOME/.config/scrot
        cp -r $PWD/.config/scrot $HOME/.config

        echo ""

        echo "##################################################################################"
        echo "Take note! To activate the keybinding of sreenshot (scrot),"
        echo "you will need to change permission of that script to be executable,"
        echo "go to scrot directory so we can locate our script to change the permission,"
        echo "to change that use this command: 'chmod +x (name of script which is 'screenshot')'"
        echo "##################################################################################"

        echo ""

        echo "Installing Spotify..."
        yay -S spotify
        echo "Installing Spicetify..."
        yay -S spicetify-cli
        echo "Applying permission to spotify..."
        sudo chmod a+wr /opt/spotify
        sudo chmod a+wr /opt/spotify/Apps -R
        echo "Cloning spicetify themes..."
        git clone https://github.com/spicetify/spicetify-themes.git
        echo "Copying spicetify configuration..."
        cd spicetify-themes
        cp -r * $HOME/.config/spicetify/Themes
        echo "Applying dribbblish themes..."
        cd "$(dirname "$(spicetify -c)")/Themes/Dribbblish"
        mkdir -p ../../Extensions
        cp dribbblish.js ../../Extensions/.
        spicetify config extensions dribbblish.js
        spicetify config current_theme Dribbblish color_scheme base
        spicetify config inject_css 1 replace_colors 1 overwrite_assets 1
        spicetify apply

        echo ""

        echo "Now for setting up our theme, just go this this tutorial:"
        echo "https://github.com/igmt-official/dotfiles#gtk-theming"

        echo ""

        echo "All done."
    fi
fi
