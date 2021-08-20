# **TP Link Omada (version 4)**

---

This page explains the configuration of TP Link access points with Omada version 4 controller for external Captive Portal and RADIUS authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **TP Link Omada v4**

### Access Point Configuration

1. Configure the Captive Portal under **Authentication -> Portal**. Use the following values:

- **Authentication Type -** External RADIUS Server
- **Authentication Timeout -** 8 hours
- **NAS ID -** TP-Link
- **Authentication Mode -** CHAP
- **Portal Customization -** External Web Portal - {{splash_page_url}}
- **Landing Page -** The Original URL

3. Define a RADIUS profile by clicking on **manage RADIUS Profile**. Configure with:

- **Name -** ironwifi_radius (or whatever you wish)
- **VLAN Assignment -** Disabled
- **Authentication Server IP -** {{primary_ip}}
- **Authentication Port -** {{auth_port}}
- **Authentication Password -** {{shared_secret}}
- **Radius Accounting -** Enabled
- **Accounting Port -** {{acct_port}}

4. Import your **SSL certificate** under **Controller** 

5. Add an **A type DNS record** to point the hostname to your omada controller.


![tplink2](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink1.png)

![tplink3](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink3.png)

![tplink4](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink2.png)

![tplink5](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/tp_link_omada_v4/tplink5.png)


