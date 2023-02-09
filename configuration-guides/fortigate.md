# **Fortigate**

---

This page explains the Captive Portal configuration for Fortigate hardware and authentication via IronWifi.

### IronWifi Console Configuration

1. Log into the IronWifi console or [register for free](https://console.ironwifi.com/register)
2. Create a **new network**
3. After that, create a **new captive portal**, with vendor **FortiGate**

### Access Point Configuration

!_IMPORTANT: You need FortiOS v5.6 or above in order to proceed._!

Please log in to your FortiGate web interface and click **User & Device > RADIUS Servers** on the left menu. Click **Create New** and configure with:

- **Name -** guestradius
- **Primary Server -** {{primary_ip}}
- **Primary Shared Secret -** {{shared_secret}}
- **Secondary Server -** {{backup_ip}}
- **Secondary Shared Secret -** {{shared_secret}}
- **Authentication Method -** Specify
- **Method -** PAP

Click **OK** to **Save**.

Next, you will need to configure custom RADIUS authentication port. This can be done in the CLI interface.

More information: https://docs.fortinet.com/document/fortigate/7.2.3/administration-guide/759080/configuring-a-radius-server

config system global
    set radius-port <integer> 
end

Next, click on **User Groups** and **Create New**. Configure with:

- **Name -** guestgroup
- **Type -** Firewall

Under **Remote groups** click **Create New** and under **Remote Server** choose **guestradius**. Click **OK** to **Save**.

Next, click **Policy & Objects > IP**. Click **Create New > Address**. Configure with:

- **Category -** Address
- **Name -** guestonline
- **Type -** IP/Netmask
- **Subnet / IP Range -** 10.1.0.0/255.255.255.0
- **Interface -** any
- **Show in Address List -** Enabled

Click **OK** to **Save**. Next, click **Create New > Address** again and configure with:

- **Category -** Address
- **Name -** Your splash page's hostname
- **Type -** FQDN
- **FQDN -** Your splash page's hostname

Click **OK** to **Save**.

Next, under **Addresses** click **Create New > Address Group**. Configure with:

- **Category -** IPv4 Group
- **Group Name -** guestwhitelist
- **Members -** click the + button and select all the domains you added earlier.

Click **OK** to **Save**.

Next, click **WiFi & Switch Controller > SSID** on the left. Click **Create New > SSID**. Configure with:

- **Interface Name -** guestwifi
- **Type -** WiFi SSID
- **Traffic Mode -** Tunnel to Wireless Controller
- **Address -** 10.1.0.1/255.255.255.0
- **DHCP Server -** Enabled
- **DNS Server -** Specify: 8.8.8.8
- **SSID -** Guest WiFi (or whatever you wish)
- **Security Mode -** Captive Portal
- **Portal Type -** Authentication
- **Authentication Portal -** External: {{splash_page_url}}
- **User Groups -** guestgroup
- **Broadcast SSID -** Enabled
- **Block Intra-SSID Traffic -** Enabled
- **Redirect after Captive Portal -** Specific URL: {{success_page_url}}

Click **OK** to **Save**. Next, under **IPv4 Policy click Create New**. Configure with:

- **Name -** guestwifi
- **Incoming Interface -** Guest WiFi (guestwifi)
- **Outgoing Interface -** wan1 (your WAN connection)
- **Source -** all
- **Destination Address -** guestwhitelist
- **Schedule -** always
- **Service -** ALL
- **Action -** ACCEPT
- **Enable this policy -** Enabled

Click **OK** to **Save**. Click **Create New** again and configure with:

- **Name -** guestwifionline
- **Incoming Interface -** Guest WiFi (guestwifi)
- **Outgoing Interface -** wan1 (your WAN connection)
- **Source -** guestonline
- **Destination Address -** all
- **Schedule -** always
- **Service -** ALL
- **Action -** ACCEPT
- **Enable this policy -** Enabled

Click **OK** to **Save**.

The configuration is now complete.

 ! You must also install a valid SSL certificate on your controller/AP, in order to avoid authentication issues !
