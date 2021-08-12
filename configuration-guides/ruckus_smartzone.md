# **Ruckus SmartZone**

---

**!Note!**: Please make sure you are running SmartZone v3.0 or above in order for this to work

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Ruckus NBI**

### Access Point Configuration

Log into your SmartZone web interface.

1. Click **Services & Profiles > Authentication** on the left. Click the **Proxy (SZ Authenticator)** tab then **Create** and configure with:

- **Name -** Guest WiFi
- **Service Protocol -** RADIUS
- **Primary Server IP Address -** {{primary_ip}}
- **Port -** {{primary_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}
- **Backup RADIUS -** Enable Secondary Server
- **Secondary Server IP Address -** {{backup_ip}}
- **Port -** {{primary_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}

Click **OK** to save.

2. Next, click **Accounting** on the left. Click the **Proxy** tab then **Create** and configure with:

- **Name -** Guest WiFi Acct
- **Primary Server IP Address -** {{primary_ip}}
- **Port -** {{primary_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}
- **Backup RADIUS -** Enable Secondary Server
- **Secondary Server IP Address -** {{backup_ip}} 
- **Port -** {{primary_port}}
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}

Click **OK** to save.

### Hotspot

3. Click **Hotspots & Portals** on the left. Click the **Hotspot (WISPr)** tab then **Create** and configure with:

- **Portal Name -**	Guest Wi-Fi
- **Smart Client Support -**	None
- **Login URL -**	External
- **Redirect unauthenticated users to (Primary) -**	{{splash_page_url}}
- **Redirected MAC Format -**	AA-BB-CC-DD-EE-FF
- **HTTPS Redirect -**	ON
- **Start Page - Redirect to the following URL -**	*insert redirect_url here*
- **Walled Garden List -** 107.178.250.42

You will also need to include the following domains in the walled garden list  if you want to make use of social login.

**Facebook:** | Twitter | Linkedin | Instagram |
------------- | ------- | -------- | --------- |
*.facebook.com | *.twitter.com | *.linkedin.com | *.instagram.com
*.fbcdn.net | *.twimg.com | *.licdn.net |
*.akamaihd.net |          | *.licdn.com |
connect.facebook.net |     | *.licdn.com |

Click **OK** to save.

### Wireless LAN

4. Click **Wireless LANs** on the left, then click **Create**. Configure with:

Under General Options:

- **Name -**	Guest Wi-Fi
- **SSID -**	Guest Wi-Fi (or whatever you wish)
- **Zone -**	Select a zone
- **WLAN Group -**	Select a group (or default)

Under Authentication Options:

- **Authentication Type -**	Hotspot (WISPr)
- **Method -**	Open

Under Encryption Options:

- **Method -**	None

Under Hotspot Portal:

- **Hotspot (WISPr) Portal -**	Guest Wi-Fi
- **Bypass CNA -**	Off
- **Authentication Service -**	ON - Use Controller as proxy - Guest WiFi
- **Accounting Service -**	ON - Use Controller as Proxy - Guest WiFi Acct
- **Send interim update -**	every 2 Minutes

Under RADIUS Options:

- **NAS ID -**	AP MAC
- **Delimiter -**	Dash
- **Single Session ID Accounting -**	ON
- **Called Station ID -**	AP MAC

Click **OK** to save.

### Northbound API

5. Click **System > General Settings** on the left and then the **WISPr Northbound Interface** tab. Cconfigure as follows:

- **Enable Northbound Portal Interface Support -**	ON
- **User Name -**	api
- **Password -**	enter any password you choose

Click **OK** to save.

To complete the set up you will need to log in to the IronWifi console, and under **Networks > Captive Portals > Your Captive Portal** you will need to enter your SmartZone Public IP and the Northbound Password you chose above. This allows our system to talk to the SmartZone for authenticating users and is a mandatory step.

Please create a new port forward with the following:

- **Local/Internal IP -**	Your Smartzone internal LAN IP (e.g. 192.168.0.1)
- **Protocol -**	TCP
- **Destination Port -**	9080


The configuration is now complete.










