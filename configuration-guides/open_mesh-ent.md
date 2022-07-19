# **Open-Mesh Cloudtrax**

---

This page explains the configuration of Open-Mesh devices to work with IronWifi Captive Portal.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Open Mesh (Cloudtrax)**

### Access Point Configuration

Open the configuration page of Cloudtrax and navigate as follows. 

1. Navigate to **Configure -> SSID** and under **Captive Portal**, configure with:

- **Splash page -** Enabled
- **Splash page type -** Hosted remotely
- **Splash page URL -** {{splash_page_url}}
- **Splash page secret -** {{shared_secret}}
- **Splash page authentication type -** RADIUS
- **Server address 1 -** {{primary_ip}}
- **Server address 2 -** {{backup_ip}}
- **Server secret -** {{shared_secret}}
- **NAS ID -** 7027
- **Block unauthenticated users -** Enabled
- **Walled garden -** splash.ironwifi.com, 107.178.250.42

The configuration is now complete.

---

![screenOne](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/open_mesh_cloudtrax/OMC.png)
