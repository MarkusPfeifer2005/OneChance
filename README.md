# Setup

This project uses *ChoreoMaster* which is unfortunately only available on
Windows.  It is hoever installable via wine, with some caveats. In the
following I will provide a simple instruction. Alternatively I am developing
my own implementation which can be found [here](https://github.com/MarkusPfeifer2005/ChoreoCompiler). It is developed for Linux.

> [!IMPORTANT]
> There are some fonts that do not work in wine, so the letters on the dots as
> well as the coordinates on the border of the grid are displayed really large.
> This makes working with this setup rather painful. I only recommend it if you
> cannot get your hands on a Windows machine.

Download the .msi from [the official site](http://www.jahn-dc.de/choreomaster).

ChoreoMaster requires .NET, so let's install it.
```shell
WINEPREFIX=~/.wine-choreomaster WINEARCH=win64 wineboot
WINEPREFIX=~/.wine-choreomaster winetricks -q dotnet48
```
Then run the installer.
```shell
WINEPREFIX=~/.wine-choreomaster wine msiexec /i ~/Downloads/ChoreoMaster.msi
```
The .exe ist found at `.wine-choreomaster/drive_c/Program Files (x86)/ChoreoMaster/ChoreoMaster.exe`.
