#  Cisco WLC 

This page explains the configuration of the Cisco Wireless LAN Controller to work with IronWifi Captive Portal.

**Cisco WLC configuration**

Log in to the Cisco WLC Web-Browser interface and go to Advanced Settings.

![firstScreenshot](cisco_wlc/wlc1.png)

Go to **Security -> Access Control Lists** and add **two new ACL rules** permitting connections to the Captive Portal. Get the Captive Portal IP address from your Captive Portal settings -> Walled Garden -> IronWifi

- Source: Any, Destination: 107.178.250.42 netmask 255.255.255.255, protocol TCP, Dest port 443, Action: Permit
- Source 107.178.250.42 netmask 255.255.255.255, Destination: Any, protocol TCP, Source port 443, Action: Permit
