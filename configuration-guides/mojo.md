# **Airtight / Mojo Networks**

---

This page explains the configuration of Airtight / Mojo Networks wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Mojo Networks**

### Access Point Configuration

Open a web browser and log in to your Mojo Cloud Management dashboard

Click **Configuration** at the top, then click the **RADIUS Profiles** icon and click the **Add RADIUS Profile** link. Configure with:

- Profile Name: guest1
- IP Address: {{primary_ip}}
- Authentication Port: {{auth_port}}
- Accounting Port: {{acct_port}}
- Shared secret: {{shared_secret}}

Click **Save** and then add a second RADIUS profile. Configure with:

- Profile Name: guest2
- IP Address: {{backup_ip}}
- Authentication Port: {{auth_port}}
- Accounting Port: {{acct_port}}
- Shared secret: {{shared_secret}}

Click **Save**.

Next, click **Configuration** at the top, then click the **Device Configuration** icon and click **SSID Profiles**. Click the **Add New Wi-Fi Profile** link and configure with:

- **Profile Name**: Guest Wi-Fi
- **SSID**: Guest Wi-Fi (or whatever you want to broadcast for your SSID)
- **Broadcast SSID**: Enabled

Under The **Security**  section:

- **Security Mode**: Open
- **Client Isolation**: Enabled
  
Under the **Network** section:

- **NAT** : Enabled
- **Start IP Address**: 10.1.0.2
- **End IP Address**: 10.1.0.254
- **Local IP Address**: 10.1.0.1
- **Subnet Mask**: 255.255.255.0
- **DNS Servers**: add: 8.8.8.8 and 8.8.4.4
- **Lease time**: 1440

Under the **Captive Portal**  section:

- **Enable Captive Portal**: Enabled
- **External Splash Page with RADIUS Authentication**: Enabled
- **Splash Page URL** {{splash_page_url}}
- **Shared Secret**: {{shared_secret}}
- **Walled Garden**: Add the below domains one by one

107.178.250.42
  
If you need to load resources from external servers (SAML, social login), you will need to add other entries as well, instructions to configure the walled garden list in this case are available [here](https://ironwifi.com/walled-garden-list-guide).

- **Redirect URL**: {{success_page_url}}
- **Enable HTTPS Redirection**: Disabled
  
Under the **Radius Settings link**:

- **Called Station Id**: %m
- **Primary Authentication Server**: guest1
- **Secondary Authentication Server**: guest2
- **Interval**: 2 mins
- **Primary Accounting Server**: guest1
- **Secondary Accounting Server**: guest2

**Click Save**  and then **Click Save** again. Finally, go back to **Device Configuration** and click **Device Templates**. Edit your current template, and under the **Radio Settings** section add the new SSID profile you created above to all radios.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
