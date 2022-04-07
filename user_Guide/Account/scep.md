# **SCEP with Intune**

---

The Simple Certificate Enrolment Protocol (SCEP) is a protocol that allows devices to easily enroll for a certificate by using a URL and a shared secret to communicate with a PKI. The following instructions explain how to set up SCEP and IronWifi with Microsoft Intune.

### What do you need ?

- **owner_id -** owner id is a unique identifier of your ironwifi account that can be found in the URL when you're logged in, it should look similar to this - 1759e87912345678
- **CA Certificate Self-Signed -** This can be downloaded from [this link](https://console.ironwifi.com/assets/html/ironwifi.crt) or from within the IronWifi console, under **Account**
- **CA Certificate Trusted -** This can be downloaded from [this link](https://console.ironwifi.com/assets/html/ironwifi_comodo.crt) or from within the IronWifi console, under **Account**
- **SCEP Server URL -** https://{{region}}.ironwifi.com/api/{{owner_id}}/certificates

**!Note!** Your users must exist in the ironwifi console or the user autocreation needs to be enabled for this to work

1. Create a new Trusted Certificate profile with the following configuration options:

- **Certificate file -** ironwifi.crt
- **Destination store -** Computer certificate store - Root

2. Create a new Trusted Certificate profile with the following configuration options:

- **Certificate file -** ironwifi_comodo.crt
- **Destination store -** Computer certificate store - Root

3. Create a new SCEP certificate profile with the following configuration options:

- **Profile Type -** SCEP Certificate
- **Certificate type -** User
- **Subject name format -** CN={{SerialNumber}},O={{owner_id}},L={{region}}
- **Subject alternative name -** Email address = {{UserPrincipalName}}
- **Certificate validity period -** 10 Days
- **Key storage provider (KSP) -** Enroll to Software KSP
- **Key usage -** Key encipherment, Digital signature
- **Key size (bits) -** 1024
- **Hash algorithm -** SHA-1, SHA-2
- **Root Certificate -** _Your trusted certificate created in the first step_
- **Extended key usage -**

Name | Object Identifier | Predefined values |
----- | ---------------- | ----------------- |
Client authentication | 1.3.6.1.5.5.7.3.2 | Client Authentication

- **Renewal threshold (%) -** 20
- **SCEP Server URLs -** https://{{region}}.ironwifi.com/api/{{owner_id}}/certificates/scep

4. Create a new Wi-Fi profile with the following configuration options:

- **Profile Type -** Wi-Fi
- **Connect to more preferred network if available -** No
- **Wi-Fi type -** Enterprise
- **Wi-Fi name -** _Your SSID_
- **Connection name -** _Your connection name_
- **Connect automatically when in range -** Yes
- **Connect to this network, even when it is not broadcasting its SSID -** Yes
- **Metered Connection Limit -** Unrestricted
- **Force Wi-Fi profile to be compliant with the Federal Information Processing Standard (FIPS) -** No
- **Company proxy settings -** none
- **Single sign-on (SSO) -** Disable
- **EAP type -** EAP - TLS
- **Certificate server names -** radius.ironwifi.com, IronWifi Server Certificate
- **Root certificates for server validation -** _The trusted certificate created in the second step_
- **Authentication method -** SCEP certificate
- **Client certificate for client authentication (identity certificate) -** _Your SCEP certificate created in the second step_

You should now see 3 profiles under **Devices** in your **Microsoft Endpoint Manager admin center**

In Microsoft Intune, your settings should look like below.


![test](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/scep/scep1.png)
![test](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/scep/scep2.png)
![test](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/scep/scep3.png)
![test](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/scep/scep4.png)


