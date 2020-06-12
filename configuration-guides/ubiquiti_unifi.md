*Ubiquiti Unifi

[Purchase more Access Points](https://amzn.to/3cWIPZC)

This page explains different configuration scenarios for Ubiquiti UniFi Controller with IronWifi - Captive Portal and WPA-Enterprise with external RADIUS authentication and accounting.

Configuring UniFi Controller for external Captive Portal authentication

**IronWifi Console configuration**

1. Sign in to the [Management Console](https://console.ironwifi.com)
2. Click on Networks and add a Network
3. Click on Captive Portals and add a Captive Portal
4. In the Captive Portal settings, add Authentication Provider - can be Anonymous for testing purpose
5. IronWifi servers need direct access to your Controller (SW, Cloud Key) so we can authorize connecting devices. Enter the Controller URL or leave blank if the Controller public address is the same as connecting devices IP address (router public IP address). The controller URL should be in this format: - **https://your_public_static_ip:8443**. Make sure it is the PUBLIC IP address, and it's reachable through the Internet (not private address like 192.168.*.*, 172.16.*.*, or 10.*.*.*). You might need to configure port forwarding on your Internet router and firewall. If you are not sure, please consult with your ISP provider.
6. Decide if you want to enable the Use Proxy feature. If enabled, we will be connecting to your controller from static IP addresses 35.184.225.240, or 35.201.240.80, or 35.195.230.167, but the authorization process will be a little slower. If you disable this feature, we will be connecting from dynamic IP range - [https://cloud.google.com/appengine/kb/#static-ip](https://cloud.google.com/appengine/kb/#static-ip) and the client authorization process will be faster.
7. Enter Controller username (administrator privileges, you can create a new user in your controller) and password.
8. Enable Controller monitoring

**Ubiquiti Controller configuration**

1. Sign-in to your Ubiquiti Controller
2. In Wireless network settings change the Security to Open and enable Guest Services
3. Navigate to Guest services settings
4. Select External Captive Portal
5. Enter **107.178.250.42** in the IPv4 address input field
6. Check the Use Secure Portal checkbox
7. Check the **redirect using hostname** checkbox and enter the hostname from the Captive Portal settings page in IronWifi Console - for example, **splashr-bem7i-wud54-re5up.ironwifi.com**
8. Uncheck the Enable HTTPS Redirection
9. Add 107.178.250.42/32 to the Pre-Authorization Access list. If using an external DNS server, add the DNS server IP address to the list.
10. Apply settings and try with your phone or computer

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ubiquiti_unifi/unifi1.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ubiquiti_unifi/unifi2.png)

## Configuring UniFi Controller for WPA-Enterprise

If you wish to have a WPA-Enterprise protected network without Captive Portal, navigate to **Wireless Networks** and change Security to WPA-Enterprise. Enter information about the RADIUS servers, IP addresses, ports, and shared secrets are available in IronWifi Console -> Networks.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ubiquiti_unifi/unifi3.png)

## Common Errors

Captive Portal can return different error codes in the error_message parameter.

- **unifi_authentication_failed** - credentials configured in the Captive Portal settings are probably not valid. Sign in to the Ubiquiti Controller and create a new admin user and password. Configure this username and password in the Captive Portal configuration page in our Console.

 

- **500 Gateway Timeout** or **unifi_gw_connection_failed** - our servers could not connect to your Controller. Make sure the Controller is reachable over the internet, check your firewall settings and port forwarding rules if necessary. The controller should listen on port 8443/TCP.

## Using multiple Captive Portals

1. Create a **New Captive Portal**
2. Replace the Splash page source code with the following code (The source code can be found under Portal Pages in the Captive Portal settings). 
3. Replace the SSID1 and SSID2 with your SSID names. 
4. Replace the splash page URLs with the URLs of the other Captive Portals.

```html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content=""><meta name="author" content="">
<title>Wifi Access</title>
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
  window.location.replace("https://us-east1-r-zzzzzzzzzzzzzzz.ironwifi.com/"+location.search);
}else if (ssid == 'SSID2'){
  window.location.replace("https://us-east1.ironwifi.com/api/pages/r-xxxxxxxxxxxxxxx/"+location.search);
}else{
  window.location.replace("https://us-east1.ironwifi.com/api/pages/r-yyyyyyyyyyyyyyyyyyyyyy/"+location.search);
}
</script>
</head>
</html>

```



