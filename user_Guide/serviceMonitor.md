# UptimeRobot configuration

Please follow the steps below to monitor our service yourself in order to reduce the impact of any issues that may arise.

---

1. Set up your own uptime robot to monitor our servers yourself 

    a) Start by navigating to [https://uptimerobot.com/](https://uptimerobot.com/) , then click on the button shown below

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor1.png)


    b) Next, choose the free plan and sign up

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor2.png)


    c) Once you sign up, verify your email address and log in, you should be able to see a dashboard like below.

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor3.png)


    d) Log in to the IronWifi console and create a test user in the users section

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor4.png)

    e) Now, navigate to [https://www.ironwifi.com/authentication-test/](https://www.ironwifi.com/authentication-test/) , and input your radius server's ip, port and secret + username and password of your test user

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor5.png)

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor6.png)

    f) Now, click "Submit query", and copy the URL with parameters

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor7.png)

    g) Next, go back to uptime robot dashboard and add a new monitor

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor8.png)

    h) Choose monitor type → HTTP(s), type in your desired friendly name and paste the previously obtained URL

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor9.png)

    i) Don't forget to tick the box next to your email address so that you get notified, as stated in the picture, you can define new alert contacts in the "My Settings" page (You can get notified by SMS...etc.)

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor10.png)

    j) After that, just click "Create Monitor" and see it appear on the left hand side of your screen.

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor11.png)

    k) You can create another monitor for the backup server. Repeat the same process with the other IP address and port from the console (secret stays the same)

    ![firstScreenshot](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/serviceMonitor/monitor12.png)

_Uptime robot offers an API in case you'd like to display monitoring data in an existing system._
