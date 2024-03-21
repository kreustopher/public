# ve, vs, vv, 
function ve
    /usr/bin/nvim --server /tmp/$NVIMVGUID --remote-send "<C-\\><C-n>:FTermClose<CR>:e $(readlink -f $argv[1])<CR>"
end

