# **Alcatel-Lucent Instant (IAP)**

---

This page explains the configuration of Alcatel-Lucent Instant (IAP) wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Alcatel-Lucent Instant (IAP)**

### Access Point Configuration

Log in to your Alcatel-Lucent (Master) IAP

Under **Network** at the top left, click on **New**

Configure with:

- **Name (SSID)**: Guest WiFi (or whatever you wish)
- **Primary usage**: Guest

Click **Next** and configure with:

- **Client IP assignment**: Virtual Controller managed
- **Client VLAN assignment**: Default (unless you have a custom VLAN set up)

Click **Next** and configure with:

- **Splash page type**: External
- **Captive portal profile**: Click the dropdown and choose **New**. Configure with:

- **Name**: guestwifi
- **Type**: Radius Authentication
- **IP or hostname**: \*insert access\_domain here\*
- **URL**: /access/?iapmac=&lt;ap-mac&gt; (i.e. /access/?iapmac=00-0B-86-6E-C5-F8)
- **Port**: 80
- **Use https**: Disabled
- **Captive portal failure**: Deny internet
- **Automatic URL whitelisting**: Disabled
- **Redirect URL**: {{success_page_url}}

Click **OK** to save

- **Auth server 1**: Click the dropdown and choose **New**. Configure with:

- **Type:** RADIUS
- **Name**: guestwifi1
- **IP address**: {{primary_ip}}
- **Auth port**: 1812
- **Acct port**: 1813
- **Shared key**: {{shared_secret}}
- **Retype key**: as abov

Click **OK** to save

- **Auth server 2**: Click the dropdown and choose **New**. Configure with
- **Type:** RADIUS
- 
- **Name**: guestwifi2
- **IP address**: {{backup_ip}}
- **Auth port**: 1812
- **Acct port**: 1813
- **Shared key**: {{shared_secret}}
- **Retype key**: as above

Click<span> </span>**OK** to save

- **Reauth interval**: 24 hrs
- **Accounting**: Enabled
- **Accounting mode**: Authentication
- **Accounting interval**: 3 min
- **Blacklisting**: Disabled
- **Walled garden**: Click the link "Blacklist: 0 Whitelist: 0" and you will see the below screen:  
      
    Under **Whitelist** Click **New** and add all the below domains one by one until all are in the list:

\*insert access\_domain here\*  

107.178.250.42
  
If you need to load resources from external servers (SAML, social login), you will need to add other entries as well, instructions to configure the walled garden list in this case are available [here](https://ironwifi.com/walled-garden-list-guide).

Press **OK** when all the domains have been added to save  
  
Click **Next** and configure with:

- **Access Rules**: Role-based  
      
    Under **Roles** click **New** and enter **Preauth** as the name  
    Under **Access Rules for Preauth** click **New** and add the following rule:
- **Rule type**: Access control
- **Service**: Network - any
- **Action**: Allow
- **Destination**: to domain name
- **Domain name**: \*insert access\_domain here\*

Click **OK** to save.

You need to add a rule (just like you did above), for all the below domains:

\*insert access\_domain here\*

107.178.250.42
  
If you need to load resources from external servers (SAML, social login), you will need to add other entries as well, instructions to configure the walled garden list in this case are available [here](https://ironwifi.com/walled-garden-list-guide).

- **Assign pre-authentication role**: select **Preauth**

Click<span> </span>**Finish** to complete the set up.
