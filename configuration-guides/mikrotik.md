
# MikroTik

This page explains the Captive Portal configuration for MikroTik Router OS and authentication with IronWifi.

#### IRONWIFI CONSOLE SETUP

Sign in to the **IronWifi Console -> Networks** and create a **new Network** to assign a set of RADIUS servers for your network.

Click on Networks -> **Captive Portals** and create a new Captive Portal. Make sure the selected vendor is **MikroTik**. Add an **Authentication Provider** and download the *mikrotik_login.html* file. Rename the downloaded file to *login.html*.


#### MikroTik AP Setup

Sign-in to your MikroTik configuration interface, usually http://192.168.88.1

Navigate to **Hotspot -> Users** and add a temporary user called user1.