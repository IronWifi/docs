# **Aruba Instant On** 

---

This page explains the configuration of Aruba Instant On with IronWifi.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Aruba Instant On**

### Access Point Configuration

1. Click on **Networks**
2. Add a **new network** and choose **Portal** under **Security**
3. Click on the newly created network and choose **customize guest portal**. Configure with:

- **Server URL -** {{splash_page_url}}
- **Send RADIUS Accounting -** On
- **Server IP Address -** {{primary_ip}}
- **Shared secret -** {{shared_secret}}
- **Secondary RADIUS Server -** On
- **Server IP Address -** {{backup_ip}}
- **Shared secret -** {{shared_secret}}

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
 
![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_instant_on/aruba.png)
![second](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_instant_on/aruba2.png)
![third](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_instant_on/aruba3.png)
