# **Ubiquiti Unifi**

---

This page explains different configuration scenarios for Ubiquiti UniFi Controller with IronWifi - Captive Portal and WPA-Enterprise with external RADIUS authentication and accounting.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Ubiquiti Networks**
4. IronWifi servers need **direct access** to your **Controller** (SW, Cloud Key) so we can authorize connecting devices. Enter the **Controller URL** or leave blank if the Controller public address is the same as connecting devices IP address (router public IP address). 

- **Controller URL -** https://your_public_static_ip:8443

Make sure it is the PUBLIC IP address, and it's reachable through the Internet (not private address like 192.168.., 172.16.., or 10...*). You might need to configure port forwarding on your Internet router and firewall. If you are not sure, please consult with your ISP provider.

7. Decide if you want to enable the **Use Proxy feature**. If enabled, we will be connecting to your controller from **static IP** addresses 35.184.225.240, or 35.201.240.80, or 35.195.230.167, but the authorization process will be a little slower. If you disable this feature, we will be connecting from dynamic IP range - https://cloud.google.com/appengine/kb/#static-ip and the client authorization process will be faster.
9. Enter **Controller username** (administrator privileges, you can create a new user in your controller) and **password**.
10. Enable Controller monitoring


### Access Point Configuration

> If you are running UniFi 6.0+ you need to disable the new UI until you've set everything up. To do so, click System Settings on the left menu and disable the New Settings option.

Log in to your UniFi controller and click the Setting icon (bottom left).

1. On the left menu, under **Wireless Networks** click **Create New Wireless Network** and configure with:

- **Name/SSID -** Guest WiFi (or whatever you wish)
- **Enabled -** Enabled
- **Security -**: Open
- **Guest Policy -** Enabled

2. Click **Save** to apply. Next, click on **Guest Control** and configure with:

_Under the Guest Policies header:_

- **Enable Guest Portal -** Enabled
- **Authentication -** External Portal Server
- **Custom Portal -** IPv4 Address 107.178.250.42
- **Use Secure Portal -** Enabled
- **Redirect using hostname -** Enabled - {{splash_page_hostname}}
- **Enable HTTPS Redirection -** Disabled

_Under the **Access Control** header:_

- **Pre-Authorization Access -** 107.178.250.42

### Configuring UniFi Controller for WPA-Enterprise

If you wish to have a WPA-Enterprise protected network without Captive Portal, navigate to **Wireless Networks** and change Security to WPA-Enterprise. Enter information about the RADIUS servers, IP addresses, ports, and shared secrets are available in IronWifi Console -> Networks.

### Common Errors

Captive Portal can return different error codes in the error_message parameter.

- **unifi_authentication_failed** - credentials configured in the Captive Portal settings are probably not valid. Sign in to the Ubiquiti Controller and create a new admin user and password. Configure this username and password in the Captive Portal configuration page in our Console.

- **500 Gateway Timeout** or **unifi_gw_connection_failed** - our servers could not connect to your Controller. Make sure the Controller is reachable over the internet, check your firewall settings and port forwarding rules if necessary. The controller should listen on port 8443/TCP.

### Using multiple Captive Portals

1. Create a **New Captive Portal**
2. Replace the Splash page source code with the following code (The source code can be found under Portal Pages in the Captive Portal settings). 
3. Replace the SSID1 and SSID2 with your SSID names. 
4. Replace the splash page URLs with the URLs of the other Captive Portals.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">
 <meta name="viewport" content="width=device-width, initial-scale=1">

<script>
function getUrlParam(parameter, defaultvalue){
    var urlparameter = defaultvalue;
    if(window.location.href.indexOf(parameter) > -1){
        urlparameter = getUrlVars()[parameter];
        }
    return urlparameter;
}
function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}
var ssid = getUrlParam('ssid', 'none')

if (ssid == 'SSID1'){
  window.location.replace("https://us-east1-r-zzzzzzz.ironwifi.com/"+location.search);
}else if (ssid == 'SSID2'){
  window.location.replace("https://us-east1-r-xxxxxxx.ironwifi.com/"+location.search);
}else{
  window.location.replace("https://us-east1-r-yyyyyyy.ironwifi.com/"+location.search);
}
</script>
</head>
</html>

```
![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ubiquiti_unifi/unifi1.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ubiquiti_unifi/unifi2.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ubiquiti_unifi/unifi3.png)


