# SonicWall

This page explains the configuration of SonicWall devices to work with IronWifi Captive Portal and Captive Portal Authentication.

Log in to your SonicWall firewall and click Manage at the top. On the left menu, click on VPN > Base Setting and ensure the Unique Firewall Identifier is the original serial number of the device (as shown on the Licenses page).


Next, click on **Users > Settings** on the left menu and on the Authentication tab at the top configure with:

User authentication method: **RADIUS + Local Users**

Click the Configure RADIUS button. Under the Settings header > RADIUS Servers sub-header click ADD...


On the Settings tab:
```
Host Name or IP Address: **insert primary RADIUS IP here**
Port: **authentication port**
Shared Secret: **insert shared secret here**
Confirm Shared Secret: as above
```

On the Advanced tab:
```
User Name Format: **Name@Domain**
```

Click Save.  Click ADD... again and configure exactly as above with the following change:

```
Host Name or IP Address: **insert backup RADIUS IP here**
```

Click Save again. On the RADIUS Users header:

Default user group to which all RADIUS users belong: **Guest Services**


Finally, click OK to save. Next, on the Accounting tab at the top configure with:

```
Send RADIUS Accounting information: **Enabled**
```

Under RADIUS Accounting Servers click ADD... and configure with:
```
Host Name or IP Address: **insert primary RADIUS IP here**
Port: **accounting port**
Shared Secret: **insert shared secret here**
Confirm Shared Secret: as above
User Name Format: **Name@Domain**
```
Click Save. Click ADD... again and configure exactly as above with the following change:

```
Host Name or IP Address: **insert backup RADIUS IP here**
```

Click Save again.
```
Send accounting data for: **Guest Users**
Include: **Domain and local users**
Send interim updates: **Every 2 minutes**
```
Click Accept at the bottom to save changes. Next, on the left menu click on **Objects > Address Objects** and click Add at the top. Here, you will need to add multiple rules to allow pre-authentication traffic to be permitted. For each of the entries below you need to add a rule as follows, changing the Name and FQDN Hostname each time:
```
Name: **ironwifi**
Zone Assignment: WAN
Type: FQDN
FQDN Hostname: **insert *.ironwifi.com here**
```
Additionally. if you wish to support social network logins, you also need to add the entries below for each network you plan to support.

```
Facebook
*.facebook.com
*.fbcdn.net
*.akamaihd.net
connect.facebook.net
Twitter
*.twitter.com
*.twimg.com
LinkedIn
*.linkedin.com
*.licdn.com
Instagram
*.instagram.com
*.akamaihd.net
```

Once all the required entries are added click on the Address Groups tab and click Add at the top. Enter a name of guestwifi and then for each of the entries you created above click the -> arrow to move them to the right hand box. Click OK to save.



Next, on the left menu click on **Network > Zones** and edit the zone you are using for your guest users (typically the WLAN zone). Under the Guest Services tab configure with:

Enable Guest Services: **Enabled**


Enable the Captive Portal Authentication checkbox and click Configure. Set the following:
```
External Captive Portal Vendor URL: **insert splash page URL here**
Auto Relay Login Credential to SonicWall: **Enabled**
Captive Portal Welcome URL Source: **Custom**
Custom Captive Portal Welcome URL: **insert success page URL here**
Session Timeout Source: **From Radius**
Idle Timeout Source: **From Radius**
Radius Authentication Method: **CHAP**
```
Click OK to save.

Enable the Pass Networks checkbox and select guestwifi from the dropdown. Be sure to also set the Max Guests option to a suitable concurrent number else new guest users might be denied access.

Click OK to save. Finally, if you are using SonicWall Access Points be sure to create an open SSID to enable guest users to connect.
