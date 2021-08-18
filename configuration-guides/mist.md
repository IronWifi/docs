# **Mist Systems**

---

This page explains the necessary configuration for Mist Systems Access Points and external Captive Portal with RADIUS authentication.

### **IronWifi Console Configuration**

1. Log into the IronWifi console or **[register for free](https://console.ironwifi.com/register)**
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Mist Systems**

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
