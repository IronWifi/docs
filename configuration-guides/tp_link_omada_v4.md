# **TP Link Omada (version 4)**

---

This page explains the configuration of TP Link access points with Omada version 4 controller for external Captive Portal and RADIUS authentication.

### IronWifi Console Configuration

1. Create a free _14-day demo account_ [here](https://console.ironwifi.com/register)
2. Once you log in to the console, create a **new network**
3. After that, create a **new captive portal**

### Access Point Configuration

1. Make sure you select TP Link Omada v4 as a vendor in the captive portal settings.

![tplink1](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink4.png)

2. Configure the Captive Portal under **Authentication -> Portal**. This is where information from the ironwifi console will be required (RADIUS IPs, splash page URL)

![tplink2](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink1.png)

3. Define a RADIUS profile using the information from the IronWifi console. Authentication password is the shared secret.

![tplink3](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink3.png)

4. Import your SSL certificate under **Controller** 

![tplink4](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink3.png)

![tplink5](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink5.png)




