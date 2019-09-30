# Peplink

This page explains the necessary configuration for Peplink Access Points and external Captive Portal with RADIUS authentication.

**IronWifi Console configuration**

1. Log in to the IronWifi Console
2. From the menu, go to **Network**, click on **New Network** to create a new network. Click on the network name and copy assigned RADIUS authentication and accounting server IP addresses, port numbers and shared secrets
3. Go to **Captive Portals -> New Captive Portal**
4. Fill in Name, select **Network**, select **_Peplink_** as Vendor
5. Copy the Splash Page URL from Captive Portal settings page, e.g. https://us-east1.ironwifi.com/r-umj79-****-****/
6. Add at least one Authentication Provider

**Peplink configuration**

Sign in to the InControl control panel, find the Access Point -> Settings -> **Remote Web Admin**

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/peplink/peplink1.png)

In the Access Point settings page, click on **Network -> Captive Portal**

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/peplink/peplink2.png)

Enter the values copied from IronWifi console -

- Auth Server, Port, Auth Server Secret
- Accounting Server, Port, Accounting Server Secret
- Splash page - change to External and past the splash page URL

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/peplink/peplink3.png)
