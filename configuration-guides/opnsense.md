# **OPNsense**

---

This page describes the necessary configuration of the OPNsense firewall with RADIUS authentication using the Captive Portal.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **OPNsense**
4. Click on **Auth_page**, rename downloaded file to **index.html** and create a zip archive containing this file

### Access Point Configuration

Log in to the **OPNsense administration** console and navigate to **Systems -> Access -> Servers**. 

1. Click on the **Add button** and configure with:

- **Descriptive name -** radius1 (or whatever you wish)
- **Type -** Radius
- **Hostname or IP address -** {{primary_ip}}
- **Shared Secret -** {{shared_secret}}
- **Services offered -** Authentication and Accounting
- **Authentication port value -** {{auth_port}}
- **Accounting port value -** {{acct_port}}
- **Authentication Timeout -** 3

2. Navigate to **Services -> Captive Portal -> Administration** and switch to the Templates tab. Click the + button, enter a Template name, and upload the zip archive.
3. Switch to the **Zones tab** and click the + button to create a new zone. Configure with:

- **Interfaces -** LAN
- **Authenticate using -** radius1
- **Allowed addresses -** 107.178.250.42

To prevent **SSL warnings**, select a hostname for your firewall, create a valid **SSL certificate**, and upload it to the firewall.

Review your firewall settings to make sure access to the internet is allowed.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
