# **Extreme Cloud IQ (Hive)**

---

This page explains configuration of Captive Portal with authentication through IronWifi for Extreme Cloud IQ. 

### IronWifi Console Configuration

1. Log in to your ExtremeCloud IQ web interface.
2. Click on `Configuration` at the top and then on `Guided Configuration` on the left.
3. Under `Choose Network Policy` click `New` and configure with:

    - Name: `GuestWiFi`
    - Wireless Access: `Enabled`
    - Switching: `Disabled`
    - Branch Routing: `Disabled`
    - Bonjour Gateway: `Disabled`

4. Click on `Create` to continue.
5. Next to `SSIDs` click `Choose`. Click on `New` and configure with:

    - Profile Name: `guestwifi`
    - SSID: `Guest WiFi` (or whatever you wish)
    - Enabled Captive Web Portal: `Enabled`
    - All other settings can be left at their defaults.

6. Click `Save` and then `OK`.
7. Next, click on `Captive Web Portal` and choose `New`. Configure with:

    - Name: `guestwifi`
    - Registration Type: `External Authentication`

    Under `Captive Web Portal Login Page Settings`:

    - Login URL: {{splash_page_url}}
    - Passwor Encryption: `No Encryption`
    - Authentication Method: `PAP`

    Under `Captive Web Portal Success Page Settings`:

    - Show the success page...: `Disabled`
    - After a successful login: `Redirect to an external page`
    - Use simple URL address: _Your redirect URL_

    Under `Optional Advanced Configuration`:

    - Use network default settings: `Enabled`
    - Use HTTP 302 a the redirection method: `Enabled`
    - Enable HTTPS: `No`

    Under `Walled Garden`:

    IMPORTANT: You will need to add the below entries one by one. Click on `New`, enter the domain and then click `Apply`. Repeat this until you have all domains in the list below.

    - *insert access_domain here*
    - *stripe.com
    - *venuewifi.com
    - *openweathermap.org
    - *cloudfront.net

    If you wish to support social network logins, you also need to add the domains below for each network you plan to support.

    Facebook:

    - *facebook.com
    - *fbcdn.net
    - *akamaihd.net
    - connect.facebook.net

    Twitter:

    - *twitter.com
    - *twimg.com

    LinkedIn:

    - *linkedin.com
    - *licdn.net
    - *licdn.com

    Instagram:

    - *instagram.com

    Weibo:

    - *weibo.com
    - login.sina.com.cn

    VKontakte:

    - *vk.me
    - *vk.com

    Click `Save`.

8. Next, click on `RADIUS Settings` and choose `New`. Configure with:

    - RADIUS Name: `guest`

    Under `Add a New RADIUS Server` configure with:

    - IP Address/Domain Name: {{primary_ip}}
    - Server Type: `Auth/Acct`
    - Shared Secret: {{shared_secret}}
    - Authentication Port: {{auth_port}}
    - Accounting Port: {{acct_port}}
    - Confirm Secret: as above
    - Server Role: `Primary`

    Click `Apply` to add, and then click on `New` to add another:

    - IP Address/Domain Name: {{backup_ip}}
    - Server Type: `Auth/Acct`
    - Shared Secret: {{shared_secret}}
    - Authentication Port: {{auth_port}}
    - Accounting Port: {{acct_port}}
    - Confirm Secret: as above
    - Server Role: `Backup1`

9. Click Apply again, and then click on Save.
10. Under User Profile click on Add/Remove.
11. Select default-profile and click Save.
12. Further down the page, beside Advanced Settings click Edit.
13. Click on Service Settings and beside ALG Services click the Plus (+) icon Configure with:
    - Name: guestwifi
    - DNS: Enabled
    - HTTP: Enabled
14. Click on Save and then Save again at the top right.
15. Finally, click on Continue at the top right.
16. You are now asked which of your access points you wish to push the new settings to (typically all your access points). Select all that apply, and click Update > Update Devices.
17. Click Update.
