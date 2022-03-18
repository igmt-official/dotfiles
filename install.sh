echo "#################################################"
echo "Welcome to Igmt-Official Dotfiles"
echo "Written by https://www.reddit.com/u/igmt-official"
echo "#################################################"

echo ""

echo "Note: Please follow the instruction carefully, to avoid cancelling this installation!"
echo "Do you want to procceed the installation? Type 'Y': " read yN0

echo ""

if [ $yN0 == "Y" ]; then
    echo "Cloning Igmt-Official Dotfiles..."
    git clone https://github.com/igmt-official/dotfiles.git

    echo ""

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
    # [ ! -d "$HOME/.config/qtile" ] && mkdir -p $HOME/.config/qtile/
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

    echo "If you already done type 'Y' to continue our configuration: " read yN1

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

    echo "###############################################################################################################################################"
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
    echo "And for our Treesitter install what you want language, to install use this command: 'TSInstall (language)'"
    echo "Then edit treesitter config to add your language '.config/nvim/lua/treesitter-config/init.lua', and uncomment all '--' sign."
    echo "###############################################################################################################################################"

    echo ""

    echo "Make sure you followed already all steps to activate our all plugins."
    echo "To avoid error in our Neovim."

    echo ""

    echo "If you done, type 'Y': " read yN2

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
    
fi