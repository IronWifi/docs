# REST API

If you are a software developer or integrator, you might want to use the provided API (Application Programming Interface) to integrate the IronWifi authentication service with your existing system easily. Possible system integrations include:

- Building access control system
- Human resources system
- Visitor tracking system
- Billing system
- Hotel check-in, checkout system

The API communication interface is available at https://console.ironwifi.com/api, and communication is provided strictly through the HTTPS protocol and JSON arrays.

Full documentation of our API is available at https://market.mashape.com/ironwifi/ironwifi.

**For best performance, please send your requests to https://console.ironwifi.com/api, not the Mashape gateway servers available at https://ironwifi.p.mashape.com/api**

All requests have to include authorization header with valid API token which is generated in Console -> Account -> API Keys.

## Examples on how to use the Rest API

https://curl.haxx.se/download.html is one method of working with our API.

Generate an [API key](https://www.ironwifi.com/user-guide/api-keys/) and add it to the variable below. This key will be used with all requests sent to the API.

key=’xxxxxxxxxxxxxxxxxxxx’;

**To get a list of users**
```
$ curl 'https://console.ironwifi.com/api/users' -H "authorization: Bearer $key" -H 'accept: application/json, text/plain, */*'
```
 

**Create new user**
```
$ curl 'https://console.ironwifi.com/api/users' -H "authorization: Bearer $key" -H 'content-type: application/json;charset=UTF-8' -H 'accept: application/json, text/plain, */*' –data-binary '{"username":"USER1"}'
```
Response includes the user_id. It is required to manipulate the user profile.

user_id=2969744;

**Set a user password (add attribute)**
```
$ curl 'https://console.ironwifi.com/api/attributes' -H "authorization: Bearer $key" -H 'content-type: application/json;charset=UTF-8' -H 'accept: application/json, text/plain, */*' –data-binary "{\"userid\":\"$user_id\",\"attribute\":\"Cleartext-Password\",\"operator\":\":=\",\"table\":\"radcheck\",\"value\":\"abc123\"}"
```
 

**Get a list of user attributes**
```
$ curl "https://console.ironwifi.com/api/attributes?table=radcheck&userid=$user_id" -H "authorization: Bearer $key" -H 'accept: application/json, text/plain, */*'
```

Response provides attribute_id. It is required to manipulate the attribute.

attribute_id=5505687;

**To delete an attribute**
```
$ curl "https://console.ironwifi.com/api/attributes/$attribute_id?table=radcheck" -X DELETE -H "authorization: Bearer $key" -H 'accept: application/json, text/plain, *.*'
``` 

**Download a report data synchronously, works with data up to 4 hours old.**

```
$ curl "https://console.ironwifi.com/api/110?earliest=-4h&latest=now&page=1&period=1" -H "authorization: Bearer $key" -H 'accept: application/json, text/plain, *.*'
```

**Get report data asynchronously, returns task_name.**
```
$ curl "https://console.ironwifi.com/api/reports/115?earliest=-1d@d&format=csvfile&latest=now&page=1&period=1&columns=fullname,email,phone,client_mac,address,creationdate" -H "authorization: Bearer $key" -H
"accept: application/json, text/plain, */*"
```

**To retrieve prepared report data.**
```
$ curl "https://console.ironwifi.com/api/reports/tasks?format=csvfile&task_name=$task_name"
-H "authorization: Bearer $key"
```
