# Mist Systems

This page explains the necessary configuration for Mist Systems Access Points and external Captive Portal with RADIUS authentication.

**IronWifi Console configuration**

1. Log in to the IronWifi Console
2. From the menu, go to **Network -> Captive Portals -> New Captive Portal**
3. Fill in Name, select **Network**, select **_Mist Systems_** as **Vendor**
4. Copy the Splash Page URL from Captive Portal settings page, e.g. https://us-east1.ironwifi.com/r-umj79-****-****/
5. Add at least one Authentication Provider

**MIST Web GUI configuration**

In the Mist Web GUI, create a Guest WLAN to use your captive portal pages. This action requires an administrator account Network Admin privilege or higher.


- To start, create a new WLAN by navigating to Network -> WLANs and selecting the Add WLAN button on the upper right.

![firstScreenshot](mist/mist1.png)
