# UptimeRobot configuration

Assign: Peter Utekal
Status: Completed

Please follow the steps below to monitor our service yourself in order to reduce the impact of any issues that may arise.

---

1. Set up your own uptime robot to monitor our servers yourself 

    a) Start by navigating to [https://uptimerobot.com/](https://uptimerobot.com/) , then click on the button shown below

    ![UptimeRobot%20configuration/Screenshot_2020-03-23_at_7.42.37_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-23_at_7.42.37_AM.png)

    b) Next, choose the free plan and sign up

    ![UptimeRobot%20configuration/Screenshot_2020-03-23_at_7.43.14_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-23_at_7.43.14_AM.png)

    c) Once you sign up, verify your email address and log in, you should be able to see a dashboard like below.

    ![UptimeRobot%20configuration/Screenshot_2020-03-23_at_7.44.41_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-23_at_7.44.41_AM.png)

    d) Log in to the IronWifi console and create a test user in the users section

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_7.17.41_PM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_7.17.41_PM.png)

    e) Now, navigate to [https://www.ironwifi.com/authentication-test/](https://www.ironwifi.com/authentication-test/) , and input your radius server's ip, port and secret + username and password of your test user

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.33.07_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.33.07_AM.png)

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.34.05_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.34.05_AM.png)

    f) Now, click "Submit query", and copy the URL with parameters

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_7.21.39_PM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_7.21.39_PM.png)

    g) Next, go back to uptime robot dashboard and add a new monitor

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.41.08_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.41.08_AM.png)

    h) Choose monitor type → HTTP(s), type in your desired friendly name and paste the previously obtained URL

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.45.13_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.45.13_AM.png)

    i) Don't forget to tick the box next to your email address so that you get notified, as stated in the picture, you can define new alert contacts in the "My Settings" page (You can get notified by SMS...etc.)

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.48.11_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.48.11_AM.png)

    j) After that, just click "Create Monitor" and see it appear on the left hand side of your screen.

    ![UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.50.21_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-24_at_8.50.21_AM.png)

    k) You can create another monitor for the backup server. Repeat the same process with the other IP address and port from the console (secret stays the same)

    ![UptimeRobot%20configuration/Screenshot_2020-03-23_at_8.00.19_AM.png](UptimeRobot%20configuration/Screenshot_2020-03-23_at_8.00.19_AM.png)

Uptime robot offers an API in case you'd like to display monitoring data in an existing system.