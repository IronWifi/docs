
- enable [Azure AD Domain Services](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/create-instance) 
- create [CentOS virtual machine](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal)
- create AAD domain admin user **bob**


### Join Linux machine to Domain ###

Follow instructions from [this page](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/join-centos-linux-vm)

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

Restart Samba and Winbind
```
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

Now browse the following file through frontend using your favorite web browser. Go to the following URL.

[http://your-IP-addr/ntlm.php](http://your-IP-addr/ntlm.php)
    
You will see following message. This shows that you have a working Lighttpd web server with PHP-FPM.
```
hex decode of  failed!
```

