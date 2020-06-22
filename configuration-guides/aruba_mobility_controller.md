# **Aruba Mobility Controller**

---

1. Login to the controller GUI as an admin user. Navigate to **Configuration →  Security → Authentication → Servers tab**. Click on **RADIUS Server** and create a new RADIUS server by entering the new RADIUS server reference name in the empty Add box and clicking **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image34.jpg)

2. Click on **RFC 3576 Server**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image17.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image35.png)

3. Enter the IP address of IronWifi **RADIUS server** in the entry box and click **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image19.jpg)

4. Click on the IP address of **IronWifi RADIUS** server that appears in the left column under **RFC 3576 Server**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image5.png)

5. You will be presented with a screen in the right column that looks like this:

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image42.png)

6. You MUST enter the **RADIUS shared key** into the key boxes. Enter _IronWifi RADIUS server shared secret_ in both boxes and click **Apply** at the bottom of the page to save the changes.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image42.png)

7. The next step is to create a new **Server Group for IronWifi**. Click on **Server Group**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image38.png)

8. Enter a reference name for your IronWifi Server Group in the empty box and click **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image36.png)

9. Select the newly created Server Group on the right under Server Group

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image40.png)

10. Click New and select the IronWifi RADIUS server from the previous step.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image27.jpg)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image31.jpg)

11. Click Add Server. Click Apply at the bottom of the page to save the changes.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image20.png)

12. Click on the **L3 Authentication tab**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image33.jpg)

13. Click on Captive Portal Authentication Profile.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image10.jpg)

14. Enter a new Captive Portal profile name in the empty box and click **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image28.jpg)

15. Select the newly created Captive Portal Authentication Profile under Captive Portal Authentication Profile on the right.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image21.jpg)

16. Change the Login page to https://splash.ironwifi.com/api/pages/r-xxxxxxx/ (replacing the URL with the Splash Page URL from IronWifi Console.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image6.png)

17. Click on Server Group under the Captive Portal Authentication Profile and change the Server Group from default to the Server Group that you created for IronWifi in the previous steps and click apply at the bottom of the page to save the changes.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image41.jpg)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image3.png)

18. Navigate to **Configuration → Security → Access Control → User Roles tab**. Click **Add** to create a new User Role. 

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image29.jpg)

19. Enter a name like _CPG--Login_ for the Role Name under Firewall Policies, Click **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image44.png)

20. Choose the radio button for **Create New Policy**, and click the **Create** button

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image7.png)

21. Enter and select the following information:

- **Policy Name:** _CP6-web-ACL_
- **Policy Type:**  _Session_

Click **Add**.


![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image14.jpg)

22. Select and enter the following information for the first line of the ACL:

- **IP Version:** _IPv4_
- **Source:** _User_
- **Destination:** _host_
- **Host IP:** _(the IP address of IronWifi web server: 107.178.250.42)_
- **Service:** _service_
- **Service:** _svc--httt_ (tcp 80)
- **Action:** _Permit_

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image45.png)

23. Click **Add** at the far right underneath this rule

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image4.png)

24. Click **Add** again to add another line to this ACL, identical to the previous line _except_:

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image22.png)

25. Click **Add** at the far right underneath this rule

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image48.png)

26. Click Done (You will be brought back to the Add Role page where you were creating you CPG--Login User Role)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image15.png)

27. Click **Add** under **Firewall Policies**. Select the radio button for **Choose From Configured Policies** and select the policy called **logon-control (session)**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image1.png)

28. Click **Done** in the **Firewall Policies** section. Click **Add** again in the **Firewall Policies** section.Select the radio button for **Choose From Configured Policies** and select the policy called **captiveportal (session)**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image25.png)

29. Click **Done** in the **Firewall Policies** section. Your **Firewall Policy** should look like _this_:

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image26.png)

30. Scroll down this page to the **Captive Portal Profile** section. Select the previously configured Captive Portal Profile from the drop-down list.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image32.jpg)

- Verify that the “Not Assigned” has changed to the name of your Captive Portal Profile.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image37.jpg)

31. Navigate to **Configuration --> Security --> Authentication --> AAA Profiles tab**. Click **Add**, enter a name for the IronWifi Guest Profile, and then click **Add** again.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image30.png)

32. Now in the left column, click on the new profile that you just created. Change the Initial role to the role that you have already created

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image24.jpg)

- **Tech Tip**: On this page you will see an option for RADIUS Interim Accounting. This should be checked if you want live utilization updates in IronWifi Console, usually used to control guest users based on Bandwidth Utilization.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image18.png)

33. Set the subsections of the profile as described below, clicking **Apply** after each change:

- **MAC Authentication Profile:** default

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image46.png)

- **MAC Authentication Server Group:** _(Your IronWifi Server Group)_

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image47.jpg)

- **RADIUS Accounting Server Group:** _(Your IronWifi Server Group)_

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image2.png)

34. Click on **RFC 3576** for this AAA Profile.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image8.png)

35. From the **Add a profile** list, select the IP address of your IronWifi RADIUS server and click **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image23.png)

Click **Apply** to save these settings

Repeat Creating AAA Profiles for the IronWifi Guest and 802.1x SSID, to create the AAA Profile for the 802.1x SSID. The only difference is that this AAA Profile will have 802.1x settings but no MAC Authentication Profile. See example below:


![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image11.jpg)

36. The next step is to associate our 802.1x SSID and Guest SSID with the AAA Profiles we just created. Navigate to **Configuration --> Advanced Services --> All Profiles**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image16.png)

37. Expand the **Wireless LAN** section.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image9.png)

38. Expand the **Virtual AP profile** and locate your _Guest_ and _802.1x SSID_ profiles.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image39.png)

39. Modify _each_ Virtual AP profile to use the appropriate AAA Profile that you created in the previous section. Make sure to click **Apply** after each change.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image12.jpg)

40. Click the **Save Configuration** button at the top of the page once the changes are completed.
