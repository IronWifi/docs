# Keenetic

This page explains the configuration of [Keenetic Access Points](https://keenetic.com) to work with IronWifi Captive Portal.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Keenetic**
4. Scroll down to the **Controller Configuration** and copy the **Shared Secret** and **NAS ID**.

### Access Point Configuration

1. Log in to the Keenetic AP Web-Browser interface and go to **Guest Network -> Captive Portal** settings. Update the profile settings and configure with:

- **UAM Server -** {{splash_page_url}}
- **UAM Secret -** {{shared_secret}} 
- **RADIUS server 1 -** {{primary_ip}}
- **RADIUS Secret -** {{shared_secret}}
- **RADIUS NAS ID -** {{nas_id}}

![firstScreen](keenetik/keenetic1.png)

![firstScreen](keenetik/keenetic2.png)
