# **Okta (SAML)**

---

This page explains the configuration of Okta (SAML) in conjunction with IronWifi Captive Portal.

### IronWifi Console Setup

1. Create a **new Captive Portal**.
2. Under authentication providers, click **add new** and choose method **SAML 2.0 Single Sign-On**.
3. Provide your **SSO URL Entity ID**, **Certificate** and **NameIDFormat**.

Click **Create**.

### Okta Setup

1. In Okta interface, navigate to **Applications -> Applications** , and search for _IronWifi_. 
2. Once you open the _IronWifi_ application, click **Add**.
3. Configure general settings with:

- **Application label -** IronWifi CP Demo (or whatever you wish)
- **Do not display application icon to users -** Disabled
- **Do not display application icon in the Okta Mobile App -** Disabled

Click **done**.

4. Configure Advanced Sign On settings with (you need to replace the automatically added value):

- **Base URL -** splash (depending on your region, global - splash, europe-west1 - europe-west1...etc.)

5. After that, assign the newly created application **IronWifi CP Demo** to your users and click Next.


<callout>Your access point's walled garden list must include the following domains</callout>

- *.oktapreview.com
- *.okta.com
- *.okta-emea.com
- *.oktacdn.com

The configuration is now complete.

---

![screen1](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/okta/okta3.png)

![screen1](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/okta/okta5.png)

![screen1](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/okta/okta1.png)

![screen1](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/okta/okta4.png)

![screen1](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/okta/okta2.png)

![screen1](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/okta/okta7.png)
