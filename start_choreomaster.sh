#!/bin/bash
export FREETYPE_PROPERTIES="truetype:interpreter-version=35"
export WINEPREFIX="$HOME/.wine-choreomaster"
wineserver -w
exec wine "$WINEPREFIX/drive_c/Program Files (x86)/ChoreoMaster/ChoreoMaster.exe"
