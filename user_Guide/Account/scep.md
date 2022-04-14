# **SCEP with Intune**

---

The Simple Certificate Enrolment Protocol (SCEP) is a protocol that allows devices to easily enroll for a certificate by using a URL and a shared secret to communicate with a PKI. The following instructions explain how to set up SCEP and IronWifi with Microsoft Intune.

### What do you need ?

- **owner_id -** owner id is a unique identifier of your ironwifi account that can be found in the URL when you're logged in, it should look similar to this - abcdefg12345678 or domain-abcd1234
- **region -** region where your data resides and authentication requests are processed - us-east1, console, asia-northeast1, etc
- **SCEP Server URL -** build the URL in this format - https://{{region}}.ironwifi.com/api/{{owner_id}}/certificates/scep.

  Note that for Windows profiles, "/scep" needs to be removed since it is appended by the Intune application automatically - https://{{region}}.ironwifi.com/api/{{owner_id}}/certificates

- **IronWiFi CA Certificate -** certificate of the CA signing the CSR requests. This can be downloaded from [this link](https://console.ironwifi.com/assets/html/ironwifi.crt)
- **Trusted IronWiFi Server Certificate -** server certificate signed by a trusted CA. This file can be downloaded from [this link](https://console.ironwifi.com/assets/html/ironwifi_trusted.crt)
- **Comodo CA Certificate -** certificate of the CA that signed our RADIUS server certificates. This can be downloaded from [this link](https://console.ironwifi.com/assets/html/radius_ironwifi_com_ca-bundle.crt)


**!Note!** Your users must exist in the ironwifi console or the SCEP connector's User Auto-Creation option must be enabled for this to work

1. Sign in to the IronWifi Console and create a SCEP connector - click on Users -> Connectors -> Add New

2. Sign in to the [Intune management console](https://endpoint.microsoft.com/#blade/Microsoft_Intune_DeviceSettings/DevicesMenu/overview) and create a new Trusted Certificate profile with the following configuration options:

- **Certificate file -** ironwifi.crt
- **Destination store -** Computer certificate store - Root

3. Create a new Trusted Certificate profile with the following configuration options:

- **Certificate file -** ironwifi_trusted.crt
- **Destination store -** Computer certificate store - Root

4. Create a new SCEP certificate profile with the following configuration options:

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

5. Create a new Wi-Fi profile with the following configuration options:

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
- **Certificate server names -** radius.ironwifi.com
- **Root certificates for server validation -** _The trusted certificate created in the second step_
- **Authentication method -** SCEP certificate
- **Client certificate for client authentication (identity certificate) -** _Your SCEP certificate created in the third step_

You should now see 4 profiles under **Devices** in your **Microsoft Endpoint Manager admin center**

In Microsoft Intune, your settings should look like below.


![test](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/scep/scep11.png)
![test](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/scep/scep12.png)
![test](https://raw.githubusercontent.com/IronWifi/docs/master/user_Guide/Account/scep/scep13.png)


