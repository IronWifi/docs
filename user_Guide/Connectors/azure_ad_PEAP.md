# Azure AD Authentication with PEAP-MSCHAPv2

This tutorial provides instructions on how to make PEAP-MSCHAPv2 authentication work with IronWifi and Azure AD Domain Services.

- enable [Azure AD Connector](https://www.ironwifi.com/azure-active-directory/)
- enable [Azure AD Domain Services](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/create-instance)
- create [CentOS virtual machine](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal)
  - Make sure to choose the same resource group as in your Azure AD Domain Services, but different subnet.
  - Allow ports 80 and 443 by executing these commands iptables -A INPUT - p tcp -m tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT iptables -A INPUT - p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
- create AAD domain admin user bob

Join Linux machine to Domain

Follow instructions from this page - You may need to change bob's password before executing 'kinit'

Update /etc/hosts and add machine information
