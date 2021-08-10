# **Ruckus Cloud**

---

This page explains configuration of Captive Portal with authentication through IronWifi for the Ruckus Cloud Controller. 

### IronWifi Console Configuration

1. Create a free _14-day demo account_ [here](https://console.ironwifi.com/register)
2. Once you log in to the console, create a **new network**
3. After that, create a **new captive portal**

### Access Point Configuration

Log in to your ruckus cloud dashboard at [https://cloud.ruckuswireless.com](https://cloud.ruckuswireless.com)

1. Click **Networks** on the left menu and **add a new network**. Use the settings below.

- **Network Name -** Guest Wifi (or anything else) 
- **Type -** Captive Portal

2. Click **Next** and continue the configuration with:

- **Captive Portal Type -** 3rd Party Captive Portal (WISPr)

3. Click **Next** and continue the configuration with:

- **Portal Provider -** IronWifi
- **Captive Portal URL -** *your splash page url from the ironwifi console (Networks -> Captive Portals -> Your Captive Portal)*
- **Integration Key -** *copy and save this key somewhere safe, you will need it*
- **Walled Garden List -** 107.178.250.42

You will also need to include the following domains in the walled garden list  if you want to make use of social login.

**Facebook:** | Twitter | Linkedin | Instagram |
------------- | ------- | -------- | --------- |
*.facebook.com | *.twitter.com | *.linkedin.com | *.instagram.com
*.fbcdn.net | *.twimg.com | *.licdn.net |
*.akamaihd.net |          | *.licdn.com |
connect.facebook.net |     | *.licdn.com |

4. Click **Next** and select which Venue to apply the configuration to. Enable the venue by turning the Activated switch to ON.

If you are asked to select which AP's to apply to, choose All APs unless you have a specific requirement.

5. Click **Next** to confirm settings and then **Create** to finish.

6. In the IronWifi console, under **captive portal settings**, use the following values so that we can connect to your controller

- **Controller username -** api
- **Controller password -** *integration key that you obtained in the 3rd step*
- **Vendor -** Ruckus NBI
