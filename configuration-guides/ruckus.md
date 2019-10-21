1. Begin by creating a new network with the following attributes

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus1.png)

2. Navigate to **services -> AAA Servers**

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus2.png)

3. Edit **radius1** and input all the necessary information from your console

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus3.png)

4. Next, do the same with **radius1-acct**

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus4.png)

5. After that, edit **remu1** and set **Accounting Server** to **radius1-acct**

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus5.png)

6. Now, navigate to **Hotspot Services** and edit **remu**

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus6.png)

7. Paste your splash page’s URL to the **Login Page** textbox and make sure all your settings are identical to the ones in this picture.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus7.png)

8. After that, add the necessary URLs to your walled garden list

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/ruckus/ruckus8.png)
