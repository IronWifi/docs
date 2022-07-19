# **Hubspot**

---

Integration with hubspot allows you to gather email addresses automatically to your hubspot list. All you need is an API key from the hubspot platform.

1. Obtain an API key from your hubspot account.
2. Navigate to the accounts page in the ironwifi console and under _Marketing_, find _HubSpot API token_. Paste your API key to this input field.

![hubspot1](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/hubspot/hubspot0.png)

3. In you captive portal settings, enable _Add to HubSpot_.

![hubspot2](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/hubspot/hubspot1.png)

4. If you wish to sign up all your guests, update the Authentication Providers source code and change the opt_in input type from checkbox to hidden and set value to "on"

```html
<input type="checkbox" name="opt_in"/>

change to

<input type="hidden" name="opt_in" value="on"/>
```

5. You can create a new contact in Hubspot with the following information. Your registration form should have the following names for input fields:

* email
* firstname
* lastname
* phone

Contacts can be linked to Hubspot forms by adding the following:

* formId (enter value from your Hubspot form)
* portalId (enter value from your Hubspot form)

```html
<input type="hidden" name="formId" value="*********"/>
<input type="hidden" name="portalId" value="*********"/>
```
