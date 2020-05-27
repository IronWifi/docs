# **Netgear**

---

This page explains configuration of Captive Portal with authentication through IronWifi for _netgear_ Access Points. 

### IronWifi Console Configuration
---
1. Create a free _14-day demo account_ [here](https://console.ironwifi.com/register)
2. Once you log in to the console, create a **new network**
3. After that, create a **new captive portal**

### Access Point Configuration
---
1. Enable **External Captive Portal**
2. Provide your **splash page URL** (can be found in the captive portal settings in the IronWifi console)
3. Set authentication type to **Radius**
4. Provide your radius server's details (can be found under networks in the IronWifi console)
5. Add all necessary IP addresses and domains to the **walled garden list** (this depends on your authentication provider)

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/netgear/netgear.png)
