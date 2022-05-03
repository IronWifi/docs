# **MikroTik**

---

This page explains the Captive Portal configuration for MikroTik Router OS and authentication with IronWifi.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Mikrotik**
4. Download the **mikrotik_login.html** file. Rename the downloaded file to **login.html**

### Access Point Configuration

Sign-in to your MikroTik configuration interface, usually http://192.168.88.1

1. Navigate to **Hotspot -> Users** and add a temporary user called user1 and set a password for this new user
2. Navigate to **Hotspot -> Servers** and click the **Hotspot Setup** button. Configure with:

- **Hotspot Interface -** bridge
- **The local address of network -** 192.168.89.0/24
- **Masquerade Network -** On
- **Address Pool of Network -** 192.168.89.10 - 192.168.89.254
- **Select Certificate -** none

The access point will redirect you to the default Hotspot Authentication page. Sign in as **"user1"** and return to the Mikrotik configuration interface http://192.168.88.1

## !IMPORTANT! : _**Now, the newly created server was assigned the name "hotspot1", which you need to change for the mac address of your access point. Navigate to the quick set (main dashboard) to copy the mac address.**_

3. After you have copied the mac address, return to the **hotspot settings** and click on the server named "hotspot1". Then just paste the mac address to the name field and click **apply**
4. Navigate to **Hotspot -> Server Profiles** and click the newly created profile called **hsprof1**
5. In the **Login by** section, configure with the following values:

- **HTTP CHAP -** un-check
- **Cookie -** un-check
- **HTTP PAP -** check
- **Use RADIUS -** check

6. Navigate to **IP -> Hotspot -> Walled Garden IP List** and allow access to the IronWifi global load-balancer - **107.178.250.42**

- **Enabled -** check
- **Action -** accept
- **Server -** hotspot1
- **Dst. Address -** 107.178.250.42
- **Protocol -** (6) tcp
- **Dst. Port -** 443

7. In the **MikroTik configuration menu**, navigate down to the **Radius** and click **Add New** to add RADIUS server. In the Service section, configure with:

- **Service -** hotspot
- **Address -** {{primary_ip}}
- **Secret -** {{shared_secret}}
- **Authentication Port -** {{auth_port}}
- **Accounting Port -** {{acct_port}}
- **Timeout -** 1000ms

Use an FTP client to connect to the access point and navigate to /flash/hotspot (or /hotspot). Create a copy of the login.html file and upload the previously downloaded file **login.html** to the access point.

```
$ ftp 192.168.88.1
(username admin, empty password)
$ cd /hotspot

$ get login.html login.html-backup

$ put mikrotik_login.html login.html
```

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik1.png)
![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik2.png)
![dashboard](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik_dashboard.png)
![servers](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik_servers.png)
![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik3.png)
![fourthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik4.png)
![fifthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik6.png)
![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik7.png)
![seventhScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik8.png)
![eightScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik9.png)
![ninthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik10.png)
