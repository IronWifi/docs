# **Cisco Catalyst**

---

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cisco catalyst**

### Access Point Configuration

Open a web browser and log in to your Cisco Catalyst web interface. At the top right, click the Settings icons and enable the **Expert** mode.

1. Click on **Configuration > Security > Web Auth** on the left. Click in to the **global** profile and configure with:

- **Virtual IPv4 Address -** 192.0.2.1

Click **Apply** to save.

2. Next, click the **Add** button. Configure with:

- **Parameter-map name -**	guest_wifi
- **Maximum HTTP connections -**	200
- **Init-State Timeout -**	3600
- **Type -**	webauth

Click **Apply to Device** to save. 

3. Next, click in to the profile you just created and configure with:

On the **General** tab:

- **Banner Type -**	None
- **Turn-on Consent with Email -**	Disabled
- **Captive Bypass Portal -**	Disabled
- **Disable Success Window -**	Enabled
- **Disable Logout Window -**	Enabled
- **Sleeping Client Status -**	Enabled
- **Sleeping Client Timeout -**	720

On the **Advanced** tab:

- **Redirect for log-in -**	{{splash_page_url}}
- **Redirect On-Success -**	{{success_page_url}}
- **Redirect On-Failure -**	{{splash_page_url}}
- **Redirect Append for AP MAC Address -**	ap_mac
- **Redirect Append for Client MAC Address -**	client_mac
- **Redirect Append for WLAN SSID -**	wlan_ssid
- **Portal IPV4 Address -**	107.178.250.42

Click **Apply** to save. 

4. Next, click on **Configuration > Security > AAA** on the left. Select the **Servers / Groups** tab click **Add**. Configure with:

- **Name -**	rad1
- **IPv4 / IPv6 Server Address -** {{primary_ip}}
- **Key Type -**	0
- **Key -** {{shared_secret}}
- **Confirm Key -**	{{shared_secret}}
- **Auth Port -**	{{auth_port}}
- **Acct Port -**	{{acct_port}}
- Server Timeout	10
- **Retry Count -**	3
- **Support for CoA -**	Enabled

Click **Apply to Device** to save.

5. Next, click **Add** again and configure with:

- **Name -**	rad2
- **IPv4 / IPv6 Server Address -** {{backup_ip}}
- **Key Type -**	0
- **Key -**	{{shared_secret}}
- **Confirm Key -**	{{shared_secret}}
- **Auth Port -**	{{auth_port}}
- **Acct Port -**	{{acct_port}}
- **Server Timeout -**	10
- **Retry Count -**	3
- **Support for CoA -**	Enabled

Click **Apply to Device** to save. 

6. On the **Server Groups** sub tab, click **Add**. Configure with:

- **Name -**	guest_radius
- **Group Type -**	RADIUS
- **MAC-Delimiter -**	hyphen
- **MAC-Filtering -**	none
- **Assigned Servers -**	rad1, rad2

Click **Apply to Device** to save. 

7. Next, click on the **AAA Method List** tab. Click **Add** and configure with:

- **Method List Name -**	guest_auth
- **Type -**	login
- **Group Type -**	group
- **Assigned Server Groups -**	guest_radius

Click **Apply to Device** to save.

8. Next, click the **Accounting** sub nav menu on the left and click **Add**. Configure with:

- **Method List Name -**	guest_acct
- **Type -**	identity
- **Assigned Server Groups -**	guest_radius

Click **Apply to Device** to save. 

9. Next, click the **AAA Advanced** tab and then the Show **Advanced Settings >>>** option. Configure both Accounting and Authentication with:

- **Call Station ID -**	ap-macaddress-ssid
- **Call Station ID Case -**	upper
- **MAC-Delimiter -**	hyphen
- **Username Case -**	lower
- **Username Delimiter -**	none

Click **Apply to Device** to save. 

10. Next, click **Configuration > Tags & Policies > WLANs** on the left. Click **Add** or edit an existing WLAN and configure with:

On the **General** tab:

- **Profile Name -**	Guest WiFi
- **SSID -**	Guest WiFi (or whatever you wish)
- **Status -**	Enabled
- **Radio Policy -**	All
- **Broadcast SSID -**	Enabled

On the **Security > Layer 2** tab:

- **Layer 2 Security Mode -**	None
- **MAC Filtering -**	Disabled

On the **Security > Layer 3** tab, click **Show Advanced Settings >>>** and configure with:

- **Web Policy -**	Enabled
- **Web Auth Parameter Map -**	guest_wifi
- **Authentication List -**	guest_radius
- **On Mac Filter Failure -**	Disabled
- **Splash Web Redirect -**	Disabled
- **IPv4 ACL -**	preauth_v4

Click **Apply to Device** to save.

11. Next, click **Configuration > Security > URL Filters**. Click **Add** and configure with:

- **List Name -**	guest_url_filter
- **Type -**	PRE_AUTH
- **Action -**	PERMIT
- **URLs -** 107.178.250.42

You will also need to include the following domains in the walled garden list  if you want to make use of social login.

**Facebook:** | Twitter | Linkedin | Instagram |
------------- | ------- | -------- | --------- |
*.facebook.com | *.twitter.com | *.linkedin.com | *.instagram.com
*.fbcdn.net | *.twimg.com | *.licdn.net |
*.akamaihd.net |          | *.licdn.com |
connect.facebook.net |     | *.licdn.com |

Click **Apply** to save.

Next, click **Configuration > Tags & Profiles > Policy** on the left. 

12. Click **Add**, leaving all settings at default apart from the following:

On the **General** tab:

- **Name -**	guest_policy
- **Status -**	Enabled

On the **Access Policies** tab:

- **URL Filters -**	guest_url_filter

On the **Advanced** tab:

- **Session Timeout -**	43200
- **Idle Timeout -**	3600
- **Allow AAA Override -**	Enabled
- **Accounting List -**	guest_acct

Click **Apply to Device** to save.

14. Next, click **Configuration > Tags & Profiles > Tags** on the left. Click **Add** and configure with:

- **Name -**	guest_tag
- **WLAN Profile -**	Guest WiFi
- **Policy Profile -**	guest_policy

Click **Apply to Device** to save. 

15. Finally, click **Administration > Management > HTTP/HTTPS/Netconf** on the left. Configure with:

- **HTTP Access -**	Enabled
- **HTTPS Access -**	Enabled

Be sure to click on **Save Configuration** at the top right of the page to ensure your changes are persisted on reboot.

The configuration is now complete.



