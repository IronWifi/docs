# **Azure AD SAML**

---

This page provides instructions on how to configure your Azure Active Directory to allow Captive Portal authentication with SAML.

1. Navigate to https://portal.azure.com
2. Go to the Azure Active Directory submenu

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure1.png)

3. Select the active directory you wish to use for SSO
4. Click on Enterprise applications -> New application
5. Click on Non-gallery application, enter the name for new application and click Add

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure2.png)
![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure3.png)

6. In the application settings page, click on Properties

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure4.png)

7. Change "User assignment required?" value to No

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure6.png)

8. In the application settings page, click on Single sign-on -> SAML

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure7.png)

9. Enter Identifier (Entity-ID) and Reply URL. Valid values are displayed in IronWifi Console -> Captive Portal settings. Sample values: Entity ID - https://us-west1.ironwifi.com/api/signin/saml2, Reply URL - https://us-west1.ironwifi.com/api/signin/saml2?acs

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure8.png)

10. Under User Attributes, change User Identifier to user.mail

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure9.png)

11. on the bottom of the screen, click on "Configure your_application_name"
12. copy **SAML Single Sign-On Service URL** value
13. copy **SAML Entity ID** value
14. copy **SAML Signing Certificate - Base64 encoded** content

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure10.png)


## Sign in to IronWifi Console

1. click on **_Networks -> Captive Portals_**
2. create new Captive Portal
3. expand the Authentication Providers menu and click Add New
4. select SAML2 Single Sign-on method
5. paste copied **SAML Single Sign-On Service URL** value to SSO URL
6. paste copied **SAML Entity ID** value to IDP Entity ID
7. paste copied **SAML Signing Certificate - Base64 encoded** content to Certificate
8. select NameIDFormat value  **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/azure_saml/azure11.png)



