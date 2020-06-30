#  **Cisco WLC**

---

This page explains the configuration of the Cisco Wireless LAN Controller to work with IronWifi Captive Portal.

**Cisco WLC configuration**

Log in to the Cisco WLC Web-Browser interface and go to Advanced Settings.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc1.png)

Go to **Security -> Access Control Lists** and add **two new ACL rules** permitting connections to the Captive Portal. Get the Captive Portal IP address from your Captive Portal settings -> Walled Garden -> IronWifi

- Source: Any, Destination: 107.178.250.42 netmask 255.255.255.255, protocol TCP, Dest port 443, Action: Permit
- Source 107.178.250.42 netmask 255.255.255.255, Destination: Any, protocol TCP, Source port 443, Action: Permit

![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc2.png)

![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc3.png)

Go to **Security -> Web Auth -> Web Login Page** and change Web Authentication Type to **_External (redirect to an external server)_**. Add the External Webauth URL which is the Splash page URL from your Captive Portal in IronWifi Console

![fourthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc4.png)

Go to **Security -> RADIUS -> Authentication**, add new RADIUS Authentication Servers and enter IP Address, Port and Shared Secret from your Captive Portal in IronWifi Console -> Controller Configuration -> RADIUS for the splash page

![fifthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc5.png)

![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc6.png)

Go to **Security -> RADIUS -> Accounting**, add new RADIUS Accounting Servers and enter IP Address, Port and Shared Secret from your Captive Portal in IronWifi Console -> Controller Configuration -> RADIUS for the splash page

![seventhScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc7.png)

Go to **WLANs**, select existing or create new WLAN and open WLAN settings page

![eighthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc8.png)

![ninthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc9.png)

Click on the Security tab, Layer 2 and set **Layer 2 Security** to **_None_**

![tenthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc10.png)

Click on the Layer 3 tab and set **Layer 3 Security** to **Web Policy**, select the **_Authentication_** radio button and select your new ACL for **Pre-authentication ACL**.

![eleventhScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc11.png)

Click on the **AAA Servers** tab and select IronWifi RADIUS authentication and accounting servers. You can also set an **Interim Interval** to **_180_** seconds or higher.

![twelfthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc12.png)

Click on the **Save Configuration** link to save and apply new settings.

Finally, change the default virtual controller IP address from 1.1.1.1 to some [other IP address](https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wireless-lan-wlan/213535-wlc-virtual-ip-address-1-1-1-1.html) and install a valid SSL certificate on your controller to prevent warning messages displayed to your clients.
