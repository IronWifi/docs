# pfSense with Captive Portal

This page explains different configuration scenarios for pfSense Firewall and authentication with IronWifi.

**IronWifi Console configuration**

1. Log in to the IronWifi Console
2. From the menu, go to Network -> Captive Portals -> New Captive Portal
3. Fill in Name, select Network, select pfSense as Vendor
4. Copy the Splash Page URL from Captive Portal settings page, e.g. https://us-east1.ironwifi.com/r-umj79-****-****/
5. Add at least one Authentication Provider

**pfSense Web GUI configuration**

Sign-in to the pfSense Firewall administration console.

![firstScreenshot](pfSense/pfsense1.png)
