# **Grandstream**

This page explains the configuration of Grandstream access points for external Captive  Portal and RADIUS authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Grandstream**

### Access Point Configuration

Log in to your Grandstream Cloud account at https://www.gwn.cloud

### Step 1 - Captive Portal Policy

Click **Captive Portal > Policy List** on the left menu. Click **Add** then configure with the below settings:

- **Name -** test-portal
- **Splash Page -** External
- **Platform -** Universal Platform
- **External Splash Server Address -** {{splash_page_url}}
- **RADIUS Server Address -** {{primary_ip}}
- **RADIUS Server Port -** {{auth_port}}
- **RADIUS Server Secret -** {{shared_secret}}
- **Secondary RADIUS Server -** disabled
- **Radius Accounting Server Address -** {{primary_ip}}
- **Radius Accounting Server Port -** {{acct_port}}
- **Radius Accounting Server Secret -** {{shared_secret}}
- **Accounting Update Interval (sec) -** empty
- **Enable HTTPS Redirection** - disabled
- **Enable Secure Portal** - enabled
- **Pre Authentication Rule(s)** - Hostname - {{splash_page_hostname}}

Click **Save** to continue.

### Step 2 - SSID

Next, click SSIDs > Add and configure with the below settings:

- **SSID -** testing-ssid
- **Enabled -** enabled
- **Client IP Assignment -** Bridge
- **VLAN -** disabled
- **SSID Band -** Dual-Band
- **Security Mode -** Open
- **Enable Captive Portal -** enabled
- **Captive Portal Policy -** test-portal
- **MAC Filter -** Disabled

Click **Save** to continue.

The configuration is now complete.





