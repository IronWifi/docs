# **Draytek**

---

This page explains the configuration of Draytek wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Draytek**

### Access Point Configuration

**NOTE: You will require the Vigor 2862, 3220, 2926, 2952 Series with 3.9.0 firmware or above in order to continue.**

Log in to your Draytek Web Interface and click Hotspot Web Portal &gt;&gt; Profile Setup on the left menu.

Click an available Index, i.e. **1** and configure with:

- **Enable this profile**: Yes
- **Portal Method**: External Server
- **Captive Portal URL**: {{splash_page_url}}
- **Redirection URL**: {{success_page_url}}
- **Authentication Method**: Click External RADIUS Server and set:  
    - **Enable**: Yes  
    - **Server IP Address**: {{primary_ip}}  
    - **Destination Port**: {{auth_port}}  
    - **Shared Secret**: {{shared_secret}}  
    - **Confirm Shared Secret**: {{shared_secret}}  
    - **Enable Accounting**: Yes  
    - **Accounting Port**: {{acct_port}}  
      
Click **OK** to Save

- **MAC Address Format**: AA-BB-CC-DD-EE-FF

Click **Save and** **Next**. Now, click the **Dest Domain tab** and add the following entries, one per index:

107.178.250.42
  
If you need to load resources from external servers (SAML, social login), you will need to add other entries as well, instructions to configure the walled garden list in this case are available [here](https://ironwifi.com/walled-garden-list-guide).

Click **Save and Next** then configure with:

- **Expired Time After Activation**: 0 days 6 hours 0 min (or whatever you wish)
- **HTTPS Redirection**: No
- **Captive Portal Detection**: Yes
- **Landing Page After Authentication**: {{success_page_url}}
- **Applied Interfaces**: Select which SSID(s) you wish to enable the service on

Click **Finish** to Save. **Please ensure you reboot the router before continuing as this is a pre-requisite for the setting to apply.**

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
