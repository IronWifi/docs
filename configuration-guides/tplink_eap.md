# TP-Link EAP

This page explains the configuration of TP-Link wireless access points in standalone mode or managed by the EAP controller. We will configure the device to use an external Captive  Portal and RADIUS server authentication.

Before configuring the Captive Portal, please update your access points to the latest firmware and use the newest version of the TP-Link Controller software.

Sign-in to the EAP controller or directly to the AP settings. In **Wireless Settings** click on the **Edit** button next to the SSID you wish to use for Captive Portal - _tplink eap cp_ in our example.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink1.png)

Change **Security Mode** to _None_ and enable **Portal**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink2.png)

Click on **Wireless Control -> Portal** and change Authentication Type to _External Radius Server_ and add server details. Change **External Web Portal URL** to the _Splash page URL_ from the IronWifi Console

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink3.png)

Click on **Free Authentication Policy** and enter IronWifi load-balancer IP address which is 107.178.250.42/32

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink4.png)

