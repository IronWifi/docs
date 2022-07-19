# **Everest Networks**

---

This page explains the configuration of Everest Networks wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Everest Networks**

### Access Point Configuration

Open a web browser and log in to your Everest Cloud (BaseCamp).

## Step 1 - Wireless Network

Click **Wireless Networks** on the left menu, the **Add** at the top right. Configure with:

- **Network Name -** Guest Wifi
- **SSID -** Guest Wifi (or whatever you wish)
- **Security -** Open
- **Captive Portal Enabled -** Yes
- **Enter Splash URL -** {{splash_page_url}}
- **Session Timeout -** 86400
- **Select Third Party Integratior -** IronWifi

Under Primary RADIUS Authentication Server

- **IP Address -** {{primary_ip}}
- **Port -** {{auth_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** as above

Under Primary RADIUS Accounting Server

- **IP Address -** {{primary_ip}}
- **Port -** {{acct_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** as above

Under Secondary RADIUS Authentication Server

- **IP Address -** {{backup_ip}}
- **Port -** {{auth_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** as above

Under Secondary RADIUS Accounting Server

- ** IP Address -** {{backup_ip}}
- **Port -** {{acct_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** {{shared_secret}}

Click **Save** at the top right.

## Step 2 - Walled Garden

Click **Walled Garden** at the top and configure with:

- **Domain -** Splash Page Domain

Finally, click in to the Wireless Network (Guest WiFi) you just created, select the AP's you wish to use this configration and then click Apply to APs at the top.

The configuration is now complete.
