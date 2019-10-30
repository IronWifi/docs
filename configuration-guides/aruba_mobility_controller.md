# Aruba Mobility Controller

1. Login to the controller GUI as an admin user. Navigate to **Configuration →  Security → Authentication → Servers tab**. Click on **RADIUS Server** and create a new RADIUS server by entering the new RADIUS server reference name in the empty Add box and clicking **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image34.jpg)

2. Click on **RFC 3576 Server**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image43.png)

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image35.png)

3. Enter the IP address of IronWifi **RADIUS server** in the entry box and click **Add**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image17.png)

4. Click on the IP address of **IronWifi RADIUS** server that appears in the left column under **RFC 3576 Server**.

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image19.jpg)

5. You will be presented with a screen in the right column that looks like this:

![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/configuration-guides/aruba_mobility_controller/image5.png)

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
- **Service:** 
