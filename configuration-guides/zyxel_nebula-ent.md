# **Zyxel Nebula Cloud AP**

---

This page explains the configuration of Zyxel Nebula Cloud AP wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Zyxel Nebula Cloud AP**

### Access Point Configuration

Open a web browser and log in to your Nebula Control Center dashboard.

<div class="config-step">Step 1 - SSIDClick **AP &gt; Authentication** at the top. From the SSID dropdown, choose the one you wish to use, then configure with the below settings:

<div class="config-table"><div class="config-row"><div class="config-title">WLAN security<div class="config-value">Open<div class="config-row"><div class="config-title">Captive Portal<div class="config-value">Sign-on with: My RADIUS server<div class="config-row"><div class="config-title">Host<div class="config-value">*insert radius_server_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1812<div class="config-row"><div class="config-title">Secret<div class="config-value">*insert radius_secret here*click **Add a server** and add:

<div class="config-table"><div class="config-row"><div class="config-title">Host<div class="config-value">*insert radius_server2_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1812<div class="config-row"><div class="config-title">Secret<div class="config-value">*insert radius_secret here*<div class="config-row"><div class="config-title">RADIUS accounting<div class="config-value">RADIUS accounting enabled<div class="config-row"><div class="config-title">Host<div class="config-value">*insert radius_server_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1813<div class="config-row"><div class="config-title">Secret<div class="config-value">*insert radius_secret here*click **Add a server** again and add:

<div class="config-table"><div class="config-row"><div class="config-title">Host<div class="config-value">*insert radius_server2_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1813<div class="config-row"><div class="config-title">Secret<div class="config-value">*insert radius_secret here*<div class="config-row"><div class="config-title">Walled garden<div class="config-value">On<div class="config-row"><div class="config-title">Walled garden ranges<div class="config-value">\*.\*insert access\_domain here\*

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

<div class="config-row"><div class="config-title">Login on multiple client devices<div class="config-value">Mutiple device access simultaneously<div class="config-row"><div class="config-title">Strict Policy<div class="config-value">Block all access until sign-onClick on **Save Changes**.

<div class="config-step">Step 2 - Captive PortalClick **AP &gt; Captive portal** at the top. From the SSID dropdown, choose the one you wish to use, then configure with the below settings:

<div class="config-table"><div class="config-row"><div class="config-title">External captive portal URL<div class="config-value">*insert access_url here*<div class="config-row"><div class="config-title">After the captive portal page where the user should go?<div class="config-value">A Different URL:

{{success_page_url}}

Click **Save** to finish

The configuration is now complete.

