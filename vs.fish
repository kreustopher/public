# ve, vs, vv, 
function vs
    /usr/bin/nvim --server /tmp/$NVIMVGUID --remote-send "<C-\\><C-n>:Sp<CR>:e $(readlink -f $argv)<CR>"
end



