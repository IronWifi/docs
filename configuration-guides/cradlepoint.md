# **Cradlepoint**

---

This page explains the Captive Portal configuration for Cradlepoint and authentication with IronWifi.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cradlepoint**

### Access Point Configuration

Please log in to your Cradlepoint Router

At the top, click on Network Settings and choose WiFi / Local Networks

At the bottom of the page, select which Wireless Profile you wish to use and click Edit.

Configure with:

- **WiFi Name (SSID) -** Guest WiFi (or whatever you wish)
- **Hidden -** Unticked
- **Isolate -** Ticked
- **WMM -** Ticked
- **Enabled -** Ticked
- **Security Mode -** Open

Click **Submit** to save

Next, on the same page, above the Wireless Profiles, tick the box beside the Guest LAN network and click **Edit**.

Configure with:

IPv4 Settings tab:

- **IPv4 Routing Mode -** Hotspot

IPv6 Settings tab:

- **IPv6 Address Source -** None

Interfaces tab:

- **WiFi -** Guest WiFi: Click the + to move it to the Selected list

IPv4 DHCP tab:

- **DHCP Server -** Ticked

Click **Submit** to save

Next, click on **System Settings** at the top and choose **Hotspot Services**. Configure with:

Under **Hotspot** Settings:

- **Hotspot Mode -** RADIUS/UAM
- **Local IP Network -** Guest LAN
- **Allow Service on 3G/4G modems -** Ticked
- **Redirect HTTPS Requests -** Unticked
- **Hotspot/UAM Auhentication Port -** 8000

Under **RADIUS** Settings:

- **Server Address 1 -** {{primary_ip}}
- **Server Address 2 -** {{backup_ip}}
- **Authentication Port -** {{auth_port}}
- **Accounting Port -** {{acct_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** as above
- **Redirect Successful Authenticate -** Select To an administrator-defined URL and enter:\
    {{success_page_url}}
- **Session Timeout -** 240 Mins
- **Idle Timeout -** 30 Mins

Under **UAM** Settings:

- **Login URL -** {{splash_page_url}}
- **Splash Page URL -** leave empty
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}

Next, under Allowed Hosts/Domains Prior to Authentication click the Add button and add - **107.178.250.42**

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
 
Follow this instructions to enable SSL on your Access Points - https://customer.cradlepoint.com/s/article/Enabling-Secure-Captive-Portal-UAM-Transactions
