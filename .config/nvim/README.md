![2022-03-21-19:32:57-screenshot](https://user-images.githubusercontent.com/96023410/159258190-a5b90b65-8281-4253-9748-11151f8176a2.png)

Install **[Neovim](https://github.com/neovim/neovim/wiki/Installing-Neovim)**:

```bash
sudo pacman -S neovim
```

Now we can setup our **Neovim** to be our **IDE**, I will not guide you step by step, because it will take a long series.
If you want to make your own setup, search in **[Youtube](https://youtube.com)**, this steps is guide to activate my **Neovim Setup**.

If you not downloaded yet my repository:

```bash
git clone https://github.com/igmt-official/dotfiles.git
```

Copy my configs:

```bash
cp -r dotfiles/.config/nvim ~/.config
```

# Neovim Features

| Neovim Features                                                                     | Utility                  |
| ----------------------------------------------------------------------------------- | ------------------------ |
| **[Plugins Packer](https://github.com/wbthomason/packer.nvim)**                     | Plugins Installer        |
| **[Nvim Tree](https://github.com/kyazdani42/nvim-tree.lua)**                        | File Explorer            |
| **[Colorscheme](https://github.com/Mofiqul/dracula.nvim)**                          | Theme                    |
| **[Lsp Config](https://github.com/neovim/nvim-lspconfig)**                          | Initializing Language    |
| **[Cmp](https://github.com/neovim/nvim-lspconfig/wiki/Autocompletion)**             | Auto Complete Code       |
| **[Lsp Kind](https://github.com/onsails/lspkind-nvim)**                             | Vscode-like Pictograms   |
| **[Nvim Notify](https://github.com/rcarriga/nvim-notify)**                          | Fancy Notification       |
| **[Lualine](https://github.com/nvim-lualine/lualine.nvim)**                         | Statusline               |
| **[Barbar](https://github.com/romgrk/barbar.nvim)**                                 | Tabline                  |
| **[Treesitter](https://tree-sitter.github.io/tree-sitter/)**                        | Syntax Highlight         |
| **[Telescope](https://github.com/nvim-telescope/telescope.nvim#pickers)**           | Finder                   |
| **[Null-ls](https://github.com/jose-elias-alvarez/null-ls.nvim)**                   | Format on Save           |

## Plugins

Install **Plugin Manager**:

```bash
# This is for setting up our Plugins Packer
git clone --depth 1 https://github.com/wbthomason/packer.nvim\
 ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

Next edit ```.config/nvim/lua/packer-config/init.lua``` in **Neovim** install packer plugin using this command:

```vim
:PackerSync
```

Now try to uncommenting all plugins that have ```--``` sign and try to install all plugins using this command:

```vim
:PackerSync
```

After that edit ```.config/nvim/init.lua``` and uncommenting all ```--``` sign, then save it and reload the **Lua Config** using this command:

```vim
:luafile %
```

## Lsp

For my **Lsp Config**, I install **[Python Language Server](https://github.com/microsoft/pyright)**, because I'm **Python Developer**.

Installing **[Python Language Server](https://github.com/microsoft/pyright)**:

```bash
sudo npm i -g pyright
```

And also install **[Eslint Language Server](https://github.com/hrsh7th/vscode-langservers-extracted)** for **JavaScript and TyperScript**:

```bash
sudo npm i -g vscode-langservers-extracted
```

You can install what you want language to install your langauge server,
go to this site **[Language Servers](https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md)**.

## Treesitter

For my **Treesitter Config**, I install **Python** and **Lua** to enable their syntax, to install just type this command inside **Neovim**:

```vim
:TSInstall python
:TSInstall lua
:TSInstall javascript
:TSInstall html
:TSInstall css
:TSInstall json
```

Now that we already installed our languages, edit ```.config/nvim/lua/treesitter-config/init.lua``` and uncommenting all ```--```.

## Telescope

Installing Ripgrep and Fd:

```bash
sudo pacman -S ripgrep fd
```

## Null-ls

Installing Eslint and Autopep8:

```bash
sudo npm install -g eslint
```

## KeyMap

| Key                            | Action                           |
| -------------------------------| -------------------------------- |
| **leader + t**                 | File Explorer                    |
| **leader + ff**                | Find Files                       |
| **leader + fg**                | Live Grep                        |
| **leader + rn**                | Rename                           |
| **a**                          | Create file inside File Explorer |
| **alt + 1 - 9, 0**             | Next tab                         |
| **leader + lf**                | Auto Format Code                 |
| **:vsplit**                    | Vertical Split Pane              |
