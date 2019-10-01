# Google Apps

If you want to manage your wireless users using Google Apps account, you can enable remote synchronization with your Google Apps account for users in specific groups and organizational units.

**How to enable Synchronization**

1. [Log in to the Console](https://console.ironwifi.com)
2. From the menu, go to **Users -> Connectors -> New Connector**
3. Fill in Name, select **_Google Apps_** as **Database Type**
4. Type your domain without the http: or www
5. Select Authentication Source:
   - **Google** - will forward authentication requests to Google servers for verification
   - **Local** will verify provided credentials locally - Cleartext-Password attribute, etc.
6. Configure your Google Apps account to allow API access by clicking the link below - [Enable API access](https://support.google.com/a/answer/60757?hl=en).
7. Click to Authorize, and you will receive a unique authorization code.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/google_apps/googlesetup1.jpg)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/google_apps/googlesetup2.jpg)

9. Click Continue
10. In the **Select Group for Import** window, select the **_Organizational Unit_** or **_Group_** that you want to import

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/google_apps/googlesetup3.png)

Every imported user will have a random password generated. Please do not delete these generated passwords. They can be used for authentication if there is some problem with your Google Apps account and deleting the generated password will disable the user's ability to authenticate.

 

**11. Authentication**

You have multiple options on how to authenticate your imported users:

**_Option 1: Authentication using generated password - PEAP_**

During the initial synchronization, we create a random password for every imported user. Use **CSV export** function to export a list of passwords and provide these passwords to your users.

**_Option 2: Authentication using certificate - TLS_**

You can manually create a client certificate for each user and distribute these certificates to your users. Users will be able to authenticate to your network using these certificate.

**_Option 3: Authentication using existing Google account password - TTLS + PAP_**

If your users wish to authenticate using their existing Google passwords, enable [Access for less secure apps](https://www.google.com/settings/security/lesssecureapps) for your Google Apps domain. IronWifi will open a secure connection to Google services and verify provided credentials on Google servers.

**12. Configuring Client Devices**

a. The easiest method is to use our [profile generator tool](https://www.ironwifi.com/wifi-profile-generator/) since as you will see from the below instructions that Windows makes this setup a very cumbersome task

b. If you prefer to do it manually Follow system specific instructions on how to configure your clients:

 - [Windows Clients](https://www.ironwifi.com/windows-clients/)
 - [Android Clients](https://www.ironwifi.com/android-clients/)
 - [Apple iOS, Mac OS X Clients](https://www.ironwifi.com/ios-mac-os-clients/)

**13. 2-Factor Authentication**

If your users have 2-Step Verification enabled in their Google account, you can let them authenticate to network with their username (email address) and App password. To generate an application specific password, do the following:

- go to https://security.google.com/settings/security/apppasswords?pli=1
- Select **Mail**, select your device and click **GENERATE**
- a new app password will be created and displayed. This password (without spaces) can be used for authentication to your WiFi network.
