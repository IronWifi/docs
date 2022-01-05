# **Avaya**

---

This page explains the configuration of Avaya wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Avaya**

### Access Point Configuration

<span style="font-size: 13px; color: rgb(255, 0, 0);">**IMPORTANT NOTICE**: Your device must be running 7.0 firmware or above to continue.</span>

Open a web browser and log in to your Avaya AP web interface.

Click on "**Security**" on the left menu and select "**External Radius**" on the sub menu.

Under **RADIUS Attribute Formatting**:

- **Called-Station-Id Attribute Format**<span style="font-size: 13px;">: Ethernet-MAC</span>
- **Station MAC Format**<span style="font-size: 13px;">: UC-hyphenated (XX-XX-XX-XX-XX-XX)</span>
- **Accounting**<span>: On</span>

<div>Under **Accounting**<span style="font-size: 13px;">:</span>

**- **Accounting Interval**<span>: 300</span>** <div><div>Click **Save changes to flash** at the top right of the page.

<span>Next, click on </span>**SSIDs**<span> on the left and then </span>**SSID Management**<span> on the sub menu.</span>

Underneath the current SSID's, enter **Guest WiFi** and click on **Create**

  
This will create the new SSID. You now have access to the following settings. Please set the following:

- **SSID**: Ticked
- **Brdcst**: Ticked
- **Encryption**: None/Open and untick the **Global** checkbox
- **WPR**: Ticked

  
<span>Next, scroll down the page and under </span>**SSID Guest WiFi Web Page Redirection Configuration**<span>, set the following:</span>

**Landing Page URL**: {{success_page_url}}

**Server**: External Login

**Redirect URL**: {{splash_page_url}}

**Redirect Secret**: \*insert uam\_secret here\*

  
Next, under **SSID Guest WiFi WPR Whitelist Configuration**:

**IMPORTANT: You will need to add the below entries one by one until you have them all listed.**

  
<div style=""><span>\*.\*insert access\_domain here\*</span>

\*.venuewifi.com

<span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">openweathermap.org</span>

<span style="font-size: 13px;">\*.</span><span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">cloudfront.net</span>

<span>\*.stripe.com</span>

**<span style="font-size: 13px; color: rgb(255, 0, 0);">If you wish to support social network logins, you also need to add the domains below for each network you plan to support</span>**

<table border="1" cellpadding="0" cellspacing="0" id="table30325" style="background-color: rgb(255, 255, 255);"><tbody style="font-size: 13px;"><tr style="font-size: 13px;"><td>**Facebook**</td><td>**Twitter**</td><td>**LinkedIn**</td><td>**Instagram**</td></tr><tr style="font-size: 13px;"><td><span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">facebook.com</span>  
  
<span style="font-size: 13px;">\*.</span><span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">fbcdn.net</span>  
<span style="font-size: 13px;">\*.</span><span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">akamaihd.net</span>  
<span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">connect.facebook.net</span><span style="font-size: 13px;">  
</span>  
</td><td><span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">twitter.com</span>  
  
<span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">twimg.com</span><span style="font-size: 13px;">  
</span>  
</td><td><span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">linkedin.com</span>  
  
<span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">licdn.net</span>  
  
<span style="font-size: 13px;">\*.</span><span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">licdn.com</span>  
  
</td><td><span style="font-size: 13px;">\*.</span><span style="font-size: 13px;">instagram.com</span>  
</td></tr></tbody></table>

Next, under **SSID Guest WiFi Authentication Service Configuration**:

<span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">Enter the following information:</span>

- **Authentication Server**<span style="font-size: 13px;">: External Radius</span>

Under **Primary**:

- **Host / IP Address**<span style="font-size: 13px;">: \*insert radius\_server here\*</span>
- **Port**<span style="font-size: 13px;">: 1812</span>
- **Shared Secret**<span style="font-size: 13px;">: {{shared_secret}}</span>
- **Verify Secret**<span style="font-size: 13px;">: as above</span>

Under **Secondary**:

- **Host / IP Address**<span style="font-size: 13px;">: \*insert radius\_server2 here\*</span>
- **Port**<span style="font-size: 13px;">: 1812</span>
- **Shared Secret**<span style="font-size: 13px;">: {{shared_secret}}</span>
- **Verify Secret**<span style="font-size: 13px;">: as above  
      
      
    </span>
- **Accounting**<span style="font-size: 13px;">: ticked</span>

Under **Primary**:

- **Host / IP Address**<span style="font-size: 13px;">: \*insert radius\_server here\*</span>
- **Port**<span style="font-size: 13px;">: 1813</span>
- **Shared Secret**<span style="font-size: 13px;">: {{shared_secret}}</span>
- <span style="font-size: 13px;">**Verify Secret**</span><span style="font-size: 13px;">: as above  
      
    </span>

Under **Secondary**:

<div>- **Host / IP Address**<span style="font-size: 13px;">: \*insert radius\_server2 here\*</span>
- <span style="font-size: 13px;">**Port**</span><span style="font-size: 13px;">: 1813</span>
- <span style="font-size: 13px;">**Shared Secret**</span><span style="font-size: 13px;">: {{shared_secret}}</span>
- **Verify Secret**<span style="font-size: 13px;">: as above  
    </span>

<span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">Click </span>**Save changes to flash**<span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;"> at the top right of the page.</span>

<span style="font-size: 13px;"></span>

</div></div></div></div></div>