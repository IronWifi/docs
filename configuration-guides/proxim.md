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
- **Session Timeout -** Specifies the time interval after which the session will end automatically.
- **Portal URL -** {{splash_page_url}} 
- **Portal Secret -** {{shared_secret}}
- **User Name/User Password -** Applicable only when using an external portal service provider. 
- **Unique ID -** Applicable only when using an external portal service provider. This information will be auto-populated or provided by an external portal service provider.
- **Primary Radius Server -** {{primary_ip}}
- **Secondary Radius Server -** {{backup_ip}}
- **Radius Shared Secret -** {{shared_secret}}

To configure the hotspot using Web GUI, navigate to **Network Configuration > Hotspot** for Admin users and **Advanced Configuration > Network > Hotspot** for Advanced users.

_Note_:
- Authentication between client and the device is always open
- DNS should be reachable whenever Web Portal or RADIUS Servers or both are configured using Domain Names.
- When the Web Portal or RADIUS Servers or both are unreachable, users cannot access the Internet..

2. When Hotspot 1.0 is enabled, Proxim Access Point operates in Routing Mode with NAT (Network Address Translation) enabled.

4. A DHCP Server is automatically enabled on the LAN interfaces and assigns IP addresses dynamically to the clients connecting to the Access Point. If required, the default IP pools of the DHCP Server can be changed by the Hotspot Operator.

_Note_:
- The first IP address from the DHCP pool is assigned to the LAN interface(s).
- Using the Web GUI, configure the DHCP Pool from Network > Hotspot.

4. Click **Add** in the Hotspot screen, the **Hotspot Walled Garden Table - Add Row** screen appears. Configure the Domain Name i.e. the list of site names to attain direct access.

To configure, add URL(s) or web address (es). For Example: If you add **proxim.com** in the list, you can access any sites like **proxim.com, www.google.com**, etc. directly without being redirected to the login page.

Note: Access to any other site would require the user to login into the portal

Click **OK** and **COMMIT**, to save the configured parameters. **REBOOT** the device, if you have changed any of the parameters marked with an asterisk symbol.



