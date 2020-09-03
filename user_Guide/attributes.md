# **Attributes**

---

IronWifi supports thousands of attributes from over 100 vendors.

Two types of attributes are available - Check and Reply and these can be assigned to individual users or groups of users.

## Common Check Attributes

Check attributes are used to compare received value with stored value. If the values match, Reply Attributes will be added to the Response that goes back to the AP/controller.

**SSID**

Called-Station-SSID - check SSID network value

**Data limits**

DATA-Total-Bytes := 1000000 (value in bytes)

DATA-Reset-Type := daily|weekly|monthly|never - how often to reset the counter

**Time limits** - all values should be in seconds

Max-All-Session - the maximum allowed total online time

Max-Daily-Session - maximum allowed daily online time

Max-Weekly-Session - the maximum allowed weekly online time

Max-Quarterly-Session  - the maximum allowed quarterly online time

Max-Yearly-Session - the maximum allowed yearly online time

Expire-After - expire after the first usage

Login-Time - authentication window

**Client Devices**

Max-Devices - total number of client MAC addresses allowed to authenticate with the username

Simultaneous-Use - the maximum number of simultaneous sessions per username

## Common Reply Attributes

Acct-Interim-Interval - how often to send accounting updates to the RADIUS server

Session-Timeout - a period of time after which to disconnect the user

Tunnel-Private-Group-Id - VLAN defining attribute

Egress-VLANID - VLAN defining attribute

WISPr-Bandwidth-Max-Down / WISPr-Bandwidth-Max-Up - speed limit

## Combination of Attributes

It's possible to combines attributes for filtering purpose. For example, if you want to allow users to connect only to SSID1, and not SSID2, do the following.
- create an Organizational Unit
- create Group1 with check attribute Called-Station-SSID
- create Group2 and change the status to Disabled
- assign both groups to the Organizational Unit - Group1 with priority 1 and Group2 with priority 2
- assign your users to the Organizational Unit


![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/attributes/attribute1.png)
![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/attributes/attribute2.png)
