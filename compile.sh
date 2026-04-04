#!/bin/bash

if [ -z "$(ls $HOME/C-Team)" ] 
then
    echo "NAS not accessable! No files were written!"
    exit
fi

LATEST_TAG=$(git describe --tags --abbrev=0)
coco OneChance.choreo "${HOME}/C-Team/Bilder/OneChance/${LATEST_TAG:1}_Trainersicht_OneChance.pdf"
coco OneChance.choreo "${HOME}/C-Team/Bilder/OneChance/${LATEST_TAG:1}_Tanzsicht_OneChance.pdf" --topUp

