# **TP-Link EAP**

---

This page explains the configuration of TP-Link wireless access points in standalone mode or managed by the EAP controller. We will configure the device to use an external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **TP-Link EAP**

### Access Point Configuration

**Before configuring the Captive Portal, please update your access points to the latest firmware and use the newest version of the TP-Link Controller software.**

1. Sign-in to the EAP controller or directly to the AP settings. In **Wireless Settings** click on the **Edit** button next to the SSID you wish to use for Captive Portal - _tplink eap cp_ in our example.

2. Under basic info, edit the configuration with:

- **Security Mode -** none
- **Portal -** enabled

Click **Apply**.

3. Click on **Wireless Control -> Portal** and configure with:

- **Authentication Type -** External Radius Server
- **Radius Server IP -** {{primary_ip}}
- **Port -** {{auth_port}}
- **Radius Password -** {{shared_secret}}
- **Redirect -** Enabled
- **Redirect URL -** {{success_page_url}}
- **Portal Customization -** External Web Portal
- **External Web Portal URL -** {{splash_page_url}}

Click **Apply**.


4. Click on **Free Authentication Policy** and enter IronWifi load-balancer IP address which is **107.178.250.42/32**

The configuration is now **complete**.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

---

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink1.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink2.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink3.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tplink_eap/tplink4.png)

