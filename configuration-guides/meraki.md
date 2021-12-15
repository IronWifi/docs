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
