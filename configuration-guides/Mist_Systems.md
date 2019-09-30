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

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/MIST/mist1.png)


- Under the **Security** section, select the desired WLAN security mode
- Go to the **Guest Portal** box and select **Forward to the external portal**.  Here, please provide the **Splash page URL** that you copied from our Captive Portal settings page.
- Enter the IP **107.178.250.42/32** to Allowed Subnets input field.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/MIST/mist2.png)


- Click **Create** to create the new WLAN on your site. The API Secret will automatically be created for you.
- Return to the WLAN settings page and copy the **API Secret**.
- Go back to the IronWifi console and paste the API Secret to **Controller Password** on the Captive Portal settings page.
