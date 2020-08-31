#!/bin/bash

output=$(python /home/charles/Documents/AutoProject/mkp.py $1)
echo $output

if [[ "$output" == "Génération..." ]]; then 

    cd ~/Coding/Projets/$1

    echo "# $1" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M master
    git remote add origin https://github.com/charlesthms/$1.git
    git push -u origin master

    code .
fi
