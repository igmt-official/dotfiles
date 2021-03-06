return require("packer").startup(function()
    -- Plugin Manager
    use'wbthomason/packer.nvim'

    -- Colorschemes
    use 'Mofiqul/dracula.nvim'
    use 'tomasiser/vim-code-dark'
    use 'RRethy/nvim-base16'

    -- Nvim Tree
    use 'kyazdani42/nvim-tree.lua'
    use 'kyazdani42/nvim-web-devicons'

    -- Treesitter
    use({ "nvim-treesitter/nvim-treesitter", run = ":TSUpdate" })

    -- Telescope
    use {
        'nvim-telescope/telescope.nvim',
        requires = { {'nvim-lua/plenary.nvim'} }
      }

    -- Color Preview
    use 'norcalli/nvim-colorizer.lua'

    -- Lsp
    use 'neovim/nvim-lspconfig'
    use 'hrsh7th/nvim-cmp' -- Autocompletion plugin
    use 'hrsh7th/cmp-nvim-lsp' -- LSP source for nvim-cmp
    use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip' -- Snippets plugin
    use 'onsails/lspkind-nvim'
    use 'jose-elias-alvarez/null-ls.nvim' -- Format on save

    use 'rcarriga/nvim-notify'
    use 'nvim-lualine/lualine.nvim'
    use 'romgrk/barbar.nvim'

end)

