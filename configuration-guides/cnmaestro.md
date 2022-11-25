# **Cambium cnMaestro**

---

This page explains the configuration of Cambium wireless access points for external Captive  Portal and RADIUS server authentication using cnMaestro REST API.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cambium cnMaestro**

### Access Point Configuration

Log in to the Cambium Networks cnMaestro web interface.

1. Navigate to **Network Services > API Clients** and click _Add API Client_, configure with the following values.

- **Name -** IronWifi
- **Description -** Client authorizing guest sessions
- **Expiration Time -** 3600
- **Token Renewal Time -** 1800

Do not forget to copy the **client ID and client secret**, these values need to be added in your captive portal settings.

Controller username = Client ID
Controller password = Client secret

Click **save** to continue.

2. Navigate to **WLANs > Your WLAN** and configure as follows.

- **Type -** Enterprise Wi-Fi
- **Name -** POC CP (or whatever you wish)
- **Description -** empty (or whatever you wish)
- **SSID -** Enabled
- **Mesh -** Off
- **VLAN -** 2
- **Security -** Open
- **Transition SSID -** empty
- **Band -** 2.4GHz, 5GHz, 6GHz
- **Client Isolation -** Local

3. Navigate to **WLANs > Your WLAN > Configuration > AAA Servers** and configure with the following values.

- **1. Host -** {{primary_ip}}
- **Secret -** {{shared_secret}}
- **Port -** {{auth_port}}

- **2. Host -** {{backup_ip}}
- **Secret -** {{shared_secret}}
- **Port -** {{auth_port}}

- **Timeout -** 3
- **Attempts -** 1

4. Navigate to **WLANs > Your WLAN > Configuration > Guest Access** and configure with the following values.

- **Guest Access -** Enabled
- **Portal Mode -** External Hotspot
- **Access Policy -** RADIUS
- **AP Server Protocol -** HTTP
- **Redirect Hostname -** empty
- **WISPr Clients External Server Login -** Enabled
- **External Page URL -** {{splash_page_url}}
- **External Portal Post Through cnMaestro -** Enabled
- **External Portal Type -** Standard
- **Success Action -** Redirect User to External URL
- **Prefix Query Strings in Redirect URL -** Enabled
- **Redirect URL -** {{success_page_url}}

## DHCP Configuration

1. Navigate to **Monitor and Manage > Wi-Fi AP Groups > click on group > Configuration > Network > VLANs**.

![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn8.png)

2. Don't forget to assign the VLAN id to your WLAN at step N.2

![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn7.png)

## Passpoint + OpenRoaming

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/opn1.png)
![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/opn2.png)
![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/opn3.png)
![fourthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/opn4.png)
![fifthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/opn5.png)
![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/opn6.png)

## Screenshots

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn1.png)
![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn2.png)
![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn3.png)
![fourthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn4.png)
![fifthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn5.png)
![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cnmaestro/cn6.png)
