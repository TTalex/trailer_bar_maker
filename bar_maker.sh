#! /bin/bash
if [[ $# -eq 1 ]]; then
#    wget $1 -O src.mov
    youtube-dl $1 -o src.mp4
#    fg
    if [[ $? -eq 0 ]]; then
        python bar_maker.py
        name=$(youtube-dl --get-filename -o '%(title)s' $1)
        mv res.png "$name.png"
        eog "$name.png" &
    fi
    rm src.mp4
fi

