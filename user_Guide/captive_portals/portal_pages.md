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
