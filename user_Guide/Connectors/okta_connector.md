# **Okta (Connector)**

---

This page explains the configuration of the IronWifi Okta Connector.

1. Obtain an **API token** - [Okta documentation](https://developer.okta.com/docs/guides/create-an-api-token/overview/)
2. In the IronWifi console, navigate to **Users** in the left menu.
3. Click on **Connectors** and create a **new** connector, configure with:

- **Name -** okta2 (or whatever you wish)
- **Database Type -** OKTA
- **Your Okta Domain -** {{your_subdomain}}.oktapreview.com
- **Access Token -** {{api_token}}
- **Search Filter -** status eq "ACTIVE"

Click **Continue**.

4. Select the **group** you want to import.

The configuration is now complete.

---

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/okta_connector/auth_provider.png)
![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/okta_connector/okta_group.png)

