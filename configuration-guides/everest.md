# **Everest Networks**

---

This page explains the configuration of Everest Networks wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Everest Networks**

### Access Point Configuration

Open a web browser and log in to your Everest Cloud (BaseCamp).

Click **Wireless Networks** on the left menu, the **Add** at the top right. Configure with:

- Network Name - Guest WiFi
- SSID - Guest WiFi (or whatever you wish)
- Security - Open
- Captive Portal Enabled - Yes
- Enter splash URL - {{splash_page_url}}
- Session Timeout - 86400

Select Third Party Integration

**Under Primary RADIUS Authentication Server**
- IP Address - {{primary_ip}}
- Port - {{auth_port}}
- Shared Secret - {{shared_secret}}
- Confirm Shared Secret - {{shared_secret}}

**Under Primary RADIUS Accounting Server**
- IP Address - {{primary_ip}}
- Port - {{acct_port}}
- Shared Secret - {{shared_secret}}
- Confirm Shared Secret - {{shared_secret}}

**Under Secondary RADIUS Authentication Server**
- IP Address - {{backup_ip}}
- Port - {{auth_port}}
- Shared Secret - {{shared_secret}}
- Confirm Shared Secret - {{shared_secret}}

**Under Secondary RADIUS Accounting Server**
- IP Address - {{backup_ip}}
- Port - {{acct_port}}
- Shared Secret - {{shared_secret}}
- Confirm Shared Secret - {{shared_secret}}

Click **Save** at the top right.

Wireless Network

- Click **Walled Garden** at the top and configure with:
- Domain **insert access_domain here*
- Click the **+** icon to add. You now need to add the following domains in the same way:

Domains
*.ironwifi.com

Note: If you wish to support social network logins, you also need to add the below domains for each network you plan to support.
**Facebook**:
- *.facebook.com
- *.fbcdn.net
- *.akamaihd.net
- connect.facebook.net

Twitter:
- *.twitter.com
- *.twimg.com

LinkedIn:
- *.linkedin.com
- *.licdn.net
- *.licdn.com

Instagram:
- *.instagram.com

Finally, click in to the Wireless Network (Guest WiFi) you just created, select the AP's you wish to use this configration and then click Apply to APs at the top.

The configuration is now complete.
