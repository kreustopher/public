# nvim --listen /tmp/nvima.pipe
function nvim
    export NVIMVGUID="$(uuidgen).pipe"
    /usr/bin/nvim --listen /tmp/$NVIMVGUID $argv
end


