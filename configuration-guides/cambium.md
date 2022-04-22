# **Cambium Networks**

---

This page explains the configuration of Cambium Networks access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cambium Networks**

### Access Point Configuration

1. In your controller UI, create a **new wlan** or edit an existing one.
2. Navigate to **AAA servers** and configure with:

_Authentication Server_

- **1. Host -** {{primary_ip}}
- **Secret -** {{shared_secret}}
- **Port -** {{auth_port}}
- **2. Host -** {{backup_ip}}
- **Secret -** {{shared_secret}}
- **Port -** {{auth_port}}

_Accounting Server_

- **1. Host -** {{primary_ip}}
- **Secret -** {{shared_secret}}
- **Port -** {{acct_port}}

3. Navigate to **Guest Access** and configure with the following values:

- **Access Policy -** RADIUS
- **External Page URL -** {{splash_page_url}}

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

![](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cambium/cambium1.png)
![](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cambium/cambium2.jpg)
