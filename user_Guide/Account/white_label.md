# White Label

IronWiFi allows you to white label your landing page URL and emails and get rid of the IronWifi sender, subject, and design on your emails. You can start to build your domain’s email reputation and explicitly show all your recipients that you sent these emails. This should help increase your deliverability rates and reduce your potential for spam reports.

White labeling is critical to your reputation as a sender. Inbox providers distrust messages that are not properly white-labeled, and you will not be able to start building your reputation until you complete the white labeling process.

There are a few quick points worth highlighting before you dive into the white labeling process.

- You can only have one white label per account.
- The email white labeling process requires you to create a SendGrid account and send an email through this account.
- You will have to generate SendGrid API Keys and Transactional templates
- Team members can access the parent white labels or white labels created by other team members if their Role permits.
- We provide all the information about every step of the process below so that you can set up your white label quickly and easily.

## Email White Label Settings

**API token** - The API token used to send email through SendGrid platform.

**Sender Email** - Valid email address that will be included in sent emails. Recipients will reply to this email address.

**Sender Name** - Name as it will be visible in sent emails.

IronWifi sends emails in different situations. The white label allows you to customize all these emails to match your company's standards. If you do not specify Subject or Template Id, default IronWifi subject or template will be used.

## Templates

**Team Member New** - email sent when a new [Team Member](https://www.ironwifi.com/user-guide/team-members/) is invited to the Account. This template is used if a new Team Member does not have an account with IronWifi yet. Email is sent to the Team Member's email address.

**Team Member Existing** - email sent when a new [Team Member](https://www.ironwifi.com/user-guide/team-members/) is invited to the Account. This template is used if a new Team Member already has an account with IronWifi. Email is sent to the Team Member's email address.

**Certificates Link** - email sent to the User when a new authentication certificate is generated. This template is used when the Email link delivery method is chosen during the Certificate generation process.

__LINK__ - will be replaced with a link to download the client certificate

__PASSWORD__ - will be replaced with a generated password needed to install the downloaded certificate

Certificates Attachment - email sent to the User when a new authentication certificate is generated. This template is used when the Email certificate delivery method is chosen during the Certificate generation process.

__PASSWORD__ - will be replaced with a generated password needed to install the attached certificate

Order Confirmation - email sent to the User when Internet Access package is purchased. This email typically contains a generated username and password that can be used to sign-in from a different device.

Your email template can include these two variables

__USERNAME__ - will be replaced with a generated username

__PASSWORD__ - will be replaced with a generated password

You customer can use these credentials to sign in using the [Local Account](https://www.ironwifi.com/captive-portals/authentication-providers/) authentication provider.

 

**Sponsored Access Request** - email sent to the Employee or Access Approver's email address. This email usually contains the requester's name and phone number. The email also includes links to the Approve or Reject access request.

Your email template should include at least these two variables

__APPROVELINK__ - will be replaced with a link to approval access request

__REJECTLINK__ - will be replaced with a link to reject the access request

__REQUESTEXPIRATION__ - will be replaced with a request expiration time in minutes

 

You can have the following additional variables in your email template, and they will be automatically replaced with the information provided by a visitor:

 

__FIRSTNAME__ - first name of the requester

__LASTNAME__ - last name of the requester

__FULLNAME__ - full name of the requester

__COMPANY__

__DEPARTMENT__

__MANAGER__

__PHONE__

__EMAIL__

 
## Hostname White Label Settings

Partners, Resellers, and Enterprise customers can improve their brand by using their domain name for landing pages.

To set up an alias, do the following:

1. Identify the type of hostname that your WiFi vendor requires. You can see the required format in the Captive Portal settings after you select your WiFi Vendor. Depending on the required format, make the following changes to your DNS server settings:

        1. **_splash.YOUR_DOMAIN_**
           - add a CNAME record and redirect host splash.YOUR_DOMAIN to ghs.googlehosted.com
           - ask the IronWifi support team to add your domain alias to Google Apps Engine settings.
           - Cooperate with the support team during the domain validation process
           
        2. **_splash-static.YOUR_DOMAIN_**
           - Add an A record and connect splash-static.YOUR_DOMAIN to 35.184.225.240 (US region), or 35.195.230.167 (EU region), or 35.201.240.80 (Asia Pacific region)
           - generate an SSL certificate for this sub-domain and send both private key and public certificate to the IronWifi support team.
           
        3. **_splashUNIQUE_ID.YOUR_DOMAIN_**
           - Add a CNAME record and redirect splashUNIQUE_ID.YOUR_DOMAIN to ghs.googlehosted.com. UNIQUE_ID is displayed in the Captive Portal settings in IronWifi Console
           - ask the IronWifi support team to add your domain alias to Google Apps Engine settings.
           - cooperate with the support team during the domain validation process
           
2. You can get a valid SSL certificate for free here - https://www.sslforfree.com/
3. Update your WiFi controller with a new URL and test to confirm everything works fine.


