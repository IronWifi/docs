# Azure AD OAuth


This page provides instructions on how to configure your Azure Active Directory to allow Captive Portal authentication with OAuth.

1. Navigate to _https://portal.azure.com_
2. Go to Azure Active Directory submenu

![firstScreenshot](azure_ad_oauth/image4.png)

3. Select the active directory you wish to use for SSO
4. Click on Application Registrations -> New application registration

![firstScreenshot](azure_ad_oauth/image10.png)

5. Enter the name for the new application, type Web app / API, Sign-on URL enter - https://us-west1.ironwifi.com/api/signin/azure (update subdomain with the selected region or use splash for Global), then click **Register**

![firstScreenshot](azure_ad_oauth/image8.png)

6. Copy Application-ID

![firstScreenshot](azure_ad_oauth/image7.png)

7. In the application settings panel, click on **Certificates & secrets**, then add a new client secret and enter description and expiration time. Then simply click add.

![firstScreenshot](azure_ad_oauth/image2.png)

8. Now copy the newly created Client Secret and navigate to **API permissions -> Add a permission -> Microsoft Graph -> Delegated permissions**

![firstScreenshot](azure_ad_oauth/image5.png)

9. From there, enable access to **“Sign users in”** and **“View users’ basic profile”**. Then just click **Add permissions**.

![firstScreenshot](azure_ad_oauth/image6.png)

## Sign in to IronWifi console

1. Click on **Networks -> Captive Portals** and create a new _Captive Portal_. Then click on the newly created Captive Portal

![firstScreenshot](azure_ad_oauth/image3.png)

2. Expand the **Authentication Providers** menu and click **Add New**

![firstScreenshot](azure_ad_oauth/image9.png)

3. Select **Social Login - OAuth 2.0**, provider **Azure**
4. Paste copied Application-ID (Client ID) and Secret Key (Client Secret), then click **create**

![firstScreenshot](azure_ad_oauth/image1.png)




