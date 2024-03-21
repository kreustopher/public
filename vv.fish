# ve, vs, vv, 
function vv
    /usr/bin/nvim --server /tmp/$NVIMVGUID --remote-send "<C-\\><C-n>:Vs<CR>:e $(readlink -f $argv[1])<CR>"
end

