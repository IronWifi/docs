# Azure AD Authentication with PEAP-MSCHAPv2

This tutorial provides instructions on how to make PEAP-MSCHAPv2 authentication work with IronWifi and Azure AD Domain Services.

- enable [Azure AD Connector](https://www.ironwifi.com/azure-active-directory/)
- enable [Azure AD Domain Services](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/create-instance) 
- create [CentOS virtual machine](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal)
  - Make sure to choose the same resource group as in your Azure AD Domain Services, but different subnet.
  - Allow ports 80 and 443 only from the IronWifi addresses that call your bridge (replace IRONWIFI_EGRESS_IP with each address, and apply the same source restriction in the VM's Azure network security group). Do not open these ports to the whole internet: the bridge checks Active Directory passwords.
  ```
  iptables -A INPUT -p tcp -m tcp -s IRONWIFI_EGRESS_IP --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
  ```
  ```
  iptables -A INPUT -p tcp -m tcp -s IRONWIFI_EGRESS_IP --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
  ```
- create AAD domain admin user **bob**


### Join Linux machine to Domain ###

Follow instructions from [this page](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/join-centos-linux-vm) 
- You may need to change bob's password before executing 'kinit'

Update /etc/hosts and add machine information
```
echo "127.0.0.1 ironwificentos.testgmail.onmicrosoft.com ironwificentos" >> /etc/hosts
```
  
Install required packages on Linux machine
```
sudo yum install realmd sssd krb5-workstation krb5-libs oddjob oddjob-mkhomedir samba-common-tools
```

Discover the AAD Domain Services managed domain. In your SSH terminal, type the following command:
```
sudo realm discover TESTGMAIL.ONMICROSOFT.COM
```

Update kerberos config file /etc/krb5.conf

```
[libdefaults]
 dns_lookup_realm = true
 dns_lookup_kdc = true
 ticket_lifetime = 24h
 renew_lifetime = 7d
 forwardable = true
 rdns = false
 pkinit_anchors = /etc/pki/tls/certs/ca-bundle.crt
 default_realm = TESTGMAIL.ONMICROSOFT.COM
 default_ccache_name = KEYRING:persistent:%{uid}
 default_realm = TESTGMAIL.ONMICROSOFT.COM
 
 [realms]
 TESTGMAIL.ONMICROSOFT.COM = {
  kdc = 10.3.0.4
  admin_server = testgmail.onmicrosoft.com
  default_domain = testgmail.onmicrosoft.com
 }
 
 [domain_realm]
 .testgmail.onmicrosoft.com = TESTGMAIL.ONMICROSOFT.COM
 testgmail.onmicrosoft.com = TESTGMAIL.ONMICROSOFT.COM
```


- Initialize Kerberos. Try to get a valid Kerberos ticket for your active directory administrator account,
```
kinit bob@TESTGMAIL.ONMICROSOFT.COM
```


### Configure SAMBA and WINBIND ###

- update /etc/resolv.conf, add "search ironwificentos.testgmail.onmicrosoft.com"
- update /etc/samba/smb.conf

```
[global]
        workgroup = TESTGMAIL
        security = ads
        realm = TESTGMAIL.ONMICROSOFT.COM
        winbind use default domain = yes
        winbind offline logon = false
        winbind enum users = yes
        winbind enum groups = yes
        passdb backend = tdbsam
        template shell = /bin/bash
        idmap uid = 100000-200000
        idmap gid = 100000-200000
        template homedir = /home/%U

        printing = cups
        printcap name = cups
        load printers = yes
        cups options = raw
```

Create service startup script and restart Samba and Winbind
```
service samba enable
service winbind enable

service samba restart
service winbind restart
```

- Joing the Linux machine to domain
```
net join -w testgmail.onmicrosoft.com -U bob@testgmail.onmicrosoft.com
```

Test authentication
```
wbinfo -a 'bob%__PASSWORD__'
plaintext password authentication succeeded
challenge/response password authentication succeeded
```

### Installing the web server ###

Install the EPEL repository
```
yum install epel-release -y
```

Import the EPEL GPG key
```
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
```

Install the Lighttpd web server
```
yum install lighttpd -y
```

Open /etc/lighttpd/lighttpd.conf and disable IPv6
```
#server.use-ipv6 = "enable"
```

Start the service and create startup links
```
systemctl enable lighttpd
systemctl start lighttpd
```

Install the PHP-FPM and FastCGI packages
```
yum -y install php-fpm lighttpd-fastcgi
```

Open /etc/php-fpm.d/www.conf
```
nano /etc/php-fpm.d/www.conf
```

... and set user and group to lighttpd:
```
[...]
; Unix user/group of processes
; Note: The user is mandatory. If the group is not set, the default user's group
;       will be used.
; RPM: apache Choosed to be able to access some dir as httpd
user = lighttpd
; RPM: Keep a group allowed to write in log dir.
group = lighttpd
[...]
```

Generate a long random bridge secret. IronWifi sends it on every request and ntlm.php refuses any request that does not carry it.
```
openssl rand -hex 32
```

Add it to the same file /etc/php-fpm.d/www.conf, replacing \_\_BRIDGE_SECRET\_\_ with the generated value, and make the file readable only by root:
```
env[IRONWIFI_BRIDGE_SECRET] = __BRIDGE_SECRET__
```
```
chmod 600 /etc/php-fpm.d/www.conf
```

Create the system startup links for PHP-FPM and start it:
```
systemctl enable  php-fpm.service
systemctl start  php-fpm.service
```

## Configuring Lighttpd to Work With PHP ##

To enable PHP to work with Lighttpd web server, we will need to make few configuration changes. Open your /etc/php.ini file in your favorite editor:
```
nano /etc/php.ini
```

Look for the following lines in the configuration:
```
    ; cgi.fix_pathinfo provides *real* PATH_INFO/PATH_TRANSLATED support for CGI.  $
    ; previous behaviour was to set PATH_TRANSLATED to SCRIPT_FILENAME, and to not $
    ; what PATH_INFO is.  For more information on PATH_INFO, see the cgi specs.  Se$
    ; this to 1 will cause PHP CGI to fix its paths to conform to the spec.  A sett$
    ; of zero causes PHP to behave as before.  Default is 1.  You should fix your s$
    ; to use SCRIPT_FILENAME rather than PATH_TRANSLATED.
    ; http://php.net/cgi.fix-pathinfo
    ;cgi.fix_pathinfo=1
```

Uncomment the line
```
;cgi.fix_pathinfo=1
```
to make it
```
cgi.fix_pathinfo=1
```

Save the file and exit the editor.

Now open another file /etc/lighttpd/conf.d/fastcgi.conf using your favorite editor.
```
nano /etc/lighttpd/conf.d/fastcgi.conf
```

Now look for the following lines in the file:
```
server.modules += ( "mod_fastcgi" )
```

Add the following lines just below the above line:

```
fastcgi.server += ( ".php" =>
            ((
                    "host" => "127.0.0.1",
                    "port" => "9000",
                    "broken-scriptfilename" => "enable"
            ))
)
```

Save the file and exit from editor:

Now open /etc/lighttpd/modules.conf file using your favorite editor.
```
nano /etc/lighttpd/modules.conf
```

Look for the following lines in the file:
```
##
## FastCGI (mod_fastcgi)
##
#include "conf.d/fastcgi.conf"
```

Uncomment __#include "conf.d/fastcgi.conf"__ to make it look line __include "conf.d/fastcgi.conf"__. Save the file and exit from editor.

Now restart PHP-FPM and Lighttpd using the following command.
```
systemctl restart php-fpm
systemctl restart lighttpd
```

Now to verify if Lighttpd is configured to use PHP-FPM, you will need to view your php information. Create a new file in your document root directory which may be /var/www/htdocs or /var/www/lighttpd according how you have configured it before.
```
nano /var/www/lighttpd/ntlm.php
```

Now add the following php code into the file.
```
<?php
$secret=getenv('IRONWIFI_BRIDGE_SECRET');
$supplied=isset($_GET['secret']) ? $_GET['secret'] : null;
if (!is_string($secret) || $secret === '' || !is_string($supplied) || !hash_equals($secret, $supplied)){
      http_response_code(403);
      exit;
}
$pos=strrpos($_GET['username'], "\\");
if ($pos == true){
      $username=escapeshellarg(substr($_GET['username'],$pos+1));
}else{
      $username=escapeshellarg($_GET['username']);
}
$challenge=escapeshellarg(@$_GET['challenge']);
$response=escapeshellarg(@$_GET['response']);
$domain=@$_GET['domain'];
$cmd = "/bin/ntlm_auth --request-nt-key --username=$username --challenge=$challenge --nt-response=$response 2>&1";
$ouput = exec("$cmd",$out,$ret);
echo $out[0];
?>
```

If you have SELINUX enabled, allow lighttpd access winbind 
```
setsebool -P httpd_mod_auth_ntlm_winbind 1
```

Restart PHP-FPM so it picks up the bridge secret.
```
systemctl restart php-fpm
```

Check that the script refuses a request without the secret. It must answer with HTTP 403 and an empty body.
```
curl -i http://127.0.0.1/ntlm.php
```

Check that a request with the secret reaches ntlm_auth (replace \_\_BRIDGE_SECRET\_\_ with your value). You will see the following message. This shows that you have a working Lighttpd web server with PHP-FPM.
```
curl "http://127.0.0.1/ntlm.php?secret=__BRIDGE_SECRET__"
hex decode of  failed!
```

Return to the IronWifi console and set the Bridge URL value in your Azure Connector, including the secret. The secret travels in the URL, so serve the bridge over HTTPS and do not log query strings in your web server's access log.
```
Bridge URL:    https://your-bridge-hostname/ntlm.php?secret=__BRIDGE_SECRET__
```
