# **Groups**

---

Voucher/User can be a member of multiple groups and **inherit attributes** from these groups. This way, you can apply attributes to users/vouchers in bulk.

- **Priority -** determines the order of how the group membership should be evaluated, starting with 1 (highest priority), down to 10 (lowest priority). The evaluation will continue through all groups until a match is found - all Check Attributes match the request. If this happens, group Reply attributes will be added to the Response, and no further Groups will be checked
- **Description -** Message visible only to the administrator, not the end-user
- **Users In This Group -** Total number of users
- **Status -** Whether or not users/vouchers in this group should be allowed to access the network, if disabled, users/vouchers will not be able to authenticate
