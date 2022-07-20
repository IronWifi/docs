# **D-Link Nuclias Cloud**

---

This page explains the configuration of D-Link Nuclias Cloud wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **D-Link Nuclias Cloud**

### Access Point Configuration

Log in to your Nuclias Cloud portal.

## Step 1 - RADIUS

At the top, click Configure > Access point > RADIUS servers. Then, click Add a RADIUS server and configure with:

- **RADIUS server name -** guest_auth
- **Host -** {{primary_ip}}
- **Port -** {{auth_port}}
- **Secret -** {{shared_secret}}
- **Access level -** Organization

Click Save to add the RADIUS server. Next, click Add as RADIUS server again and configure with:

- **RADIUS server name -** guest_acct
- **Host -** {{primary_ip}}
- **Port -** {{acct_port}}
- **Secret -** {{shared_secret}}
- **Access level -** {{Organization}}

Click Save to add the RADIUS server. Next, click Add as RADIUS server again and configure with:

- **RADIUS server name -** guest2_auth
- **Host -** {{backup_ip}}
- **Port -** {{auth_port}}
- **Secret -** {{shared_secret}}
- **Access level -** Organization

Click Save to add the RADIUS server. Next, click Add as RADIUS server again and configure with:

- **RADIUS server name -** guest2_acct
- **Host -** {{backup_ip}}
- **Port -** {{acct_port}}
- **Secret -** {{shared_secret}}
- **Access level -** Organization

Click Save to add the RADIUS server.

## Step 2 - Walled garden

At the top, click Configure > Access point > Walled garden. Then, click Add a walled garden and configure with:

- **Walled garden name -** guest
- **Range -** *access domain here*

Press Save to confirm.

## Step 3 - SSID

At the top, click Configure > Access point > Profiles and then SSID beside the AP profile you are using. Then, click Add SSID and configure with:

- **SSID name -**	Guest WiFi (or whatever you wish)
- **Band selection -** 2.4GHz and 5GHz

Press Save to confirm. Next, on the SSID you just created and configure with:

- **Security -** Open
- **Broadcast SSID -** Enable
- **Guest Access mode	-** Enable
- **NAT mode -** Enable
- **Station isolation -** Enable

Press Save to confirm. Next, click on the Captive Portal tab and configure with:

- **Captive portal -** Sign-on with External Captive Portal
- **Option -** Custom External Captive Portal
- **Splash page URL -**	{{splash_page_url}}
- **Primary RADIUS server -**	{{primary_ip}}
- **Secondary RADIUS server -** {{backup_ip}}
- **Primary accounting server	-** {{primary_ip}}
- **Secondary accounting server	-** {{backup_ip}}
- **Session timeout -** 240 minutes
- **Idle timeout -** 60 minutes
- **Walled garden -** guest

Click Save to confirm. Finally, click PUSH CONFIGURATION at the top to deploy the configuration to your AP(s).

The configuration is now complete.
