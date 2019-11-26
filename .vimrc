set tabstop=4
set shiftwidth=4
set expandtab
set nu
nnoremap <F2> :set nonumber!<CR>
set hlsearch
syntax on

" Show trailing white space in red$
:highlight ExtraWhitespace ctermbg=red guibg=red$
:match ExtraWhitespace /\s\+$/$
