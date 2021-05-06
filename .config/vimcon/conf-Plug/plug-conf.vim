call plug#begin('~/.vim/plugged')

" themes 
Plug 'morhetz/gruvbox'
Plug 'kaicataldo/material.vim'
Plug 'joshdick/onedark.vim'
Plug 'danilo-augusto/vim-afterglow'
" IDE

Plug 'jiangmiao/auto-pairs'

Plug 'prettier/vim-prettier'
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'


Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

Plug 'mbbill/undotree'

Plug 'frazrepo/vim-rainbow'
Plug 'airblade/vim-gitgutter'

Plug 'sheerun/vim-polyglot'

Plug 'ryanoasis/vim-devicons'

Plug 'neoclide/coc.nvim',{'branch':'release'}
 
Plug 'alvan/vim-closetag'

Plug 'junegunn/fzf' ,{'do': {-> fzf#install()}}
Plug 'junegunn/fzf.vim'
Plug 'airblade/vim-rooter'

"Plug 'francoiscabrol/ranger.vim'

call plug#end()

