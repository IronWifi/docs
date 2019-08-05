# Twilio

This page provides instructions on how to set up a new Twilio account for SMS authentication and use it with IronWiFi Captive Portal.

## Sign Up for Twilio Account

Visit https://www.twilio.com and click on the Sign-Up button.

![firstScreen](twilio/twillio1.png)

Enter your registration details and click **Get Started** button.

![firstScreen](twilio/twillio2.png)

Copy the ACCOUNT SID and AUTH Token, and you will enter it to the Authentication Provider window in the last step.

![firstScreen](twilio/twilio3.png)

Next, we request a new Phone Number that will be used for outgoing SMS messages. In the Phone Numbers Dashboard, click on the **Get Started** button.

![firstScreen](twilio/twilio4.png)

Click on the **Get your first Twillio phone number** button.

![firstScreen](twilio/twilio5.png)

Click on the **Choose this Number** button.

![firstScreen](twilio/twilio6.png)

Copy the new Phone Number and paste it to the  Authentication Providers settings.

![firstScreen](twilio/twilio7.png)

Upgrade your account and add your billing details to pay the provider for the service.

![firstScreen](twilio/twilio8.png)

If you expect to see visitors with international phone numbers, read about [Global SMS](https://support.twilio.com/hc/en-us/articles/223133947-What-is-Global-SMS-and-how-does-it-work-) and enable [Geographic permissions](https://www.twilio.com/console/sms/settings/geo-permissions).

Sign In to the IronWiFi Management Console, click on Networks -> Captive Portals -> New Captive Portal -> Authentication Providers -> Add New. Select SMS Registration Method and Twilio SMS Gateway. Next, enter your Twilio account details and click **Create**.

![firstScreen](twilio/twilio9.png)




