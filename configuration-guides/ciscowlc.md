#  **Cisco WLC**

---

This page explains the configuration of the Cisco Wireless LAN Controller to work with IronWifi Captive Portal.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Cisco WLC**

### Access Point Configuration

1. Log in to the Cisco WLC Web-Browser interface and go to **Advanced Settings**.

2. Go to **Security -> Access Control Lists** and add **two new ACL rules** permitting connections to the Captive Portal. Get the Captive Portal IP address from your Captive Portal settings -> Walled Garden -> IronWifi

_ACL Rule n. 1_

- **Source -** Any
- **Destination -** 107.178.250.42
- **Netmask -** 255.255.255.255
- **Protocol -** TCP
- **Source port -** Any
- **Dest port -** 443
- **Action -** Permit

_ACL Rule n. 2_

- **Source -** 107.178.250.42
- **Destination -** Any
- **Netmask -** 255.255.255.255
- **Protocol -** TCP
- **Source port -** 443
- **Dest port -** Any
- **Action -** Permit

3. Go to **Security -> Web Auth -> Web Login Page** and configure with:

- **Web Authentication Type -** External (redirect to external server)
- **Redirect URL after login -** Empty
- **External Webauth URL -** {{splash_page_url}}

4. Go to **Security -> RADIUS -> Authentication**, add new RADIUS Authentication Servers and use the following values:

- **Server Address -** {{primary_ip}}
- **Shared Secret Format -** ASCII
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** {{shared_secret}}
- **Key wrap -** Disabled
- **Port Number-** {{auth_port}}
- **Server Status -** Enabled
- **Support for RFC  3576 -** Disabled
- **Server Timeout -** 5 seconds
- **Network User -** Enabled
- **Management -** Enabled
- **Management Retransmit Timeout -** 2 seconds
- **IPSec -** Disabled

5. Go to **Security -> RADIUS -> Accounting**, add new RADIUS Accounting Servers and configure with:

- **Server Address -** {{primary_ip}}
- **Shared Secret Format -** ASCII
- **Shared Secret -** {{shared_secret}}
- **Confirm Shared Secret -** {{shared_secret}}
- **Port Number-** {{acct_port}}
- **Server Status -** Enabled
- **Server Timeout -** 5 seconds
- **Network User -** Enabled


6. Go to **WLANs**, select existing or create new WLAN and open WLAN settings page. Click on the **Security tab, Layer 2** and set:

- **Layer 2 Security -** None

7. Click on the **Layer 3 tab** and configure with:

- **Layer 3 Security -** Web Policy (Authentication)
- **Preauthentication ACL -**  IPv4 - IronWifi-Auth

8. Click on the **AAA Servers tab** and select **IronWifi RADIUS** authentication and accounting servers. You can also set an Interim Interval to 180 seconds or higher.

_Radius Servers_

- **Authetication Servers -** Enabled
- **Server 1 -** IP: {{primary_ip}} , Port: {{auth_port}}
- **Accounting Servers -** Enabled
- **Server 1 -** IP: {{primary_ip}} , Port: {{acct_port}}

_Radius Server Accounting_

- **Interim Update -** Enabled
- **Interim Interval -** 180

Click on the **Save Configuration** link to save and apply new settings.

Finally, change the default virtual controller IP address from 1.1.1.1 to some [other IP address](https://www.cisco.com/c/en/us/support/docs/wireless-mobility/wireless-lan-wlan/213535-wlc-virtual-ip-address-1-1-1-1.html) and install a valid SSL certificate on your controller to prevent warning messages displayed to your clients.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc1.png)

![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc2.png)

![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc3.png)

![fourthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc4.png)

![fifthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc5.png)

![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc6.png)

![seventhScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc7.png)

![eighthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc8.png)

![ninthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc9.png)

![tenthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc10.png)

![eleventhScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc11.png)

![twelfthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/cisco_wlc/wlc12.png)

