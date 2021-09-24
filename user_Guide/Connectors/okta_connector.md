# **Okta (Connector)**

---

This page explains the configuration of the IronWifi Okta Connector.

1. In the IronWifi console, navigate to **Users** in the left menu.
2. Click on **Connectors** and create a **new** connector, configure with:

- **Name -** okta2 (or whatever you wish)
- **Database Type -** OKTA
- **Your Okta Domain -** {{your_subdomain}}.oktapreview.com
- **Access Token -** {{your_access_token}}
- **Search Filter -** status eq "ACTIVE"

Click **Continue**.

3. Now choose the group to import

The configuration is now complete.

---

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/okta_connector/auth_provider.png)
![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/okta_connector/okta_group.png)

