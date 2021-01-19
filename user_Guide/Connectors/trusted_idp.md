# **Trusted IdP With ADFS**

---

This topic describes how to configure ADFS and IronWifi to allow users to sign in to the Captive Portal using ADFS as the trusted identity provider (IdP).

 

In ADFS, navigate to **Trust Relationships > Relying Party Trust**, and choose Add Relying Party Trust.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp1.jpg)

IronWifi does not currently support federation Metadata URL, so select the radio button for “Enter the data about relying party manually” and continue.

Display name can be anything.

Select ADFS 2.0 Profile and continue.

On the optional token encryption certificate configuration, skip this step (not required by IronWifi).

Enable support for the SAML 2.0 WebSSO and add the URL: **https://splash.ironwifi.com/api/signin/saml2?acs**

Relying party trust identifier URL is: **https://splash.ironwifi.com/api/signin/saml2?acs**

Permit/deny all user access based on requirements.

Add trust endpoint **https://splash.ironwifi.com/api/signin/saml2?acs** with a binding of “Post” and select finish.

Open the properties for the newly created Relying Party Trust, go to the **Advanced** tab, select SHA-1 for the Secure hash algorithm.

Select **Edit Claim Rules**, for the new trust, and add the rule “Send LDAP attributes as Claims.” Select the LDAP attribute from the Attribute store containing an email for a user. Map this to an outgoing claim type of E-Mail Address.

Create a second rule “Transform an incoming claim.” Configure incoming claim of E-Mail Address to Outgoing claim type Name ID (Format: Email).

You will need to export your Token-signing certificate from ADFS. In ADFS, go to **Service > Certificates**, open the details for the token signing certificate, go to the **Details** tab and select **Copy to File…** You will need to convert this certificate to PEM format for configuration in IronWifi Console (you might use OpenSSL win32 port)

```
openssl x509 -inform der -in adfs.cer -out adfs.pem
```

In IronWifi Console, go to **Networks -> Captive Portals  > Your Portal** to configure your trusted IdP settings. If you have not created an Authentication Provider for this ADFS account, click the **Add New** button.  If you have already created the SAML Authentication Provider, click on edit and enter the URL of the ADFS Federation Service Identifier in the format _http://fully_qualified_domain_name/adfs/services/trust_ to SSO URL.  Under **Certificate**, enter the public key from ADFS in PEM format (include the begin and end certificate tags).

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp2.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp3.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp4.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp5.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp6.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp7.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp8.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp9.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp10.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp11.png)
![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/trusted_idp/idp12.png)



