# **D-Link Nuclias Cloud**

---

This page explains the configuration of D-Link Nuclias Cloud wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **D-Link Nuclias Cloud**

### Access Point Configuration

Log in to your Nuclias Cloud portal.

<div class="config-step" data-identifyelement="493"><span data-identifyelement="495">Step 1 - RADIUSAt the top, click **Configure &gt; Access point &gt; RADIUS servers**. Then, click **Add a RADIUS server** and configure with:

<div class="config-table" data-identifyelement="508"><div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">RADIUS server name<div class="config-value" data-identifyelement="511">guest1_auth<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Host<div class="config-value" data-identifyelement="511">*insert radius_server_ip here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Port<div class="config-value" data-identifyelement="511">1812<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Secret<div class="config-value" data-identifyelement="511">*insert radius_secret here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Access level<div class="config-value" data-identifyelement="511">OrganizationClick **Save** to add the RADIUS server. Next, click **Add as RADIUS server** again and configure with:

<div class="config-table" data-identifyelement="508"><div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">RADIUS server name<div class="config-value" data-identifyelement="511">guest1_acct<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Host<div class="config-value" data-identifyelement="511">*insert radius_server_ip here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Port<div class="config-value" data-identifyelement="511">1813<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Secret<div class="config-value" data-identifyelement="511">*insert radius_secret here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Access level<div class="config-value" data-identifyelement="511">OrganizationClick **Save** to add the RADIUS server. Next, click **Add as RADIUS server** again and configure with:

<div class="config-table" data-identifyelement="508"><div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">RADIUS server name<div class="config-value" data-identifyelement="511">guest2_auth<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Host<div class="config-value" data-identifyelement="511">*insert radius_server2_ip here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Port<div class="config-value" data-identifyelement="511">1812<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Secret<div class="config-value" data-identifyelement="511">*insert radius_secret here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Access level<div class="config-value" data-identifyelement="511">OrganizationClick **Save** to add the RADIUS server. Next, click **Add as RADIUS server** again and configure with:

<div class="config-table" data-identifyelement="508"><div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">RADIUS server name<div class="config-value" data-identifyelement="511">guest2_acct<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Host<div class="config-value" data-identifyelement="511">*insert radius_server2_ip here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Port<div class="config-value" data-identifyelement="511">1813<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Secret<div class="config-value" data-identifyelement="511">*insert radius_secret here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Access level<div class="config-value" data-identifyelement="511">OrganizationClick **Save** to add the RADIUS server.

<div class="config-step" data-identifyelement="493"><span data-identifyelement="495">Step 2 - Walled gardenAt the top, click **Configure &gt; Access point &gt; Walled garden**. Then, click **Add a walled garden** and configure with:

<div class="config-table" data-identifyelement="498"><div class="config-row" data-identifyelement="499"><div class="config-title" data-identifyelement="500">Walled garden name<div class="config-value" data-identifyelement="501">guest<div class="config-row" data-identifyelement="499"><div class="config-title" data-identifyelement="500">Range<div class="config-value" data-identifyelement="501">Add the following entries one by one:

  
\*insert access\_domain here\*

venuewifi.com

openweathermap.org

cloudfront.net

stripe.com

<div class="config-info" data-identifyelement="530"><span data-identifyelement="509">Note: If you wish to support social network logins, you also need to add the below entries for each network you plan to support.**Facebook**:

facebook.com

fbcdn.net

akamaihd.net

connect.facebook.net

**Twitter**:

twitter.com

twimg.com

**LinkedIn**:

linkedin.com

licdn.net

licdn.com

**Instagram**:

instagram.com

Press **Save** to confirm.

<div class="config-step" data-identifyelement="493"><span data-identifyelement="495">Step 3 - SSIDAt the top, click **Configure &gt; Access point &gt; Profiles** and then **SSID** beside the AP profile you are using. Then, click **Add SSID** and configure with:

<div class="config-table" data-identifyelement="498"><div class="config-row" data-identifyelement="499"><div class="config-title" data-identifyelement="500">SSID name<div class="config-value" data-identifyelement="501">Guest WiFi (or whatever you wish)<div class="config-row" data-identifyelement="502"><div class="config-title" data-identifyelement="503">Band selection<div class="config-value" data-identifyelement="504">2.4GHz and 5GHzPress **Save** to confirm. Next, on the SSID you just created and configure with:

<div class="config-table" data-identifyelement="508"><div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Security<div class="config-value" data-identifyelement="511">Open<div class="config-row" data-identifyelement="512"><div class="config-title" data-identifyelement="513">Broadcast SSID<div class="config-value" data-identifyelement="514">Enable<div class="config-row" data-identifyelement="515"><div class="config-title" data-identifyelement="516">Guest Access mode<div class="config-value" data-identifyelement="517">Enable<div class="config-row" data-identifyelement="518"><div class="config-title" data-identifyelement="519">NAT mode<div class="config-value" data-identifyelement="517">Enable<div class="config-row" data-identifyelement="518"><div class="config-title" data-identifyelement="519">Station isolation<div class="config-value" data-identifyelement="517">EnablePress **Save** to confirm. Next, click on the **Captive Portal** tab and configure with:

<div class="config-table" data-identifyelement="508"><div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Captive portal<div class="config-value" data-identifyelement="511">Sign-on with External Captive Portal<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Option<div class="config-value" data-identifyelement="511">Custom External Captive Portal<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Splash page URL<div class="config-value" data-identifyelement="511">*insert access_url here*<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Primary RADIUS server<div class="config-value" data-identifyelement="511">*insert radius_server_ip here*:1812<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Secondary RADIUS server<div class="config-value" data-identifyelement="511">*insert radius_server2_ip here*:1812<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Primary accounting server<div class="config-value" data-identifyelement="511">*insert radius_server_ip here*:1813<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Secondary accounting server<div class="config-value" data-identifyelement="511">*insert radius_server2_ip here*:1813<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Session timeout<div class="config-value" data-identifyelement="511">240 minutes<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Idle timeout<div class="config-value" data-identifyelement="511">60 minutes<div class="config-row" data-identifyelement="509"><div class="config-title" data-identifyelement="510">Walled garden<div class="config-value" data-identifyelement="511">guestClick **Save** to confirm. Finally, click **PUSH CONFIGURATION** at the top to deploy the configuration to your AP(s).

The configuration is now complete.

