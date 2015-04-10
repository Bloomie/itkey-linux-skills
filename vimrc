syntax on

set number

set autoindent
set expandtab
set smarttab

set wildmenu
set wildmode=list:longest,full

set ignorecase
set smartcase

set hlsearch

colorscheme gruvbox
set background=dark

execute pathogen#infect()

" set default comment color to cyan instead of darkblue
" which is not very legible on a black background
highlight comment ctermfg=cyan

set tabstop=2
set expandtab
set softtabstop=2
set shiftwidth=2

" Set up puppet manifest and spec options
au BufRead,BufNewFile *.pp
\ set filetype=puppet
au BufRead,BufNewFile *_spec.rb
\ nmap <F8> :!rspec —color %<CR>

" Enable indentation matching for =>'s
filetype plugin indent on
