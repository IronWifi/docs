# **Azure Active Directory**

---

To manage your wireless users using Azure Active Directory account, you can enable remote synchronization with your Azure account for users in specific groups.

1. Log in to the Azure Portal
2.  From the main menu, navigate to **Azure Active Directory > Properties > Tenant ID** Copy the **Tenant ID** value.

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure1.png)

3. From the menu, go to **Azure Active Directory -> App registrations**

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure2.png)

4. Click on **New application registration** 1. Name - ironwifi for example 2. Application type - Web app / API 3. Sign-on URL - [https://www.ironwifi.com](https://www.ironwifi.com/)

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure3.png)

5. Copy the Application ID value.

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure4.png)

6. Click on the link next to **Redirect URIs** button.

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure5.png)

7. Under Redirect URIs, click add and paste this link [https://console.ironwifi.com/api/oauth2callback](https://console.ironwifi.com/api/oauth2callback). If you are using some other region, replace console with the territory, e.g., [us-west1.ironwifi.com](http://us-west1.ironwifi.com/). Don't forget to hit save.

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure6.png)

8. Click on **API permissions** in the left menu and click **Add Permission** 

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure7.png)

9. **API - Microsoft Graph** and **Application Permissions** and **Delegated Permissions** - Read directory data, scroll down for **Directory** → **Directory.Read.All**

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure8.png)

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure9.png)

10. Now, navigate to **Certificates&Secrets** and create a new secret (set duration to never expires). Make sure to copy the value because you can only see it once.

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure10.png)

## IronWifi Console

1. Log in to the IronWifi console
2. Go to Users→Connectors→New Connector
3. Choose a name and pick database type - Azure AD
4. Select Authentication Source: 1. Azure - will forward authentication requests to Microsoft servers for verification 2. Local will verify provided credentials locally - Cleartext-Password attribute, etc.
5. Enter the Tenant identifier value (Directory ID)
6. Enter the Application ID and Application Secret.
7. Click the Continue button, and you will receive a unique authorization code.
8. Click to Authorize, and we will redirect you to the Azure portal for authorization. Approve the request.
9. Click Continue
10. In the **Select Group for Import** window, select the Group that you want to import

![screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure/azure11.png)

Every imported user will have a random password generated. Please do not delete these generated passwords. They can be used for authentication if there is some problem with your Azure account. Deleting the generated password will disable the user's ability to authenticate.

 

**11. Authentication**

You have multiple options on how to authenticate your imported users:

**_Option 1: Authentication using the generated password - PEAP_**

During the initial synchronization, we create a random password for every imported user. Use **CSV export** function to export the list of passwords and provide these passwords to your users. You can also change the generated password manually or use our API.

**_Option 2: Authentication using certificate - TLS_**

You can manually create a client certificate for each user and distribute these certificates to your users. Users will be able to authenticate to your network using these certificate.

**_Option 3: Authentication using existing Azure account password - TTLS + PAP_**

If your users wish to authenticate using their existing Azure credentials, configure your clients to use the TTLS-PAP protocol.

**_Option 4: Authentication using existing Azure account password - PEAP-MSCHAPv2_**

If your users wish to authenticate using their existing Azure credentials and you have AD Domain Services enabled, create an [Azure AD Bridge](https://www.ironwifi.com/azure-ad-authentication-peap-mschapv2/).

 

**12. Configuring Client Devices**

a. The easiest method is to use our [profile generator tool](https://www.ironwifi.com/wifi-profile-generator/) since as you will see from the below instructions that Windows makes this setup a very cumbersome task

b. If you prefer to do it manually Follow system specific instructions on how to configure your clients:

- [Windows Clients](https://www.ironwifi.com/windows-clients/)
- [Android Clients](https://www.ironwifi.com/android-clients/)
- [Apple iOS, Mac OS X Clients](https://www.ironwifi.com/ios-mac-os-clients/)

