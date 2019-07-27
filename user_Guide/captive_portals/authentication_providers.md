# Authentication Providers

Authentication Providers define how users are allowed to authenticate on a Splash page.

Users will be allowed to use any available authentication method, and the Report will contain information about the authentication provider.

## Add a New Authentication Provider

When your first create a Captive Portal, you do not have any Authentication Providers defined. To add an Authentication Provider, click the “Add New” button at the top of the section. When you finish entering information, click the blue "Add Provider" button at the bottom of the Authentication Providers window.

IronWifi currently supports 11 methods on how to authenticate users via a Splash page:

- Anonymous Access
- Social Login - OAuth 2.0
- SAML 2.0 - Single Sign-On
- Paid Access
- Voucher Code
- Guest Access
- Self Registration
- Local Account
- REST API
- Sponsored Access
- SMS One Time Password

## Anonymous Access

This provider creates a simple Click to Connect button and does not require the user to enter any additional information. It can be used to accept the Terms of Usage.

**INPUTS:**

```tos``` _Accepted Terms of Service_

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/anonymousreg_

[Demo](https://splash.ironwifi.com/api/pages/r-fsum4-zf255-99bid/?mac=01:22:33:44:55:66&url=https://www.ironwifi.com)


## Social Login - OAuth 2.0

It allows the user to sign in with their Social Network account. Supported providers include:

- Google Apps
- Facebook
- Linked In
- Twitter
- Instagram

**Client ID** - IronWifi by default, uses it's own Social Login application when requesting access to the user's social profile. If you create your app with supported Social Login providers, you can enter here your application's Client ID number, and your users will approve access to your use, instead of IronWifi.

**Client Secret** - password linked to the Client ID. You will get this from your OAuth 2.0 provider after you create a new Custom Application with them.

[Demo](https://splash.ironwifi.com/api/pages/r-owzdo5y6/?mac=12:22:33:44:55:66&url=https://www.ironwifi.com)

## SAML 2.0 Single Sign-On

Allows using existing SAML Identity Provider (IdP) to sign in with existing credentials. SAML IdPs confirmed to work with our platform are [Google Apps](https://www.ironwifi.com/user-guide/captive-portals/authentication-providers/apps-saml/), [Okta](https://www.okta.com/), [Ping Identity](https://www.pingidentity.com/en.html), and [Active Directory Federation Services](https://msdn.microsoft.com/en-us/library/bb897402.aspx)

**SSO URL** - Single Sign-On URL provided by your SAML Identity Provider

**IDP Entity ID** - Entity identifier provided by your SAML Identity Provider

**Certificate** - public certificate in PEM format provided by SAML Identity Provider. We use this certificate to verify the SAML message signature.

**TARGET METHOD and URL:**

POST to https://splash.ironwifi.com/api/signin/saml2

[DEMO](https://splash.ironwifi.com/api/pages/1868/?mac=10:22:33:44:55:66&url=https://www.ironwifi.com)


