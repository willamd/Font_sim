#!/bin/bash
filename=$1
comment=$2
git add $filename
git commit -a -m $comment
git push -u Font_sim master
