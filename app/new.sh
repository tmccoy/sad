#!/bin/bash
for i in $(find . -type d -mindepth 1); do
mkdir $i/assets
mkdir $i/html
echo "folders made in " $i
done
