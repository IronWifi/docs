# Cisco Meraki

This page explains the configuration of Cisco Meraki wireless access points for external Captive  Portal and RADIUS server authentication.

Sign-in to the Meraki cloud portal.

![firstScreenshot](https://github.com/IronWifi/docs/edit/master/configuration-guides/meraki/meraki1.png)

Navigate to **Wireless -> Configure -> SSIDs** and define a network that we will protect with a Captive Portal with RADIUS authentication - Students in this example.

![secondScreenshot](https://github.com/IronWifi/docs/edit/master/configuration-guides/meraki/meraki2.png)

**Association requirements**: Open (no encryption)

**Splash page**: Sign-on with my RADIUS server

**RADIUS for splash page**: add both servers from the IronWifi console, IP address, Port number and Secret

**Walled garden ranges**: add all Walled garden IP addresses from the IronWifi console

![thirdScreenshot](https://github.com/IronWifi/docs/edit/master/configuration-guides/meraki/meraki3.png)

Navigate to **Wireless -> Configure -> Splash page** and add **Custom splash URL** from the IronWifi console 

![fourthScreenshot](https://github.com/IronWifi/docs/edit/master/configuration-guides/meraki/meraki4.png)

