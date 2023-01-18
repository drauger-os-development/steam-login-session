steam-login-session
===========

Put STEAM BigPicture mode at login screen

NEWS
----
* *Version 14 - Add Steam Deck-based BPM

* *Version 13 - Translated from BASH to Python for better performance and fix some bugs

* *Version 12 - Forked from original dev due to lack of updates* <br/>
steam-login-session is a fork of steam-session. To view the original source code,
go to https://github.com/thor27/steam-login

* *Version 11 - Test version with Steam manager* <br/>
This  verison add a special manager for Steam that prevents focus loss.
To get this version change to branch steam-manager


KNOWN ISSUES
------------

Steam, sometimes, may "hide" itself, mostly when something went wrong with a game or Steam itself. If this happens just press ALT+TAB to get back do Steam Big Picture. (**this will likely not happens in version 10**)

INSTALL
-------
Drauger OS users can simply install from `apt`:
```
sudo apt install steam-login-session
```
For other users, on Debian-based systems:
```
git clone https://github.com/drauger-os-development/steam-login-session
cd steam-login-session
./build.sh
sudo apt install ../steam-login-session_*.deb
```
There is no support for RPM packages at this time, but we are open to adding that support.
