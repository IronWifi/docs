# **Aruba Instant On** 

---

This page explains the configuration of Aruba Instant On with IronWifi.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Aruba Instant On**

### Access Point Configuration

1. Sign in the [Aruba Instanton portal](https://portal.arubainstanton.com)
2. Sign in the Aruba InstantOn portal - https://portal.arubainstanton.com/
Click on Networks

3. Click on **Networks**
4. Add a new network, usage **Guest**, security **Open**, mark the **Guest portal** checkbox and click **Save**
5. Click on the little arrow next to the newly created network and choose **customize guest portal**

- **Server URL -** {{splash_page_url}}
- **Send RADIUS Accounting -** On
- **Server IP Address -** {{primary_ip}}
- **Shared secret -** {{shared_secret}}
- **Secondary RADIUS Server -** On
- **Server IP Address -** {{backup_ip}}
- **Shared secret -** {{shared_secret}}

 
![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_instant_on/aruba.png)
![second](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_instant_on/aruba2.png)
![third](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_instant_on/aruba3.png)
