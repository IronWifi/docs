# **Azure 2-Factor Authentication**
---
This pge explains the setup of two factor authentication in your Active Directory. This will then enable your users to authenticate with both username/password and sms code or OAuth for better security.

**This configuration guide assumes that you have already followed these instructions to configure your Azure Active Directory users to authenticate through IronWifi**

1. Go to _Azure Active Directory -> Enterprise Applications -> /your application/ -> Conditional Access_

![](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure_2fa/azure.png)

2. Click “New policy” and choose **all users**

![](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure_2fa/azure2.png)

3. Then, choose the desired cloud application, in our case **ironwifi**

![](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure_2fa/azure3.png)

4. After that, click “Grant” and choose **Require multi-factor authentication**, then click select to confirm

![](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure_2fa/azure4.png)

5. Make sure you have the enabled the policy, see the screenshot below. Then just click **Create**

![](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Connectors/azure_2fa/azure5.png)

**Congratulations! You have successfully set up 2-factor authentication in Azure, assuming you have followed the previous instructions, this will now work with your IronWifi authentication**
