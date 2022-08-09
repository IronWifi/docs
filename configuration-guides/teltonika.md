# **Teltonika RU Series**

---

This page explains the configuration of Teltonika RU Series wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Teltonika RU Series**

### Access Point Configuration

NOTE: You will require firmware version R_00.07.00 or above in order to continue

Log in to your Teltonika web interface. At the top, click **Network > Wireless**. Click **Add** and configure with:

- **Enable wireless**: Yes
  
<u>Under **Device Configuration**</u>

- **SSID**: Guest WiFi (or whatever you wish)

  
<u>Under **Interface Configuration**</u>

- **Encryption**: No encryption

  
Click **Save**. **Next**, at the top click **Services &gt; Hotspot**. Click **Edit** beside your new SSID. Configure with:

On the **General** tab:

<u>Under </u>**<u>General Settings</u>**

- **Configuration profile**: Custom
- **Enable**: Yes
- **AP IP**: Leave default
- **Logout IP**: Leave default
- **Authentication mode**: External radius
- **Authentication protocol**: PAP
- **RADIUS server #1**: {{primary_ip}}
- **RADIUS server #2**: {{backup_ip}}
- **Authentication port**: {{auth_port}}
- **Accounting port**: {{acct_port}}
- **Radius secret key**: {{shared_secret}}
- **UAM port**: Leave default
- **UAM UI port**: Leave default
- **UAM secret**: {{shared_secret}}
- **NAS Identifier**: guest
- **Swap octets**: Yes
- **External Landing Page**: Yes
- **Landing page address**: {{splash_page_url}}
- **HTTPS redirect**: No

<u>Under</u>**<u> Walled Garden</u>**

Click **Add** and configure with:

- **Enable**: Yes
- **Address**: domain name of your landing page
- **Allow subdomains**: Yes

**If you wish to support social network logins, you also need to add the following domains for each network you plan to support**

<table cellspacing="1"><tbody><tr><td>**Facebook**  
</td><td>facebook.com  
fbcdn.net  
akamaihd.net  
connect.facebook.net  
  
</td></tr><tr><td>**Twitter**  
</td><td>twitter.com  
twimg.com  
  
</td></tr><tr><td>**LinkedIn**  
</td><td>linkedin.com  
licdn.com  
  
</td></tr><tr><td>**Instagram**  
</td><td>instagram.com  
  
</td></tr><tr><td>**Weibo**  
</td><td>weibo.com  
sina.com.cn  
  
</tr></tbody></table>

Click **Save** to apply.

