# **Authentication Providers**

---

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

## Paid Access

Allows integration with external transaction processing to sell internet access. Available Paid plans are defined in the Hotspot Paid Plans section.

**Transaction Processor** - external credit card processor used to process payments from visitors. Currently supported is Stripe. Any collected payments will go directly to your Stripe account, and IronWifi now does not charge any extra processing fees.

**Secret Key** - authorization token that was provided by your Transaction Processor.

**INPUTS:**

```email``` _[Required]_ Visitor's email address

```card_number``` _[Required]_ Credit card number

```exp_year``` _[Required]_ Credit card expiration year

```exp_month``` _[Required]_ Credit card expiration month

```cvc``` _[Required]_ Credit card security verification number

```name``` _[Optional]_ Cardholder name

```address_line1``` _[Optional]_ Billing address line 1

```address_line2``` _[Optional]_ Billing address line 2

```address_city``` _[Optional]_ Billing address city

```address_state``` _[Optional]_ Billing address state

```address_zip``` _[Optional]_ Billing ZIP code as a string (e.g., "94301")

```address_country``` _[Optional]_ Billing address country

```plan_quantity``` _[Required]_ Number of units of selected plan

```selected_plan``` _[Required]_ ID of the selected plan

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/hotspot_

[DEMO](https://splash.ironwifi.com/api/pages/2034/?mac=17:22:33:44:55:66&url=https://www.ironwifi.com)

## Voucher Code

It allows visitors to sign in with pre-generated voucher codes. These codes can be created manually on the Users page (voucher = user with the same username as password), or you can use our Voucher Generator to generate a set of voucher codes.

**INPUTS:**

```voucher_code``` _[Required]_ Contains voucher code for validation

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/voucher_

[DEMO](https://splash.ironwifi.com/api/pages/r-ufqgh-jruex-v4cuh/?mac=07:22:33:44:55:66&url=https://www.ironwifi.com)


## Guest Access

This method allows you to collect additional information from your Guests. Examples of collected data are full name, phone number, and email address.

**INPUTS:**

```fullname``` Contains guest's full name

```firstname``` Contains guest's first name

```lastname``` Contains guest's last name

```phone``` Contains guest's phone number

```email``` Contains guest's email address

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/guestselfregister_

[DEMO](https://splash.ironwifi.com/api/pages/r-p4vpk-xkxrq-gt6vx/?mac=05:22:33:44:55:66&url=https://www.ironwifi.com)


## Self Registration

It allows the creation of permanent user accounts that can be used to sign on the Splash page. Usually, customers use this method in combination with the "Local Account" authentication provider method.

**INPUTS:**

```username``` _[Required]_ Contains user's username

```password``` _[Required]_ Contains user's password in clear-text

```fullname``` Contains user's full name

```firstname``` Contains user's first name

```lastname``` Contains user's last name

```phone``` Contains user's phone number

```email``` Contains user's email address

 

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/selfregister_

[DEMO](https://splash.ironwifi.com/api/pages/r-xqkwo-rcwhu-xcrkv/?mac=08:22:33:44:55:66&url=https://www.ironwifi.com)


## Local Account

This method requires your users to sign in with an existing account.

**INPUTS:**

```username``` _[Required]_ Contains username for validation

```password``` _[Required]_ Contains password in clear-text for verification

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/localaccount_

[DEMO](https://splash.ironwifi.com/api/pages/r-3nukz-wgogj-sqk9d/?mac=13:22:33:44:55:66&url=https://www.ironwifi.com)


## REST API

The external web server is used to verify the provided information. JSON data will be forwarded to external API endpoint using the POST request method. This request will contain all information submitted by the user, and also parameters from the original request URL. Our communication is authorized using a secret Bearer authentication token.

Users will be authorized if a web server returns a correct response with an HTTP status code value between 200 and 299. If the status code is higher than 299, we decline the access request.

**API endpoint** - web server URL that should receive an authentication request

**API token** - bearer token, if defined, this authentication token will be included with all requests sent to the external web server

**INPUTS:**

We POST all input fields to the external web server. These may include username, password, voucher, email, etc.

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/rest_

[DEMO](https://splash.ironwifi.com/api/pages/r-jjfhz-5b4xb-zzpc9/?mac=18:22:33:44:55:66&url=https://www.ironwifi.com)

Response Status Codes:

2** – return status code indicates success, and the sample body provides user attributes, and access will be approved

```
HTTP/1.1 200 OK
{"valid_until":"2022-06-17T22:26:13","attributes":[{"name":"Acct-Interim-Interval","value":"300"},{"name":"Framed-Protocol","value":"1"},{"name":"Service-Type","value":"2"}]}
```

4** – return status code indicates failure and body provides an error message, and we reject the access request

```
HTTP/1.1 422 Unprocessable Entity
{“errors”:[“Email/login or password incorrect.”]}
```


## Sponsored Access

The visitor will be required to provide the necessary information, and we will send an Access-Request email for approval. The visitor will be authorized after the approver clicks the link contained in the delivered request. This email can be White labeled to match your design.

**Approver's email address** - this is the email address where Access Request emails should be delivered. If not defined, a visitor can enter the email address of the visited person, and an email will be sent to this email address instead. For this to work, an input field with id "eaa_email" needs to be on the Splash page, and a user with the same username or email address has to exist in the IronWifi account.

**Request expiration** - access requests can have an expiration time. You can define the expiration period in minutes, or leave blank if this request should not expire.

**INPUTS:**

```fullname``` visitor's full name

```email``` - visitor's email address

```firstname``` - visitor's first name

```lastname``` - visitor's last name

```phone``` - visitor's phone number

```approver_email``` - Sponsor's email address, domain address, or leave empty. If you define an email address, we will send all requests to this email address. If you set a domain (e.g., @example.com), or multiple domains separated with commas, the guest will have to enter the email address that belongs to one of these domains (e.g., bill@example.com). If you leave this input field empty, the guest can enter any email address, but there has to be a valid user with the same email address defined in Console -> Users.

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/employeeauth_

[DEMO](https://splash.ironwifi.com/api/pages/r-ctz4k-39s9w-smq39/?mac=09:22:33:44:55:66&url=https://www.ironwifi.com)


## SMS One Time Password

We will send a temporary access code to the visitor's phone number. This code will have the format defined in the [Guest Manager](https://www.ironwifi.com/captive-portals/guest-manager/) username section.

**SMS Gateway** - select an external SMS gateway that should be used to send access codes to your visitors. Currently supported are [Twilio](https://www.twilio.com/) and [Clickatell](https://www.clickatell.com/)

**Auth Token** - authentication token used to access the services of an SMS gateway provider. Your SMS gateway provider issues this token.

**Sender's Phone Number** - if supported and configured by your SMS gateway provider, outgoing text messages will appear to be coming from this phone number.

**Country Code** - you can let your users enter the country code in the input field, or you can select a value that we will add to all phone numbers.

**SMS Body** - defines the format of sent text messages. We will replace variable **${sms_code}** with the generated access code.

**Code expiration in minutes** - for security reasons, access codes have an expiration time. The default value is 10 minutes.

**Limit per phone number** - within the "Code expiration in minutes" period, we will send maximum this number of text messages to a provided phone number.

**Limit per client** - within the "Code expiration in minutes" period, we will send maximum this number of text messages from the same connected client device.

**INPUTS:**

Step 1:

```phone_number``` _[Required]_ The user-friendly phone number that should receive the SMS code. If you don't specify a Country Code in Authentication Provider Settings, this number should include a country code.

```prefix``` We will prepend this country code to the phone number.

Step 2:

```sms_code``` _[Required]_ Contains SMS code for validation

```fullname``` - visitor's full name

```firstname``` - visitor's first name

```lastname``` - visitor's last name

**TARGET METHOD and URL:**

POST to _https://splash.ironwifi.com/api/signin/smsreg_

[DEMO](https://splash.ironwifi.com/api/pages/r-s6nwn-ap32o-35f3m/?mac=14:22:33:44:55:66&url=https://www.ironwifi.com)
