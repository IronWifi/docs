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

_RADIUS accounting_

- **1. Host -** {{primary_ip}}
- **1. Port -** {{acct_port}}
- **1. Secret -** {{shared_secret}}
- **2. Host -** {{backup_ip}}
- **2. Port -** {{acct_port}}
- **2. Secret -** {{shared_secret}}
- 
**If you don't see RADIUS Accounting servers, contact Meraki support to enable this feature in your account.**

For accurate accounting, please enable the **Data-Carrier Detect** feature under the Access Control Page.

3. Navigate to **Wireless -> Configure -> Splash page** and configure:

- **Custom Splash URL -** {{splash_page_url}}


If data-carrier detect is enabled, sessions will be revoked and accounted for whenever a client disassociates from a network. To allow clients to reassociate to the network without re-authorization, do not enable data-carrier detect.

If you have devices that don't have support for two way authentication like printers, Smart TV, etc., you can white-list these devices directly in the Meraki Console - (https://documentation.meraki.com/General_Administration/Cross-Platform_Content/Blocking_and_Whitelisting_Clients)

## **Identity PSK with RADIUS**

RADIUS server is queried at association time to obtain a passphrase for a device based on its MAC address

Meraki Documentation - (https://documentation.meraki.com/MR/Encryption_and_Authentication/IPSK_with_RADIUS_Authentication)

Create a **user** and set the username and password to be the client device **MAC address**.

Add a **Tunnel-Password** reply attribute.



---
![firstScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki1.png?raw=true)
![secondScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki2.png?raw=true)
![thirdScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki3.png?raw=true)
![fourthScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki4.png?raw=true)

![ipsk_first](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/Screenshot%202021-03-23%2011.50.50%20AM.png?raw=true)
![ipsk_second](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/Screenshot%202021-03-23%2011.54.06%20AM.png?raw=true)
