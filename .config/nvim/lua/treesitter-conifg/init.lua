require("nvim-treesitter.configs").setup({
 	--> parsers <--
 	ensure_installed = {
 		"python",
 		"lua",
         "javascript",
         "css",
         "html",
         "json",
 	},

 	sync_install = false,
 	highlight = {
 		enable = true,
 		additional_vim_regex_highlighting = false,
 	},

     indent = {
 		enable = true,
 	},

     --> refactor module
 	refactor = {
 		smart_rename = {
 			enable = true,
 			keymaps = {
 				smart_rename = "grr",
 			},
 		},
 	},
	
 })
