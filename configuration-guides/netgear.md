# **Netgear**

---

This page explains configuration of Captive Portal with authentication through IronWifi for _netgear_ Access Points. 

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Netgear**

### Access Point Configuration

1. Navigate to **Management -> WLAN settings -> your SSID**
2. Under **Advanced**, enable **Captive Portal** and configure with:

- **External Captive Portal -** Enabled
- **Splash Page URL -** {{splash_page_url}}
- **Captive Portal Authentication Type -** Radius

_Primary Authentication Server_

- **IPv4 Address -** {{primary_ip}}
- **Port -** {{auth_port}}
- **Password -** {{shared_secret}}

_Secondary Authentication Server_

- **IPv4 Address -** {{backup_ip}}
- **Port -** {{auth_port}}
- **Password -** {{shared_secret}}

_Primary Accounting Server_

- **IPv4 Address -** {{primary_ip}}
- **Port -** {{acct_port}}
- **Password -** {{shared_secret}}

_Secondary Accounting Server_

- **IPv4 Address -** {{backup_ip}}
- **Port -** {{acct_port}}
- **Password -** {{shared_secret}}

5. Add **splash.ironwifi.com** to the walled garden list

The configuration is now complete.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

---

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/netgear/netgear.png)
