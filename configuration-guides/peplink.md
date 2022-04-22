# **Peplink**

---

This page explains the necessary configuration for Peplink Access Points and external Captive Portal with RADIUS authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Peplink**

### Access Point Configuration

1. Sign in to the InControl control panel, find the **Access Point -> Settings -> Remote Web Admin**
2. In the Access Point settings page, click on **Network -> Captive Portal**, and configure with:

- **Hostname -** captive-portal.peplink.com
- **Access Mode -** User Authentication
- **Authentication -** RADIUS Server
- **Auth Server -** {{primary_ip}}
- **Port -** {{auth_port}}
- **Auth Server Secret -** {{shared_secret}}
- **CoA-DM -** Disabled
- **Accounting Server -** {{primary_ip}}
- **Port -** {{acct_port}}
- **Accounting Server Secret -** {{shared_secret}}
- **Accounting Interim Interval -** 300 seconds
- **Splash Page -** External, URL: {{splash_page_url}}
 
The configuration is now complete. 

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

---

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/peplink/peplink1.png)

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/peplink/peplink2.png)

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/peplink/peplink3.png)
