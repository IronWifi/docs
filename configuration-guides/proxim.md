# **Proxim**

---

This page explains the configuration of Proxim access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Proxim**

### Access Point Configuration

1. Configure the following parameters for hotspot configuration on Proxim devices:

- **Hotspot status -** Specifies the status of the hotspot
- **Session Timeout**: Specifies the time interval after which the session will end automatically.
Portal URL: Specifies the IP or Domain Name of the Captive Web Portal. If the Hotspot operator is using an external portal, the external portal service provider provides this IP or Domain Name.
Portal Secret: Specifies the password of the web server. If the Hotspot operator is using an external portal, the external portal service provider provides this password.
User Name/User Password: Applicable only when using an external portal service provider. 
The Hotspot operator can get this information from an external portal service provider.(Is there any possibility of ironwifi providing username/password mainly for client connection other than regular support).
Unique ID: Applicable only when using an external portal service provider. This information will be auto-populated or provided by an external portal service provider.
Primary Radius Server: Specifies the Radius Server IP or Domain Name. If the Hotspot operator is using an external portal, the external portal service provider provides this Radius Server IP or Domain Name.
Secondary Radius Server: Specifies the fallback Radius Server IP or Domain Name. If the Hotspot operator is using an external portal, the external portal service provider provides this fallback Radius Server IP or Domain Name.
Radius Shared Secret: Specifies the password shared by the radius server. If the Hotspot operator is using an external portal, external portal service provider provides this password.
