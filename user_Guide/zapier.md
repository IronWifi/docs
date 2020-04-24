# Zapier & IronWifi integration

---

Zapier allows you to automate tasks in our console such as user creation or voucher generation. There are thousands of applications that you can seamelessly connect with IronWifi without the need to write a single line of code.

The integration is currently in beta as it has not been officially published, we are working on getting that done as soon as possible. Despite that, you can still start using it today by clicking on the invite link below. Once the integration is officially approved and published by Zapier, your settings will remain in place and you can continue using your zaps as usual.

## Setup

1. Click on this link to become a beta tester, you should see a webpage like below

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier1.png)

2. Scroll down and click "Accept Invite & Build a Zap"

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier2.png)

3. Now, you should see the zapier dashboard in front of you. Click on "Make a New Zap" as shown in the picture below.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier3.png)

4. We will use google sheets for this example, but you can connect IronWifi to any other application available on the Zapier platform. Choose "Google Sheets" from the selection

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier4.png)

5. Now, choose trigger event "New Spreadsheet Row" and click Continue

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier5.png)

6. After that, you'll have to sign in to your google account to authorize google sheets. Do so with any account your want and click continue. Then, you'll be presented with the spreadsheet customization form, choose the spreadsheet and worksheet you prefer like below.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier6.png)

7. In your spreadsheet, you need to use the first row as column labels, these will be zapier variables that you will use later on. Your spreadsheet should look similar to the one below, please note that you can have any number of columns you desire. The highlighted cells will be used as column labels in Zapier.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier7.png)

8. Now, test the trigger in Zapier and check that correct information was obtained in response.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier8.png)

9. Now, let's setup the action. Click done and search "ironwifi", you should see it as in the picture below.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier9.png)

10. Choose the event "Create a User" and click continue.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier10.png)

11. After, that you'll need to authorize your IronWifi account. A window like below should pop up.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier11.png)

12. You need an API key to authorize Zapier to access to your account. Create one in the Account section of our console (https://console.ironwifi.com/account). If you're having trouble with this, email us at support@ironwifi.com and we will help you.

13. Once you have the API key, paste it to the input box and click "Yes, Continue". After you've set up the IronWifi account, click "Continue" again as shown in the picture below.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier12.png)

14. Now, customize the user creation by choosing the value from your spreadsheet like below.

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier13.png)

15. Then, click "Continue" and test the action!

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier14.png)

16. If everything went well, a user with the username of your value from the spreadsheet was created. You can turn on the zap and test it in action if you'd like, or chain more actions to the zap you've already created!

  ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/zapier/zapier15.png)

If you're having trouble with creating your own zaps, or have any other questions do not hesitate to let us know at support@ironwifi.com
