# **SonicWall**

---

This page explains the configuration of SonicWall devices to work with IronWifi Captive Portal.

### Assumptions

1. SonicWall Access Point is set up and running the latest firmware.
2. DHCP and DNS are appropriately configured.
3. IronWifi initial setup is complete. This setup includes Network and Captive Portal settings.
4. SonicWall Access Point can communicate with IronWifi servers.
5. The Guest SSID VLAN can communicate with IronWifi servers.
6. All systems are appropriately licensed.

### Instructions

Sign in to SonicWall Administration Interface. Click Network, click Zones and click the WLAN edit button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/sonic_wall/sonicwall1.png)

Leave the "General" options default and click **Guest Services**

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/sonic_wall/sonicwall2.png)

Check **Enable Guest Services** and check **Enable External Guest Authentication**. Change the Max Guests value to **255**.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/sonic_wall/sonicwall3.png)

Select **HTTP** client Redirect Protocol.

Under "Web Server," select **HTTPS** protocol and create a new object for Splash page - FQDN hostname from Console - e.g., splash-static.ironwifi.com, st-us-east1.ironwifi.com, splash-static-eu.ironwifi.com, etc.., zone DMZ.

Enter **443** as the Port Number.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/sonic_wall/sonicwall4.png)

Select **Auth Pages** tab and enter "/api/pages/xxxxxx/" to all input fields. "xxxxxx" is your Splash page identifier, from Console.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/sonic_wall/sonicwall5.png)

Review other settings and click **OK** to save Changes.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/sonic_wall/sonicwall6.png)

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/sonic_wall/sonicwall7.png)

The last step is to Allow remote connections on your Firewall. IronWifi needs to be able to connect to the SonicWall Guest Services to authorize connected clients. Guest Services are listening on port 4043 and IronWifi will try to connect to the URL in this format:

https://SOURCE_IP_ADDRESS:4043

* SOURCE_IP_ADDRESS - IP address that we have received the authentication request from

We will be connecting directly from the web server, so no further changes are required in your SonicWall firewall rules.\

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

## Common Errors

IronWifi needs to be able to connect to your Access Point to authorize the connecting device. If not successful, the Captive Portal will return different error codes in the error_message parameter.

- **sonicwall_gw_connection_failed** - our servers could not connect to your SonicWall AP. Make sure the Access Point Guest Services port is reachable over the internet, check your firewall settings and port forwarding rules if necessary. The Guest Services service is listening on port 4043/TCP by default, and you can override this value using the Controller URL parameter in the Captive Portal settings in our Console.
