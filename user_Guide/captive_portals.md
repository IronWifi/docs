# **Captive Portals**

---

**Name** – Give your Captive Portal a name

**Description** – Provide a description to your Captive Portal

**Network** – The network that this Captive Portal belongs to. These Network's RADIUS servers will authenticate any access requests processed by this Captive Portal.

**Vendor** – Brand of your Access Points or Controller that are used to provide access control for connecting users.

**Splash Page URL** – This is the URL where the Splash page is available. Configure this URL in your Controller settings as External Captive Portal.

**Language** – Language for any internal error and notice messages generated by IronWifi

**On Success Redirect to** – Defines what should happen after successful authentication. We can forward the user to the initially requested URL, the [Success page](https://www.ironwifi.com/captive-portals/portal-pages/), or a predefined external URL. External URL should include the protocol - e.g., https://www.google.com

**Authentication Providers** - a set of authentication methods that should be available on the Splash portal. See [Authentication Providers](https://www.ironwifi.com/captive-portals/authentication-providers/) for more details.

**Splash Page URL** – This is the URL where the Splash page is available. Configure this URL in your Controller settings as External Captive Portal.

**Portal Pages** - these are editable pages that we display to the user in different phases of the authorization process. Further information is available on the [Portal Pages](https://www.ironwifi.com/captive-portals/portal-pages/) page.

**File Library** - upload and manage static files that should be available on a [Portal page](https://www.ironwifi.com/captive-portals/portal-pages/). Use an relative path to refer to uploaded files - eg. ```<img src="./logo.png">``` or ```<link type="text/css"  href="custom.css" />```

**Cloud CDN** - this option will enable [Google Caching](https://cloud.google.com/cdn/docs/caching) by adding required headers to static files served from this Captive Portal

**Client Analytics** - collect detailed information about the visitor's browser; these include screen resolution, OS, language, installed fonts, and more. The gathered information is available in Reports.

 

**MAC-Based Authentication** - allows a user to be re-authenticated based on the client MAC address. MAC address is extracted from the URL and used for automatic authentication the next time the visitor visits the Splash page. This feature allows overriding Session timeout settings of controller that is typically limited to a few hours. List of known and authorized devices is available in the **_Console -> Users -> selected user_**. An administrator can deauthorize any device by clicking on the trash icon, and a visitor can deauthorize his machine on the Returning user page. If you delete a user from the IronWifi console, so will be the Username - MAC address pairing.

**Purchase Confirmation** - Enable to send a confirmation email after successful access purchase

**IP Address Whitelist** - Defines network ranges that are allowed to access this captive portal. Separate individual networks with comma. For example: 127.0.0.1, 10.0.2.0/24. Captive portal will be publicly accessible if you leave this field empty.

**Webhook URL** - We will make a POST request to this URL after every successful authentication. Data will be in JSON format and have these variables:

1. user_type - can be new or existing
2. username
3. logindate or creationdate
4. request_url - splash page URL with parameters added by the Access Point or Controller
5. ap_mac - access points mac address
6. client_mac - mac address of the client device
7. auth_provider_name - used authentication provider
8. captive_portal_name
9. orig_response - data from the client

## Controller Configuration

This section provides information that should be configured in your Controller settings.

**SAML ACS URL** - SAML Assertion Consumer URL, displayed if SAML Authentication Provider is enabled. This URL is part of the Service Provider configuration on your existing Identity Provider.

**SAML Logout URL** - displayed if the SAML Authentication Provider is enabled. This Logout URL is usually optional for Service Provider configuration on your existing Identity Provider.

**Entity Id** - this option is displayed if the SAML Authentication Provider is enabled. Entity Id is a globally unique name for this SAML entity. Configure this Entity Id in Service Provider on your existing Identity Provider.

**RADIUS servers** - provides IP address, port numbers, and the shared secret of Primary and Backup RADIUS servers. These values are the same as displayed in Network details.

**Walled Garden** - this is a list of IP addresses and domains that you should add to the pre-authorization access list on your Controller. Visitors need to be allowed to access these IP addresses and domains for authentication, depending on the selected [Authentication Provider](https://www.ironwifi.com/captive-portals/authentication-providers/). It is recommended to add all displayed networks and domains.

All visitors need to be able to access Splash page URL, hosted by Google and available at 107.178.250.42/32

**Guest Manager** - This section specifies how we will create temporary user accounts during the authentication process. Further information is available on the [Guest Manager](https://www.ironwifi.com/captive-portals/guest-manager/) page.

