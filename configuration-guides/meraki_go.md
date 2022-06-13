# **Cisco Meraki Go**

---

This page explains the Captive Portal configuration for Cisco Meraki Go and authentication with IronWifi.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cisco Meraki Go**

### Access Point Configuration

_Meraki Go APs do not support RADIUS authentication and accounting. Therefore, some reports in the portal like users online now and network reports will be unavailable. Tiered Bandwidth is also unavailable.
Open the Meraki Go app on your phone_

## Step 1 - Wireless Settings

Press the Settings icon at the bottom and then press WiFi network. Edit an existing network you wish to use or Add a new network. Configure with:

- **Network Name** - Guest WiFi (or whatever you wish)
- **Password** - Leave blank (no password)
- **Guest network** -	Enabled

Press Save to confirm.

## Step 2 - Guest Portal

On the SSID settings page press the Landing page option. Press Externally hosted and configure with:

- **Website** - {{splash_page_url}}
- **Timeout Frequency** -	Every four hours
- **Walled Garden**	- *.ironwifi.com
- **Redirect to Website** -	{{success_page_url}}

Press Save to confirm and then return to the WiFi network settings. Configure with:

- **Active** - Enabled
- **Guest Network**	- Enabled
- **Discoverable**	- Enabled

The configuration is now complete.
