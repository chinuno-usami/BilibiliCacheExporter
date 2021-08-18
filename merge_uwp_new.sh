#!/bin/bash

ffmpeg -i $1/video.m4s -i $1/audio.m4s -c copy "$2.mp4"
find $1 -name "*.xml" -print0 |xargs -0 -n 1 -P 1 -I {} sh -c 'danmaku2ass -s 1920x1080 -ds 10 -dm 10 -fs 70 "$1" -o "$2.ass" ' sh {} "$2"

