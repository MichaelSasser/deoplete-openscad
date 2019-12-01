"Vim filetype plugin
" Language: OpenSCAD
" Maintainer: Michael Sasser <Michael@MichaelSasser.org>
" Last Change: Dec 1, 2019

" Initialization
if exists('b:did_ftplugin')
  finish
endif
let b:did_ftplugin = 1

let s:cpo_save = &cpoptions
set cpoptions&vim

" Set 'comments' to format dashed lists in comments.
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://

" Set 'formatoptions' to break comment lines but not other lines,
" and insert the comment leader when hitting <CR> or using "o".
setlocal formatoptions-=t fo+=croql

" Syntax completion function
if exists('&ofu')
    setlocal omnifunc=syntaxcomplete#Complete
    setlocal completefunc=syntaxcomplete#Complete
endif

" Main functions
if has('python')
    " Random ID generator
    function! RandomID()

"Python implementation follows; do not alter indentations/whitespace
python << EOF
import random, string, vim
vim.command("let l:id = '" + (''.join(random.sample(string.ascii_uppercase + string.digits, 8))) + "'")
EOF

    return l:id
    endfunction
    "}

    "Unit test template
    function! Test()
        if exists('*strftime')
            let l:date = strftime('%Y%m%d') . '-'
        else
            let l:date = ''
        endif

        let l:testid = expand('%:t') . '-' . l:date . RandomID()
        let l:template = 'Test[\rtest\r,\rresult\r,\rTestID -> \"" . l:testid . "\"\r\b]'
        exe ':normal i' . l:template
    endfunction

endif


" Cleanup
let &cpoptions = s:cpo_save
unlet s:cpo_save
