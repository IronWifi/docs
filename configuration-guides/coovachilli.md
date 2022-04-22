# **CoovaChilli**

---

This page explains the configuration of CoovaChilli installed on an OpenWRT compatible device (TP-Link) to work with IronWifi Captive Portal.

**These steps are only an example. IronWifi is not providing support for configuring CoovaChilli devices. If you are looking for a supported solution, please use access points from one of our supported vendors.**

The first step is the installation of OpenWRT to your wireless access point. A list of compatible Hardware is available on this site. For installation instructions, check this installation manual.

After you install the system, telnet or ssh to your router and enter:

```
opkg update
opkg install wpad (optional, depends on your wireless)
opkg install coova-chilli
opkg install kmod-tun
opkg install tcpdump
reboot
```

You can download the CoovaChilli configuration file from the console. To download this file, please go to the **Console->Networks->CaptivePortals->your captive portal.**

Set vendor to CoovaChilli and download Configuration files - defaults file and chilli init file.
Under authentication providers, add anonymous (for testing).

Copy downloaded defaults file to your wireless router to _/etc/chilli/defaults_ and _/etc/chilli/config_
Copy downloaded chilli init file to _/etc/init.d/chilli_

_chmod +x /etc/init.d/chilli_
_/etc/init.d/chilli start_

At this moment, your OpenWRT router should be displaying our splash page to your new guests.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
