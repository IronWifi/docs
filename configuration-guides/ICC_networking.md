# **ICC Networking**

---

This page explains configuration of ICC Access Points to work with IronWifi Captive Portal.

**IronWifi Console configuration**

1. Log in to the IronWifi Console
2. From the menu, go to **Network -> Captive Portals -> New Captive Portal**
3. Fill in Name, select **Network**, select **_ICC_** as **Vendor** and add at least one Authentication Provider

**ICC Access Point configuration**

1. Log in to the ICC AP Web-Browser interface and go to Services -> Captive Portal

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ICC_Networking/ICC.png)

2. Go to **Network -> Wi-Fi** and click the **Edit** button

![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ICC_Networking/ICC2.png)

3. In the **Interface Configuration** section, click on the **Captive Portal** and fill in required information:

**IP address of the interface and Netmask**: for example 10.0.1.1 and 255.255.255.0

**Server Address**: 107.178.250.42

**Splash Page**: Splash page URL from IronWifi Console

**Splash Page Secret Required**: checked

**Splash Page Secret**: RADIUS secret from IronWifi Console

![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ICC_Networking/ICC3.png)
