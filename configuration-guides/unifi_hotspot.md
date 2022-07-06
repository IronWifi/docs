# **Ubiquiti Unifi Hotspot**

---

This page explains configuration of Captive Portal with authentication through IronWifi for the Ubiquiti Unifi Controller (hotspot version). 

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Ubiquiti Unifi Hotspot**

### Access Point Configuration

_If you are running UniFi 6.0+ you need to disable the new UI until you've set everything up. To do so, click System Settings on the left menu and disable the New Settings option._

Log in to your UniFi controller and click the **Setting** icon (bottom left).

1. On the left menu, under **Wireless Networks** click **Create New Wireless Network** and configure with:

- **Name/SSID -** Guest WiFi (or whatever you wish)
- **Enabled -** Enabled
- **Security -** Open
- **Guest Policy -** Enabled

Click **Save** to apply.

2. Next, click on **Guest Control** and configure with:

_Under the Guest Policies header_

- **Enable Guest Portal -** Enabled
- **Authentication -** Hotspot
- **Default Expiration -** 8 hours
- **Landing Page -** Promotion URL - {{success_page_url}}
- **Use Secure Portal -** Disabled
- **Redirect using hostname -** Disabled
- **Enable HTTPS Redirection -** Disabled
- **Enable encrypted redirect URL -** Disabled

_Under the Portal Customization header_

- **Template Engine -** AngularJS
- **Override Default Templates -** Enabled

_Under the Hotspot header_

- **RADIUS -** Enabled

_Under the RADIUS header_

3. Profile: click **Create New RADIUS Profile** and configure with:

- **Profile Name -** guestwifi
- **RADIUS Auth Server -** {{primary_ip}}
- **Port -** {{auth_port}} 
- **Password -** {{shared_secret}}

Click **Add Auth Server** and configure with:

- **RADIUS Auth Server -** {{backup_ip}} 
- **Port -** {{auth_port}}  
- **Password -** {{shared_secret}}
- **Accounting -** Enabled
- **Accounting Server -** {{primary_ip}}
- **Accounting Port -** {{acct_port}}

Click **Save** to continue.

- **Authentication type -** CHAP

4. Under the **Access Control -> Pre-Authorization header** enter the following IP address:

- 107.178.250.42

If you wish to support social network logins, you also need to add further IP's as per below for each network you plan to support

_Facebook_
- 31.13.24.0/21
- 31.13.64.0/18
- 45.64.40.0/22
- 66.220.144.0/20
- 69.63.176.0/20
- 69.171.224.0/19
- 74.119.76.0/22
- 103.4.96.0/22
- 129.134.0.0/16
- 157.240.0.0/16
- 173.252.64.0/18
- 179.60.192.0/22
- 185.60.216.0/22
- 204.15.20.0/22

_Twitter_
- 199.16.156.0/22
- 199.59.148.0/22
- 199.96.56.0/21
- 192.133.76.0/22
- 104.244.42.0/24
- 104.244.43.0/24
- 104.244.46.0/24

_LinkedIn_
- 91.225.248.0/23
- 103.20.94.0/23
- 108.174.0.0/22
- 108.174.4.0/24
- 108.174.8.0/22
- 108.174.12.0/23
- 144.2.0.0/22
- 144.2.192.0/24
- 216.52.16.0/23
- 216.52.18.0/24
- 216.52.20.0/23
- 216.52.22.0/24
- 65.156.227.0/24
- 8.39.53.0/24
- 185.63.144.0/24
- 185.63.147.0/24
- 199.101.161.0/24
- 64.152.25.0/24
- 8.22.161.0/24

**NOTE:** These IP ranges are subject to change depending on the social network setup.

Click **Apply Changes** to save.

Next, you will need to modify two html on the controller so that it correctly redirects and authenticates. First of all, download the below two files:

- <a href='https://console.ironwifi.com/api/debug?script=portal_file&unifi_file=index&url={{splash_page_url}}' download>index.html</a>
- <a href='https://console.ironwifi.com/api/debug?script=portal_file&unifi_file=auth&url={{splash_page_url}}' download>auth.html</a>


Open the **index.html** file in a text editor (right click on the file and choose your favourite text/code editor) and at the top of this document you will see an item named "splashurl", edit this so that it shows:

**!This has been done automatically if you opened these instructions from the ironwifi console!**

```javascript
var splashurl = "{{splash_page_url}}";
```

Now, you need to copy these two html files to your UniFi controller hotspot directory. This is typically located at the below location:

- Windows: C:\Users\<username>\Ubiquiti UniFi\data\sites\default\app-unifi-hotspot-portal
- MAC: ~/Library/Application Support/UniFi/data/sites/default/app-unifi-hotspot-portal
- Linux: /usr/lib/unifi/data/sites/default/app-unifi-hotspot-portal
- UDM Pro: /data/unifi/data/sites/default/app-unifi-hotspot-portal
- CloudKey: /srv/unifi/data/sites/default/app-unifi-hotspot-portal

To upload those two files to your controller, you will need an FTP client such as https://winscp.net/ or https://filezilla-project.org/ for macOS/Linux users. This software will enable you to connect to your controller and manipulate with its file system easily.

(replace default in the folder structure with your site name if different)

_If the sites folder is not present, you can created it by simply uploading a floorplan (even a dummy one if required) in the UniFi controller which will create the folder you need._

Finally, you will have to purchase and install a valid SSL certificate on your controller. There are a lot of articles and videos about this topic, here is one - <a href='https://www.youtube.com/watch?v=WxhY71ebc9o'>Unifi SSL installation</a>

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues ! You can purchase certificate for as low as $36.75 /year on this page - <a href='https://affiliates.ssl.com/623.html'>www.ssl.com</a>

 
 Guide on how to install an SSL certificate on Ubiquiti Unifi can be found here - https://www.namecheap.com/support/knowledgebase/article.aspx/10134/33/installing-an-ssl-certificate-on-ubiquiti-unifi/

An SSL certificate can only be purchased for a domain, therefore, you will need to alter your DNS records so that your hostname resolves to the IP address of your controller. After uploading the SSL certificate to your controller, you need to switch on the "redirect using hostname" option.
