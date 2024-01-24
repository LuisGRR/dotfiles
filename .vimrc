set number
set numberwidth=1
set mouse=a
set clipboard=unnamed
set showcmd
set ruler
set cursorline
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
"syntax enable
set laststatus=2
set noshowmode
syntax on
set autoindent


"Plug
source ~/.config/vimcon/conf-Plug/plug-conf.vim

"atajos de teclado 
let mapleader=" "

nmap<Leader>s <Plug>(easymotion-s2)
nmap<Leader>nt :NERDTreeFind<CR>

nmap<Leader>w :w<CR>
nmap<Leader>q :q<CR>
nmap<Leader>wq :wq<CR>

"Experiment
"nmap<Leader><Leader>c console.log({});<Esc>==f{a

"navigation buffer
map <C-d> :bnext<CR>
map <C-a> :bprev<CR>
imap <C-D> :bnext<CR>a
imap <C-A> :bprev<CR>a

"undotree atajos de teclado 
nmap <Leader>tu :UndotreeToggle<CR>
nmap <Leader>hu :UndotreeHide<CR>
nmap <Leader>su :UndotreeShow<CR>

" atajos Fzf
nmap <Leader>fs :File<CR>

"atajos coc
nmap <Leader>gs :CocSearch<CR>
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

"powerlinie
source ~/.config/vimcon/plug-conf/airline.vim

"themas 
"colorscheme gruvbox
"set background=dark
"let g:gruvbox_contrast_dark = "hard"

let NERDTreeQuitOnOpen =1
"THEMA material

"source ~/.config/vimcon/themas/onedark.vim
source ~/.config/vimcon/themas/afterglow.vim


"vim rainbow
let g:rainbow_active=1

"vim gitgutter
set updatetime=100

source ~/.config/vimcon/plug-conf/coc.vim

source ~/.config/vimcon/plug-conf/indentLine.vim

source ~/.config/vimcon/plug-conf/prettier.vim

source ~/.config/vimcon/plug-conf/vim-syntastic.vim

let g:script_runner_python = 'python3 '

"source ~/.config/vimcon/plug-conf/rnvimr.vim
