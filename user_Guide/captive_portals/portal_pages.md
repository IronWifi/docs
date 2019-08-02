# Portal Pages

Portal pages are displayed to the users in different authorization phases. Pages can be customized to match the Company design by clicking the Edit button in each row. You can also refer to files uploaded via the File Manager.

To restore the default version of any page, click the Edit button, click the Source button to display page source code, delete all content and save.

**Splash page** - the default Welcome page that is displayed to the user before authentication. You can customize this page as desired, but you have to keep these scripts and DIVs for the page to work properly.

**_<script src="/assets/js/jquery.js" />_**

**_<script src="/assets/js/cp-scripts.js" />_**

If you wish to replace the Logo file:

1. upload the file to the File Library - new_logo.jpg for example
2. edit the image path in the Splash page source code - ```<img alt="logo" src="new_logo.jpg" style="width: 167px; height: 100px;">```

_<div id="status_placeholder"></div>_ - will be replaced with any status messages.

_<div id="error_placeholder"></div>_  - will be replaced with an error message generated during authorization.

If you wish to display your own error message -

```
<script>
$(document).ready(function(){
var msg=$("#error_container").html();
if(msg=="You are already logged in - access denied")var msg=$("#error_container").html("New message");
});
</script>
```

Sections for Authentication Providers, each div will be replaced with the source code from Authentication Provider's Container Source Code. Unused DIVs will be replaced with empty string.

```
<div id="anonymousreg_placeholder"></div>

<div id="onetimeaccess_placeholder"></div>

<div id="voucher_placeholder"></div>

<div id="guestselfregister_placeholder"></div>

<div id="selfregister_placeholder"></div>

<div id="localaccount_placeholder"></div>

<div id="google_placeholder"></div>

<div id="facebook_placeholder"></div>

<div id="twitter_placeholder"></div>

<div id="instagram_placeholder"></div>

<div id="linkedin_placeholder"></div>

<div id="fbwifi_placeholder"></div>

<div id="saml_placeholder"></div>

<div id="smsreg_placeholder"></div>

<div id="employeeauth_placeholder"></div>

<div id="hotspot_placeholder"></div>

```



**Success page** - the Success page that will be displayed to the user if authentication was successful and On Success Redirect to is set to "Success page".

**Returning User page** - the page will be displayed to the user after the guest is authenticated based on client MAC address. To display this page, MAC-Based Reauthentication must be enabled.

Success page and Returning User page can include form to allow users change their password.

Sample form:

```
<form action="#" method="post">

<input name="new_password" type="text" />

<input name="request_id" type="hidden" value="${request_id}" />

<input type="submit" />

</form>
```

**Terms & Conditions** - the page describing acceptable usage and Terms & Conditions that the user has to accept before allowing access.

**Pending page** - page displayed to the guest while waiting for Access Authorization by Sponsor.

**Not Found page** - page displayed if requested content is not available.

**Variables** - You can include the following variables in your pages:

- ${request_id}
- ${fullName}
- ${firstName}
- ${lastName}
- ${phone}
- ${email}
- ${approve_link} - for pending approval requests
- ${reject_link} - for pending approval requests
- ${auth_user}  - display generated username
- ${auth_pass}   - display generated password
- ${device_mac} - display client mac address
- ${redir_url} - display target URL
- ${totalData} - total allowed data
- ${usedData} - already used data
- ${availableData} - available data
- ${remainingTime} - session expiration time in human readable form
- ${remainingSeconds} - session expiration time in seconds
- ${language} - based on client's browser settings
- ${country_code} - based on client's source IP address
- ${country} - based on client's source IP address
- ${city} - based on client's source IP address

