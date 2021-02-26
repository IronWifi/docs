# **MikroTik**

---

This page explains the Captive Portal configuration for MikroTik Router OS and authentication with IronWifi.

### **IronWifi console setup**

Sign in to the **IronWifi Console -> Networks** and create a **new Network** to assign a set of RADIUS servers for your network.

Click on Networks -> **Captive Portals** and create a new Captive Portal. Make sure the selected vendor is **MikroTik**. Add an **Authentication Provider** and download the *mikrotik_login.html* file. Rename the downloaded file to *login.html*.



### **MIKROTIK AP SETUP**

Sign-in to your MikroTik configuration interface, usually http://192.168.88.1

Navigate to **Hotspot -> Users** and add a temporary user called user1.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik1.png)

Set a password for this new user.

![secondScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik2.png)

Navigate to **Hotspot -> Servers** and click the **Hotspot Setup** button.

Hotspot Interface: **bridge**

The local address of network: **192.168.89.0/24**

Masquerade Network: **on**

Address Pool of Network: **192.168.89.10 - 192.168.89.254**

Select Certificate: **none**

The access point will redirect you to the default Hotspot Authentication page. Sign in as **"user1"** and return to the Mikrotik configuration interface http://192.168.88.1

Now, the newly created server was assigned the name "hotspot1", which you need to change for the mac address of your access point. Navigate to the quick set (main dashboard) to copy the mac address.

![dashboard](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik_dashboard.png)

After you have copied the mac address, return to the hotspot settings and click on the server named "hotspot1". Then just paste the mac address to the name field and click apply.

![servers](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik_servers.png)

![thirdScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik3.png)

Navigate to **Hotspot -> Server Profiles** and click the newly created profile called **hsprof1**

In the **Login by** section, un-check HTTP CHAP, un-check Cookie and check **HTTP PAP**. Also, check the **Use RADIUS** checkbox.

![fourthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik4.png)

Navigate to **IP -> Hotspot -> Walled Garden IP List** and allow access to the IronWifi global load-balancer - **107.178.250.42**

![fifthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik6.png)

![sixthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik7.png)

In the **MikroTik configuration menu**, navigate down to the **Radius** and click **Add New** to add RADIUS server.

In the Service section, check the **hotspot** checkbox. Enter information about IronWifi RADIUS servers - **IP address, ports, shared secret.** Increase the Timeout value to 1000 ms.

![seventhScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik8.png)

![eightScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik9.png)

Use an FTP client to connect to the access point and navigate to /flash/hotspot (or /hotspot). Create a copy of the login.html file and upload the previously downloaded file **login.html** to the access point.

```
$ ftp 192.168.88.1
(username admin, empty password)
$ cd /hotspot

$ get login.html login.html-backup

$ put mikrotik_login.html login.html
```

![ninthScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/mikrotik/mikrotik10.png)

