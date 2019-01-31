steam-login-session
===========

Put STEAM BigPicture mode at login screen

NEWS
----

* *Version 12 - Forked from original dev due to lack of updates* <br/>
steam-login-session is a fork of steam-session. To view the original source code,
go to https://github.com/thor27/steam-login

* *Version 11 - Test version with Steam manager* <br/>
This  verison add a special manager for Steam that prevents focus loss.
To get this version change to branch steam-manager


KNOWN ISSUES
------------

Steam, sometimes, may "hide" itself, mostly when something went wrong with a game or staem itself. If this happens just press ALT+TAB to get back do Steam Big Picture. (**this will likely not happens in version 10**)

INSTALL
-------
You can download deb packges from here from the original dev:  <a href="https://drive.google.com/drive/folders/0B0E1Hoh3ktodYnk4NF9VY1dnblE?usp=sharing">Steam Login</a> 

Or from the releases page from the current dev.

**The PPA is really outdated**, and the original dev is not maitaining it anymore. If there are any changes they will be made here. Also, Drauger OS users will get updates over `apt`.

```
sudo add-apt-repository ppa:thor27-gmail/steam-desktop
sudo apt-get update
sudo apt-get install steam-login
```
