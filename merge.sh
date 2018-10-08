#!/bin/bash

rm merge_list.txt
find $1 -name "*.flv" -print0 |xargs -0 -n 1 -P 1 -I {} sh -c 'echo file "$1" >> merge_list.txt ' sh {}
cat merge_list.txt | sort -o merge_list.txt
ffmpeg -f concat -safe 0 -i merge_list.txt -c copy "$2.flv"
rm merge_list.txt
find $1 -name "*.xml" -print0 |xargs -0 -n 1 -P 1 -I {} sh -c 'danmaku2ass -s 1920x1080 -ds 10 -dm 10 -fs 70 "$1" -o "$2.ass" ' sh {} "$2"

