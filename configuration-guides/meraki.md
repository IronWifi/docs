# **Cisco Meraki**

---

This page explains the configuration of Cisco Meraki wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cisco Meraki**

### Access Point Configuration

Sign-in to the Meraki cloud portal.

1. Navigate to **Wireless -> Configure -> SSIDs** and define a network that we will protect with a Captive Portal with RADIUS authentication. Click edit settings next to **Access Control**. Configure **Access Control** with:

- **Association requirements -** Open (no encryption)
- **Splash page -** Sign-on with my RADIUS server

_RADIUS for splash page_

- **1. Host -** {{primary_ip}}
- **1. Port -** {{auth_port}}
- **1. Secret -** {{shared_secret}}
- **2. Host -** {{backup_ip}}
- **2. Port -** {{auth_port}}
- **2. Secret -** {{shared_secret}}
- **Failover policy -** Deny access
- **Load balancing policy -** Strict priority order
- **Network access control -** Disabled
- **Assign group policies by device type -** Disabled
- **Walled Garden -** Walled Garden is enabled
- **Walled Garden Ranges -** 107.178.250.42/32

_RADIUS accounting_  -  **If you don't see RADIUS Accounting servers, contact Meraki support to enable this feature in your account.**

- **RADIUS accounting -** enabled
- **1. Host -** {{primary_ip}}
- **1. Port -** {{acct_port}}
- **1. Secret -** {{shared_secret}}
- **2. Host -** {{backup_ip}}
- **2. Port -** {{acct_port}}
- **2. Secret -** {{shared_secret}}
- **Data-Carrier Detect** - enabled
 

2. Navigate to **Wireless -> Configure -> Splash page** and configure:

- **Custom Splash URL -** {{splash_page_url}}


If data-carrier detect is enabled, sessions will be revoked and accounted for whenever a client disassociates from a network. To allow clients to reassociate to the network without re-authorization, do not enable data-carrier detect.

If you have devices that don't have support for two way authentication like printers, Smart TV, etc., you can white-list these devices directly in the Meraki Console - (https://documentation.meraki.com/General_Administration/Cross-Platform_Content/Blocking_and_Whitelisting_Clients)

# Hotspot 2.0 Configuration

In the Meraki dashboard, configure the SSID and Access Control

1. Log in to the Meraki dashboard
2. Navigate to Wireless -> Access Control and select an SSID
3. Select Enterprise with my RADIUS server as the security type
4. Select none for the splash page
5. Add your assigned RADIUS authentication and accounting servers.

![first](https://www.ironwifi.com/hubfs/image-png-Sep-22-2022-09-17-41-83-PM.png)

#### In the Meraki dashboard, configure Hotspot 2.0

1.  Click on Wireless -> Hotspot 2.0 -> and select the SSID from Step 2.
2.  Activate Hotspot 2.0
3.  Select your venue type and network type, then enter your venue name
4.  To the domain list, add the following:
    1.  ironwifi.net
5.  The following OIs should be added to the Roaming Consortium list:
    1.  AA146B0000
6.  Click on the Add realm button in the section NAI Realms and add the following:
    1.  The format is 0
    2.  Realm name - ironwifi
    3.  Methods - 13: EAP-TLS, 21: PAP, MSCHAP, MSCHAPv2
7.  Save changes

![second](https://www.ironwifi.com/hubfs/image-png-Oct-11-2022-08-35-33-02-PM.png)

Install the Passpoint profile on your client devices

1. Under the Provisioning URL field on the Captive Portal settings page, enter the Operator name
2. Click on the Provisioning URL (OSU). Invite your users to visit this link before arriving to set up their devices for fast, easy and secure network connection.

![third](https://www.ironwifi.com/hubfs/image-png-Oct-11-2022-08-37-16-44-PM.png)

3. Authenticate using one of the available authentication providers

![fourth](https://www.ironwifi.com/hs-fs/hubfs/image-png-Oct-11-2022-08-40-57-60-PM.png?width=430&name=image-png-Oct-11-2022-08-40-57-60-PM.png)

4. Install the Passpoint profile by clicking the button and following the instructions

![fifth](https://www.ironwifi.com/hs-fs/hubfs/image-png-Oct-11-2022-08-41-37-40-PM.png?width=802&name=image-png-Oct-11-2022-08-41-37-40-PM.png)

**Connect to the Hotspot 2.0 network**

1. Using the IronWiFi profile (OperatorName @ IRONWIFI) connect to the network

![sixth](https://www.ironwifi.com/hs-fs/hubfs/image-png-3.png?width=764&name=image-png-3.png)
