# **Cisco Meraki Go**

---

<<<<<<< HEAD
This page explains the configuration of Cisco Meraki Go wireless access points for external Captive  Portal and RADIUS server authentication.
=======
This page explains the Captive Portal configuration for Cisco Meraki Go and authentication with IronWifi.
>>>>>>> 9c20c74714ba89600f2da9faeb03135745652236

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cisco Meraki Go**

### Access Point Configuration

<<<<<<< HEAD
<div class="config-version">Meraki Go APs do not support RADIUS authentication and accounting. Therefore, some reports in the portal like users online now and network reports will be unavailable. Tiered Bandwidth is also unavailable.Open the Meraki Go app on your phone

<div class="config-step">Step 1 - Wireless SettingsPress the **Settings** icon at the bottom and then press WiFi network. Edit an existing network you wish to use or Add a new network. Configure with:

<div class="config-table"><div class="config-row"><div class="config-title">Network Name<div class="config-value">Guest WiFi (or whatever you wish)<div class="config-row"><div class="config-title">Password<div class="config-value">Leave blank (no password)<div class="config-row"><div class="config-title">Guest network<div class="config-value">EnabledPress **Save** to confirm.

<div class="config-step">Step 2 - Guest PortalOn the **SSID settings page** press the **Landing page** option. Press **Externally hosted** and configure with:

<div class="config-table"><div class="config-row"><div class="config-title">Website<div class="config-value">*insert access_url here*<div class="config-row"><div class="config-title">Timeout Frequency<div class="config-value">Every four hours<div class="config-row"><div class="config-title">Walled Garden<div class="config-value">Add the following entries:

\*.\*insert access\_domain here\*

\*.venuewifi.com

\*.openweathermap.org

\*.cloudfront.net

\*.stripe.com

<div class="config-info">Note: If you wish to support social network logins, you also need to add the below entries for each network you plan to support.**Facebook**:

\*.facebook.com

\*.fbcdn.net

\*.akamaihd.net

connect.facebook.net

**Twitter**:

\*.twitter.com

\*.twimg.com

**LinkedIn**:

\*.linkedin.com

\*.licdn.net

\*.licdn.com

**Instagram**:

\*.instagram.com

<div class="config-row"><div class="config-title">Redirect to Website<div class="config-value">*insert redirect_url here*Press **Save** to confirm and then return to the WiFi network settings. Configure with:

<div class="config-table"><div class="config-row"><div class="config-title">Active<div class="config-value">Enabled<div class="config-row"><div class="config-title">Guest Network<div class="config-value">Enabled<div class="config-row"><div class="config-title">Discoverable<div class="config-value">EnabledThe configuration is now complete.

=======
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
>>>>>>> 9c20c74714ba89600f2da9faeb03135745652236
