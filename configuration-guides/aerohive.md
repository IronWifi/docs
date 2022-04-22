# **Aerohive (HiveManager)**

---

This page explains the Captive Portal configuration for HiveManager and authentication with IronWifi.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Aerohive**

### Access Point Configuration

_Please note: You need to be running HiveManager 6.4r1 or above in order to continue. Earlier versions are not supported._

Log in to your HiveManager web interface

Click on **Configuration** at the top and then on **Guided Configuration** on the left.

Under **Choose Network Policy** click **New** and configure with:

- **Name -** GuestWifi
- **Wireless Access -** Enabled
- **Switching -** Disabled
- **Branch Routing -** Disabled
- **Bonjour Gateway -** Disabled

Click on **Create** to continue
 
Next to **SSIDs** click **Choose**. Click on **New** and configure with:

- **Profile Name -** guestwifi
- **SSID -** Guest Wifi (or whatever you want)
- **Enabled Captive Web Portal -** Enabled

All other settings can be left at their defaults.

Click **Save** and then **OK**

Next, click on **<Captive Web Portal>** and choose **New**. Configure with:
  
- **Name -** guestwifi
- **Registration Type -** External Authentication

Under **Captive Web Portal Login Page Settings**:
  
- **Login URL -** {{splash_page_url}}
- **Password Encryption -** No encryption
- **Authentication Method -** PAP
  
Under **Captive Web Portal Success Page Settings**:
 
- **Show the success page... -** Disabled
- **After a successful login -** Redirect to an external page
- **Use a simple URL address -** {{success_page_url}}
  
Under **Optional Advanced Configuration**:

- **Use network default -** Enabled
- **Use HTTP 302 a the redirection method -** Enabled
- **Enabled HTTPS -** No
  
Under **Walled Garden**:

107.178.250.42
  
If you need to load resources from external servers (SAML, social login), you will need to add other entries as well, instructions to configure the walled garden list in this case are available [here](https://ironwifi.com/walled-garden-list-guide).

Click **Save**

Next, click on **<RADIUS Settings>** and choose **New**. Configure with:

- **RADIUS Name -** guest
  
Under **Add** a **New RADIUS Server** configure with:
  
- **IP Address / Domain Name -** {{primary_ip}}
- **Server Type -** Auth/Acct
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}
- **Server Role -** Primary
  
Click **Apply** to add, and then click on **New** to add another:

- **IP Address / Domain Name -** {{backup_ip}}
- **Server Type -** Auth/Acct
- **Shared Secret -** {{shared_secret}}
- **Confirm Secret -** {{shared_secret}}
- **Server Role -** Backup1
  
Click **Apply** again, and then click on **Save**
 
Under **User Profile** click on **Add/Remove**.

Select **default-profile** and click **Save**

Further down the page, beside **Advanced Settings** click **Edit** 

Click on **Service Settings** and beside **ALG Services** click the **Plus (+) icon**  Configure with:
  
- **Name -** guestwifi
- **DNS -** Enabled
- **HTTP -** Enabled
  
Click on **Save** and then **Save** again at the top right.
 
Finally, click on **Continue** at the top right.

You are now asked which of your access points you wish to push the new settings to (typically all your access points). Select all that apply, and click **Update > Update Devices**

Click **Update**.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
