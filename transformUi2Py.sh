#!/bin/bash

filename=$1
pyuic5 -o $filename.py $filename.ui

mv $filename.py $filename'_UI.py'
