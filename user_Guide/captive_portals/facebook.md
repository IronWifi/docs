# Facebook

This page provides instructions on how to configure your Facebook App to allow Captive Portal authentication with OAuth 2.0.

Go to https://developers.facebook.com/apps and click the **Add a New App** button

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb1.png)

Enter Application Name, Contact Email and select Category. Click Create App ID button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb2.png)

An application dashboard will be displayed. On the bottom of the menu in the PRODUCTS section, click **Add Product** and add **Facebook Login**.

Open Facebook Login Settings page and enable **Client OAuth Login** and Web **OAuth Login**.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb3.png)

Now click on **Settings** under Dashboard to display Application settings page. Click **Add Platform** button on the bottom of the page.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb4.png)

Make sure the Application is live and available to public.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb5.png)

Click on the **Website** button.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb6.png)

Add _https://www.ironwifi.com_ to **Site URL** and _splash.ironwifi.com_ to **App Domains**.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb7.png)

Copy **App ID** and **App Secret** and add it to the Authentication Provider settings in [IronWifi Console](https://console.ironwifi.com).

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb8.png)

Test Splash page authentication, authorize application access to the user profile. Optionally you can change the logo of your application to match your brand and styling.

![firstScreen](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/captive_portals/facebook/fb9.png)

Congratulations. Your guests can now use a Facebook account to authenticate on your Captive Portal.
