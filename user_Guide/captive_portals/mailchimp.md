# MailChimp Integration

Sign in to your MailChimp account, go to your Profile, click on Extras and API keys.

![screen](mailchimp/mailchimp1.png)

Click on the Create A Key and copy generated API key.

![screen](mailchimp/mailchimp2.png)

Sign in to the IronWifi Console, go to Account -> White-label -> Marketing and add the MailChimp token.

![screen](mailchimp/mailchimp3.png)

Go to Captive Portal settings -> Guest Profile and enable the "Add to MailChimp" feature. Select the MailChimp list.

![screen](mailchimp/mailchimp4.png)

![screen](mailchimp/mailchimp5.png)

Test the guest registration process. To add users to your MailChimp list, include checkbox with the name "opt_in", or type "hidden" if you wish to sign up all guests.

```<input type="checkbox" name="opt_in" />```

or

```<input type="hidden" name="opt_in" value="on" />```

![screen](mailchimp/mailchimp6.png)

If an invalid or suspicious email address was entered, an error message will be displayed.

![screen](mailchimp/mailchimp7.png)

Member will be automatically added to the selected MailChimp list.

![screen](mailchimp/mailchimp8.png)





