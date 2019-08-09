# Users

**Username** – Unique identifier that the user will use for authentication.

**Full Name** – User's first and last name

**E-mail** – User's email address. This email address is used for Certificate delivery if using the TLS authentication method.

**Organizational Unit** – the user is a member of this unit. Every user can be a member of one unit. The user will automatically inherit group membership and all group attributes.

**Authentication Source** – Determines what identity database to use for credential validation. Valid options are:

- **local** - verify using internal password database as defined in IronWifi Console
- **google** - forward request to Google servers for verification
- **rest** - use a REST API to verify provided credentials
- **LDAP** - provided credentials will be tested using external AD/LDAP server

Google, REST, and LDAP authentication sources require the working Connector setup.

**Password** - Clear-Text password that will be stored for local verification

**Status** - User account can be **Enabled** (user can authenticate) or **Disabled** (reject all authentication requests)

**Login Time** - the period when the user is allowed to authenticate. Valid examples: _Wk2305-0855, Sa, Su2305-1655_. Any or Al means all days. All Times are in UTC timezone.

**Creation Date** - when the user account was created.

**Last seen** - last authentication attempt using this username

## Groups

The user can be a member of multiple groups and inherit attributes from these groups. To add a user to a Group, click **Add to Group** button, select Group, and assign Priority. Click **Save** to save this membership information.

**Priority** - determines the order of how the group membership should be evaluated, starting with 1 (highest priority), down to 10 (lowest priority). The evaluation will continue through all groups until a match is found - all Check Attributes match the request. If this happens, group Reply attributes will be added to the Response, and no further Groups will be checked.

## Certificates

IronWifi allows certificate-based authentication using EAP TLS authentication protocol. Every user can have multiple certificates that can be installed on different devices. To generate a certificate, click **Add Certificate** button, select Distribution, and Validity. Click **Create** to generate a new certificate.

**Distribution** - certificates need to be installed on the user's device to work. Three options are available to obtain the generated certificate:

- **Download certificate** - the certificate will be automatically downloaded to the administrator's browser. An import password will be displayed in the pop-up window.
- **Email certificate to the User** - The user will obtain an email with a certificate in the attachment. Import password is included in the email. This method requires the user to have a valid email address.
- **Email download link to the User** - an email is sent to the user with an import password and a link to download the certificate. The certificate can be downloaded only once. A valid email address in the user profile is required to deliver the email.

You can [customize outgoing emails](https://www.ironwifi.com/user-guide/whitelabel/) sent to your users to match with your company brand and style.

## Attributes

Users can have **check** and **reply** attributes. These attributes are used to control session behavior and provide a control mechanism for your NAS controller. Additional attributes can be inherited from the assigned Organizational Unit or Group.

To add an attribute to a user, click **Add Attribute** button. In the pop-up window, you can search for an attribute by name or select a vendor and its attributes.

**Table** - you can select the type of this attribute:

- **check** - received attribute value is compared to the pre-defined value
- **reply** - if check attribute match, this reply attribute is returned to the NAS/Controller for further processing

**Operator** - The following is a list of operators and their meaning.



























