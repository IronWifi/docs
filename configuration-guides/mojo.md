# **Airtight / Mojo Networks**

---

This page explains the configuration of Airtight / Mojo Networks wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Airtight / Mojo Networks**

### Access Point Configuration

Open a web browser and log in to your Mojo Cloud Management dashboard

Click **Configuration** at the top, then click the **RADIUS Profiles** icon and click the **Add RADIUS Profile** link. Configure with:

- Profile Name: guest1
- IP Address: {{primary_ip}}
- Authentication Port: 1812
- Accounting Port: 1813
- Shared secret: {{shared_secret}}

Click **Save** and then add a second RADIUS profile. Configure with:

- Profile Name: guest2
- IP Address: {{backup_ip}}
- Authentication Port: 1812
- Accounting Port: 1813
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
- **Shared Secret**: \*insert uam\_secret here\*
- **Walled Garden**: Add the below domains one by one (opting for ports 80 and 443)\*insert access\_domain here\*
    
    venuewifi.com
    
    openweathermap.org
    
    cloudfront.net
    
    stripe.com
    
    **<span style="font-size: 13px; color: rgb(255, 0, 0);">If you wish to support social network logins, you also need to add the domains below for each network you plan to support**
    
    <table border="1" cellpadding="0" cellspacing="0" id="table30325"><tbody><tr><td>**Facebook**</td><td>**Twitter**</td><td>**LinkedIn**</td><td>**Instagram**</td></tr><tr ><td>facebook.com  
    fbcdn.net  
    akamaihd.net  
    connect.facebook.net  
    </td><td>twitter.com  
    twimg.com  
    </td><td>linkedin.com  
    licdn.net  
    licdn.com  
      
    </td><td>instagram.com</td></tr></tbody></table>
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