# **Everest Networks**

---

This page explains the configuration of Everest Networks wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Everest Networks**

### Access Point Configuration

Open a web browser and log in to your Everest Cloud (BaseCamp).

<div class="config-step">Step 1 - Wireless NetworkClick **Wireless Networks** on the left menu, the **Add** at the top right. Configure with:

<div class="config-table"><div class="config-row"><div class="config-title">Network Name<div class="config-value">Guest WiFi<div class="config-row"><div class="config-title">SSID<div class="config-value">Guest WiFi (or whatever you wish)<div class="config-row"><div class="config-title">Security<div class="config-value">Open<div class="config-row"><div class="config-title">Captive Portal Enabled<div class="config-value">Yes<div class="config-row"><div class="config-title">Enter splash URL<div class="config-value">*insert access_url here*<div class="config-row"><div class="config-title">Session Timeout<div class="config-value">86400<div class="config-row"><div class="config-title">Select Third Party Integratior<div class="config-value">Purple**Under Primary RADIUS Authentication Server**

<div class="config-table"><div class="config-row"><div class="config-title">IP Address<div class="config-value">*insert radius_server_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1812<div class="config-row"><div class="config-title">Shared Secret<div class="config-value">*insert radius_secret here*<div class="config-row"><div class="config-title">Confirm Shared Secret<div class="config-value">as above**Under Primary RADIUS Accounting Server**

<div class="config-table"><div class="config-row"><div class="config-title">IP Address<div class="config-value">*insert radius_server_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1813<div class="config-row"><div class="config-title">Shared Secret<div class="config-value">*insert radius_secret here*<div class="config-row"><div class="config-title">Confirm Shared Secret<div class="config-value">as above**Under Secondary RADIUS Authentication Server**

<div class="config-table"><div class="config-row"><div class="config-title">IP Address<div class="config-value">*insert radius_server2_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1812<div class="config-row"><div class="config-title">Shared Secret<div class="config-value">*insert radius_secret here*<div class="config-row"><div class="config-title">Confirm Shared Secret<div class="config-value">as above**Under Secondary RADIUS Accounting Server**

<div class="config-table"><div class="config-row"><div class="config-title">IP Address<div class="config-value">*insert radius_server2_ip here*<div class="config-row"><div class="config-title">Port<div class="config-value">1813<div class="config-row"><div class="config-title">Shared Secret<div class="config-value">*insert radius_secret here*<div class="config-row"><div class="config-title">Confirm Shared Secret<div class="config-value">as aboveClick **Save** at the top right.

<div class="config-step">Step 1 - Wireless NetworkClick **Walled Garden** at the top and configure with:

<div class="config-table"><div class="config-row"><div class="config-title">Domain<div class="config-value">*.*insert access_domain here*Click the **+** icon to add. You now need to add the following domains in the same way:

<div class="config-table"><div class="config-row"><div class="config-title">Domains<div class="config-value">\*.venuewifi.com

\*.cloudfront.net

\*.openweathermap.org

\*.stripe.com

<div class="config-info">Note: If you wish to support social network logins, you also need to add the below domains for each network you plan to support.**Facebook**:

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

Finally, click in to the Wireless Network (Guest WiFi) you just created, select the AP's you wish to use this configration and then click **Apply to APs** at the top.

The configuration is now complete.

