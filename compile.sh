#!/bin/bash

if [ -z "$(ls $HOME/C-Team)" ] 
then
    echo "NAS not accessable! No files were written!"
    exit
fi

LATEST_TAG=$(git describe --tags --abbrev=0)
TANZ="${HOME}/C-Team/Bilder/OneChance/${LATEST_TAG:1}_Trainersicht_OneChance.pdf"
TRAIN="${HOME}/C-Team/Bilder/OneChance/${LATEST_TAG:1}_Tanzsicht_OneChance.pdf"
rm $HOME/C-Team/Bilder/OneChance/*.pdf
coco OneChance.choreo $TANZ
coco OneChance.choreo $TRAIN --topUp
./bookmark.py $TANZ "OneChance.choreo"
./bookmark.py $TRAIN "OneChance.choreo"

