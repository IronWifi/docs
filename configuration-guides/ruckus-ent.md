
# **Ruckus Flex**

---


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

## Disabling MAC address encryption

As a security measure, MAC address encryption is enabled by default on the Ruckus infrastructure, which makes it impossible for us to reauthenticate users based on their mac addresses. Here is how you can disable this MAC address encryption.

1. Log into the Ruckus virtual controller CLI as a privileged user and run the following command to validate the status of this security feature.
```
# show running-config encrypt-mac-ip
```
2. Enable the config mode and disable the feature by running the following commands as shown below; You will be prompted to confirm the command execution before proceeding further.
```
# config

(config)# no encrypt-mac-ip
```
3. Confirm that the feature has been disabled by running the following commands from the config mode as shown below.
```
(config)# do show running-config encrypt-mac-ip
```

That's it, now the MAC address encryption is disabled and our mac-based reauthentication feature should work without problem.
