# **Cisco Mobility Express**

---

This page explains configuration of Captive Portal with authentication through IronWifi for the Cisco Mobility Express. 

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cisco Mobility Express**

### Access Point Configuration

NOTE: You are required to use firmware v8.7.102.0 or above in order to continue.

Log in to your ME web interface and click the **"Switch to Expert View"** button at the top right.

On the left, click **Management > Admin Accounts** and then the **RADIUS** header. Configure with:

- **Authentication Call Station ID Type -** AP MAC Address:SSID
- **Authentication MAC Delimiter -** Hyphen
- **Accounting Call Station ID Type -** AP MAC Address:SSID
- **Accounting MAC Delimiter -** Hyphen

Click **Apply**. Next, click Add **RADIUS Authentication Server**. Configure with:

- **State -** Enabled
- **Server IP Address -** {{primary_ip}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** {{shared_secret}}
- **Port Number -** {{auth_port}}

Click **Apply** to Save. Next, click Add **RADIUS Authentication Server** again Configure with:

- **State -** Enabled
- **Server IP Address -** {{backup_ip}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** {{shared_secret}}
- **Port Number -** {{auth_port}}

Click **Apply** to Save. Next, click **Add RADIUS Accounting Server**. Configure with:

- **State -** Enabled
- **Server IP Address -** {{primary_ip}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** {{shared_secret}}
- **Port Number -** {{acct_port}}

Click **Apply** to Save. Next, click **Add RADIUS Accounting Server** again. Configure with:

- **State -** Enabled
- **Server IP Address -** {{backup_ip}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** {{shared_secret}}
- **Port Number -** {{acct_port}}

Click **Apply** to Save. Next, on the left, click **Wireless Settings > WLANs**. Click **Add New** and configure with:

On the **General** tab:

- **Profile Name -** Guest WiFi
- **SSID -** Guest WiFi (or whatever you wish)
- **Admin State -** Enabled
- **Radio Policy -** ALL
- **Broadcast SSID -** Yes

On the **WLAN Security** tab:

- **Guest Network -** Yes
- **Captive Network Assistant -** Yes
- **Captive Portal -** External Splash page
- **Captive Portal URL -** {{splash_page_url}}
- **Access Type -** RADIUS

Under the **RADIUS Server** header, click **Add RADIUS Authentication Server** and select the **first** server IP you previously added. Click **Apply**. Next, click** Add RADIUS Authentication Server** again and select the **second** server IP you previously added. Click **Apply**.

Next, click **Add RADIUS Accounting Server** and select the **first** server IP you previously added. Click **Apply**. Next, click **Add RADIUS Accounting Server** again and select the **second** server IP you previously added. Click **Apply**.

Under the **Pre Auth ACLs** header, click **Add URL Rules** and configure with:

- **URL -** ironwifi.com
- **Action -** Permit

Under the Advanced tab:

- **Allow AAA Override -** Yes

Click **Apply** to Save config. At the top right, be sure to click the **Save Configuration** button to avoid losing changes. Finally, you'll need to SSH or console to the ME AP and type the following commands in "enable" mode:

- config network web-auth https-redirect disable
- config network web-auth secureweb disable

Additionally, we need to prevent users from trying to log in to the ME GUI via RADIUS. Provided you have only added the two RADIUS servers above and don't have any others configured, run the following commands:

- config radius auth management 1 disable
- config radius auth management 2 disable

After applying the commands above you will need to reboot the controller. Type the below commands:

- save config
- reset system

The ME AP will now reboot and be ready for use.

NOTE: You need to add all the AP Base MACs to the portal. To see these, type show ap join stats summary all from the SSH or command line.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
