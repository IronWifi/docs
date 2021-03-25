# **Portal Pages**

---

Portal pages are displayed to the users in different authorization phases. Pages can be customized to match the Company design by clicking the Edit button in each row. You can also refer to files uploaded via the File Manager.

To restore the default version of any page, click the Edit button, click the Source button to display page source code, delete all content and save.

**Splash page** - the default Welcome page that is displayed to the user before authentication. You can customize this page as desired, but you have to keep these scripts and DIVs for the page to work properly.

`/assets/js/jquery.js`

`/assets/js/cp-scripts.js`

If you wish to replace the Logo file:

1. upload the file to the File Library - new_logo.jpg for example
2. edit the image path in the Splash page source code - `<img alt="logo" src="new_logo.jpg" style="width: 167px; height: 100px;">`

`<div id="status_placeholder"></div>` - will be replaced with any status messages.

`<div id="error_placeholder"></div>` - will be replaced with an error message generated during authorization.

If you wish to display your own error message -

```
(function(){
	let error_cont = document.getElementById("error_container");
	
	let msg = error_cont.innerHTML;
	
	if(msg == "You are already logged in - access denied") error_cont.innerHTML = "New message"; 
})();
```

Sections for Authentication Providers, each div will be replaced with the source code from Authentication Provider's Container Source Code. Unused DIVs will be replaced with an empty string.

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

You can also use a combination of authentication providers, for example, to provide 30 minutes access and require authentication with a valid voucher after the free access is expired.

```
<div id="voucher_hide" style="display:none">
    <form id="voucher_form" action="" onsubmit="voucherAccess(); return false;" method="post">
.....

<div id="selfregister_hide" style="display:none">
    <div id="error_container" class="alert alert-danger hidden">
        <div id="error_inner_container"></div>
    </div>
    <form id="email_guest_self_registration_submit_form" action="" onsubmit="guestSelfRegUserValidate(); return false;"
          method="post">
.....

<script type="text/javascript">
if (window.location.href.indexOf("error_message") != -1) {
console.log('show voucher');
document.getElementById("voucher_hide").style.display = "block";
}
else {
console.log('show selfregister');
document.getElementById("selfregister_hide").style.display = "block";
}
</script>
```


**Success page** - the Success page that will be displayed to the user if authentication was successful and On Success Redirect to is set to "Success page."

**Returning User page** - the page will be displayed to the user after the guest is authenticated based on the client MAC address. To display this page, MAC-Based Reauthentication must be enabled.

Success page and Returning User page can include forms to allow users to change their password.

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

**Not Found page** - page displayed if the requested content is not available.

**Variables** - You can include the following variables in your pages:

- ${request_id}
- ${fullName}
- ${firstName}
- ${lastName}
- ${phone}
- ${email}
- ${approve_link} - link to approve pending request
- ${reject_link} - link to reject pending request
- ${auth_user}  - generated username
- ${auth_pass}   - generated password
- ${device_mac} - client mac address
- ${redir_url} - target redirect URL
- ${totalData} - total allowed data
- ${usedData} - already used data
- ${availableData} - available data
- ${remainingTime} - session expiration time in human readable form
- ${remainingSeconds} - session expiration time in seconds
- ${language} - language based on client's browser settings
- ${country_code} - country code based on client's source IP address
- ${country} - country based on client's source IP address
- ${city} - city based on client's source IP address
