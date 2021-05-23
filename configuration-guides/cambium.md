# **Cambium Instructions**
---
This page explains the configuration of Cambium Networks access points for external Captive  Portal and RADIUS server authentication.

1. In your controller UI, create a new wlan or edit an existing one.
2. Navigate to **AAA servers** provide the necessary information from your ironwifi console. First host is the primary radius server and second host is the backup radius server. This information (IP, port and secret) can be found under networks in the IronWifi console.  Accounting server is optional, however, if you want to see accounting data in the reports then you will need to provide this as well. Further information such as the accounting port can be found by clicking on your network name in the IronWifi console.
![](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cambium/cambium1.png)

3. Navigate to Guest Access and provide the splash page URL from your captive portal settings in the IronWifi console to the “External Page URL” input field. Additionally, make sure you have chosen the _RADIUS_ Access Policy as highlighted in the picture.

![](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cambium/cambium2.jpg)
