# **Ruckus ZoneDirector**

---

This page explains the Captive Portal configuration for managed ZoneDirector and authentication with IronWifi RADIUS servers.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Ruckus Wireless**

### Access Point Configuration

**NOTE: This guide is for the Ruckus ZoneDirector release 9.8 or above. Earlier versions are not supported.**

Start by logging into your Ruckus ZoneDirector web interface.

### AAA Servers

1. Click Configure at the top and then AAA Servers on the left. Click Create New and configure with:

- **Name -** Guest WiFi
- **Type -** RADIUS
- **Auth Method -** PAP
- **Backup RADIUS Support -** Enabled
- **First Server IP Address -** {{primary_ip}}
- **Port -** {{auth_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}
- **Second Server IP Address -** {{backup_ip}}
- **Port -** {{auth_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}

Click **OK** to save. Next, click **Create New** again and configure with:

- **Name -** Guest WiFi Acct
- **Type -** RADIUS Accounting
- **Backup RADIUS Support -** Enabled
- **First Server IP Address -** {{primary_ip}}
- **Port -** {{acct_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}
- **Second Server IP Address -** {{backup_ip}}
- **Port -** {{acct_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}

Click **OK** to save.

### Hotspot

2. Click **Hotspot Services** on the left and then **Create New**. Configure with:

- **Name -** Guest WiFi
- **WISPr Smart Client Support -** None
- **Login Page -** {{splash_page_url}}
- **Redirect to the following URL -** Insert URL you want to redirect the user to
- **Authentication Server -** Guest WiFi
- **Accounting Server -** Guest WiFi Acct
- **Wireless Client Isolation -** Full
- **Walled Garden -** 107.178.250.42

Click **OK** to save.

### WLAN

3. Next, click WLANs on the left then Create New. Configure with:

- **Name -** Guest WiFi
- **ESSID -** Guest WiFi (or whatever you wish)
- **Type -** Hotspot Service (WISPr)
- **Authentication Method -** Open
- **Encryption Method -** Open
- **Hotspot Service -** Guest WiFi
- **Priority -** High
- **Inactivity Timeout -** 120

Click OK to save. To complete the set up you will need to SSH in to the ZoneDirector and type the commands below, one line at a time.

```
enable
config
no hotspot_redirect_https
wlan "Guest Wi-Fi"
called-station-id-type ap-mac
end
```
The configuration is now complete.

