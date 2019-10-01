# MailChimp Integration

Sign in to your MailChimp account, go to your Profile, click on Extras and API keys.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp1.png)

Click on the Create A Key and copy generated API key.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp2.png)

Sign in to the IronWifi Console, go to Account -> White-label -> Marketing and add the MailChimp token.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp3.png)

Go to Captive Portal settings -> Guest Profile and enable the "Add to MailChimp" feature. Select the MailChimp list.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp4.png)

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp5.png)

Test the guest registration process. To add users to your MailChimp list, include checkbox with the name "opt_in", or type "hidden" if you wish to sign up all guests.

```<input type="checkbox" name="opt_in" />```

or

```<input type="hidden" name="opt_in" value="on" />```

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp6.png)

If an invalid or suspicious email address was entered, an error message will be displayed.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp7.png)

Member will be automatically added to the selected MailChimp list.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/mailchimp/mailchimp8.png)





