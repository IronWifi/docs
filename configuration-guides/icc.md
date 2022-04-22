# **ICC Networking**

---

This page explains configuration of ICC Access Points to work with IronWifi Captive Portal.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **ICC**

### ICC Access Point configuration

1. Log in to the ICC AP Web-Browser interface and go to Services -> Captive Portal. Configure with:

- **RADIUS 1 -** {{primary_ip}}
- **RADIUS 2 -** {{backup_ip}}
- **RADIUS Secret -** {{shared_secret}}
- **Radius Authorization Port -** {{auth_port}}
- **Radius Accounting Port -** {{acct_port}}

2. Go to **Network -> Wi-Fi** and click the **Edit** button.

3. In the **Interface Configuration** section, click on the **Captive Portal** and fill in required information:

- **IP address of the interface and Netmask -** for example 10.0.1.1 and 255.255.255.0
- **Server Address -** 107.178.250.42
- **Splash Page -** {{splash_page_url}}
- **Splash Page Secret Required -** checked
- **Splash Page Secret -** {{shared_secret}}

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ICC_Networking/ICC.png)

![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ICC_Networking/ICC2.png)

![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ICC_Networking/ICC3.png)


