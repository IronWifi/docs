# **Avaya**

---

This page explains the configuration of Avaya wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Avaya**

### Access Point Configuration

<span style="font-size: 13px; color: rgb(255, 0, 0);">**IMPORTANT NOTICE**: Your device must be running 7.0 firmware or above to continue.

Open a web browser and log in to your Avaya AP web interface.

Click on "**Security**" on the left menu and select "**External Radius**" on the sub menu.

Under **RADIUS Attribute Formatting**:

- **Called-Station-Id Attribute Format**<span >: Ethernet-MAC
- **Station MAC Format**<span >: UC-hyphenated (XX-XX-XX-XX-XX-XX)
- **Accounting**: On

Under **Accounting**<span >:

**- **Accounting Interval**: 300** Click **Save changes to flash** at the top right of the page.

Next, click on **SSIDs** on the left and then **SSID Management** on the sub menu.

Underneath the current SSID's, enter **Guest WiFi** and click on **Create**

This will create the new SSID. You now have access to the following settings. Please set the following:

- **SSID**: Ticked
- **Brdcst**: Ticked
- **Encryption**: None/Open and untick the **Global** checkbox
- **WPR**: Ticked
  
Next, scroll down the page and under **SSID Guest WiFi Web Page Redirection Configuration**, set the following:

- **Landing Page URL**: {{success_page_url}}
- **Server**: External Login
- **Redirect URL**: {{splash_page_url}}
- **Redirect Secret**: \*insert uam\_secret here\*
  
Next, under **SSID Guest WiFi WPR Whitelist Configuration**:

**IMPORTANT: You will need to add the below entries one by one until you have them all listed.**
  
107.178.250.42
  
If you need to load resources from external servers (SAML, social login), you will need to add other entries as well, instructions to configure the walled garden list in this case are available [here](https://ironwifi.com/walled-garden-list-guide).

Next, under **SSID Guest WiFi Authentication Service Configuration**:

<span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">Enter the following information:

- **Authentication Server**<span >: External Radius

Under **Primary**:

- **Host / IP Address**<span >: {{primary_ip}}
- **Port**<span >: {{auth_port}}
- **Shared Secret**<span >: {{shared_secret}}
- **Verify Secret**<span >: as above

Under **Secondary**:

- **Host / IP Address**<span >: {{backup_ip}}
- **Port**<span >: {{auth_port}}
- **Shared Secret**<span >: {{shared_secret}}
- **Verify Secret**<span >: {{shared_secret}}  
- **Accounting**<span >: ticked

Under **Primary**:

- **Host / IP Address**<span >: {{primary_ip}}
- **Port**<span >: {{acct_port}}
- **Shared Secret**<span >: {{shared_secret}}
- <span >**Verify Secret**<span >: {{shared_secret}}

Under **Secondary**:

- **Host / IP Address**<span >: {{backup_ip}}
- <span >**Port**<span >: {{acct_port}}
- <span >**Shared Secret**<span >: {{shared_secret}}
- **Verify Secret**<span >: {{shared_secret}}
    

<span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">Click **Save changes to flash**<span style="font-size: 13px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;"> at the top right of the page.

<span >

