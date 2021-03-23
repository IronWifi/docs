# **Cisco Meraki**

---

This page explains the configuration of Cisco Meraki wireless access points for external Captive  Portal and RADIUS server authentication.

Sign-in to the Meraki cloud portal.

![firstScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki1.png?raw=true)

Navigate to **Wireless -> Configure -> SSIDs** and define a network that we will protect with a Captive Portal with RADIUS authentication - Students in this example.

![secondScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki2.png?raw=true)

**Association requirements**: Open (no encryption)

**Splash page**: Sign-on with my RADIUS server

**RADIUS for splash page**: add both servers from the IronWifi console, IP address, Port number and Secret

**Walled garden ranges**: add all Walled garden IP addresses from the IronWifi console

Tip: If you need accounting data and don't see RADIUS Accounting servers, contact Meraki support to enable this feature in your account.

![thirdScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki3.png?raw=true)

Navigate to **Wireless -> Configure -> Splash page** and add **Custom splash URL** from the IronWifi console 

![fourthScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki4.png?raw=true)

For accurate accounting, please enable the **Data-Carrier Detect** feature under the Access Control Page.

If data-carrier detect is enabled, sessions will be revoked and accounted for whenever a client disassociates from a network. To allow clients to reassociate to the network without re-authorization, do not enable data-carrier detect.

If you have devices that don't have support for two way authentication like printers, Smart TV, etc., you can white-list these devices directly in the Meraki Console - (https://documentation.meraki.com/General_Administration/Cross-Platform_Content/Blocking_and_Whitelisting_Clients)

**Identity PSK with RADIUS**

Meraki Documentation - (https://documentation.meraki.com/MR/Encryption_and_Authentication/IPSK_with_RADIUS_Authentication)

![firstScreenshot](https://github.com/IronWifi/docs/blob/master/configuration-guides/meraki/meraki1.png?raw=true)

