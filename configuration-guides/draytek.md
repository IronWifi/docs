# **Draytek Vigor Series**

---

This page explains the configuration of Draytek Vigor Series wireless access points for external Captive  Portal and RADIUS server authentication.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **Draytek Vigor Series**

### Access Point Configuration

**NOTE:** The current supported models are: 2862, 3220, 2926, 2952, 2765, 2865, 2866, 2927, 2962, 3910 series.

Log in to your Draytek Web Interface and click Hotspot Web Portal &gt;&gt; Profile Setup on the left menu.

Click an available Index, i.e. **1** and configure with:

- **Enable this profile**: Yes
- **Portal Method**: External Server
- **Captive Portal URL**: {{splash_page_url}}
- **Redirection URL**: <http://portal.draytek.com>
- **Authentication Method**: Click External RADIUS Server and set:  
    \- **Enable**: Yes  
    \- **Server IP Address**: {{primary_ip}}  
    \- **Destination Port**: 1812  
    \- **Shared Secret**: {{shared_secret}}  
    \- **Confirm Shared Secret**: as above  
    \- **Enable Accounting**: Yes  
    \- **Accounting Port**: 1813  
      
    Click **OK** to Save
- **MAC Address Format**: AA-BB-CC-DD-EE-FF

Click **Save and** **Next**. Now, click the **Dest Domain tab** and add the following entries, one per index:

\*.\*insert access\_domain here\*

\*.cloudfront.net

\*.venuewifi.com

\*.openweathermap.org

**If you wish to support social network logins, you also need to add further domains as per below for each network you plan to support**

<table cellspacing="1"><tbody><tr><td style="width: 27.7568%;">**Facebook**  
</td><td style="width: 71.863%;">\*.facebook.com  
\*.fbcdn.net  
\*.akamaihd.net  
connect.facebook.net  
  
</td></tr><tr><td style="width: 27.7568%;">**Twitter**  
</td><td style="width: 71.863%;">\*.twitter.com  
\*.twimg.com  
  
</td></tr><tr><td style="width: 27.7568%;">**LinkedIn**  
</td><td style="width: 71.863%;">\*.linkedin.com  
\*.licdn.com  
  
</td></tr><tr><td style="width: 27.7568%;">**Instagram**  
</td><td style="width: 71.863%;">\*.instagram.com  
\*.akamaihd.net  
  
</td></tr><tr><td style="width: 27.7568%;">**Weibo**  
</td><td style="width: 71.863%;">\*.weibo.com  
\*.sina.com.cn  
  
</td></tr><tr><td style="width: 27.7568%;">**VKontakte**  
</td><td style="width: 71.863%;">\*.vk.me  
\*.vk.com  
  
</td></tr></tbody></table>

Click **Save and Next** then configure with:

- **Expired Time After Activation**: 0 days 6 hours 0 min (or whatever you wish)
- **HTTPS Redirection**: No
- **Captive Portal Detection**: Yes
- **Landing Page After Authentication**: {{success_page_url}}
- **Applied Interfaces**: Select which SSID(s) you wish to enable the service on

Click **Finish** to Save. **Please ensure you reboot the router before continuing as this is a pre-requisite for the setting to apply.**