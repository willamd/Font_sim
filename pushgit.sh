#!/bin/bash
filename=$1
comment=$2
git add $filename
git commit -m $comment
git push -f Font_sim master
