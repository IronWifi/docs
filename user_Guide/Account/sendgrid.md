# **SendGrid account setup**

---

IronWifi is using SendGrid cloud service to deliver emails to its clients and users. As part of the [Whitelabel](https://www.ironwifi.com/user-guide/whitelabel/) feature, you are allowed to prepare your email templates to match your company brand and design.

This page describes the SendGrid registration process and instructions on how to configure your IronWifi account to work with your SendGrid account.

1. Signup for a SendGrid account https://sendgrid.com/pricing/

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid1.png)

2.  Create a new general API key.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid2.png)
![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid3.png)

If you wish to perform email validation, add the required permissions - Reporting (read access) and Validation (full access).

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid4.png)

3. Paste API key into the IronWifi console/account tab.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid5.png)

4. Setup approval email address in IronWifi console (for Employee Authorization only)

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid6.png)

5. From your SendGrid account create a **Legacy** template.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid7.png)
![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid8.png)
![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid9.png)


6. Paste the Id from SendGrid into the account tab of your IronWifi console, in the " sponsored access request " area.

![screen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/sendgrid/sendgrid10.png)

7. If you decided to use your own templates, you have to define your own sender email address and verify the sender identity (https://sendgrid.com/docs/for-developers/sending-email/sender-identity/)

