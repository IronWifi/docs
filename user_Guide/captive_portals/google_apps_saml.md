# Google Apps SAML

This page provides instructions on how to configure your Google Apps account to allow Captive Portal authentication with SAML.

Sign in to your Google Apps / G-Suite administrative console and search for "**saml**." Click **Apps** in the search result.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google1.png)

Click on the **Add a service/App to your domain** button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google2.png)

Click **SETUP MY OWN CUSTOM APP**

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google3.png)

Google IdP Information will be displayed. Click the **DOWNLOAD** button to download public Certificate.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google4.png)

Sign in to the IronWifi Console, navigate to Networks -> Captive Portals -> your captive portal -> Authentication Providers and add new SAML Authentication Provider.

Select SAML 2.0 Single Sign-On methods and add Google Idp SSO URL and Entity ID.

Open downloaded Google public certificate with a text editor, copy content and paste it to the Certificate input field. Click **Create** button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google5.png)

Return to Google Apps administration console and click Next. Enter **Application Name**, Description and click the **Next** button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google6.png)

Return to IronWifi Console and scroll down to the CONTROLLER CONFIGURATION of your Captive Portal.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google7.png)

Copy the **ACS URL** and **Entity ID** from Console and add it the the Service Provider Details configuration. Click Next to continue.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google8.png)

Click the **Finish** button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google9.png)

Click the **OK** button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google10.png)

Click the Settings button available in top right corner and click ON for everyone.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google11.png)

Click **TURN ON FOR EVERYONE** button. This will enable this Service Provider to be used by all members of your domain.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/google_apps_saml/google12.png)




