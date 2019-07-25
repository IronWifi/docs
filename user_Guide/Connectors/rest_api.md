# Rest API Connector

This page describes the format of messages for external authentication using REST API.

During the authentication process, the Rest API connector will POST information in JSON format to your web server (API endpoint) for verification. The information included in the request will depend on the authentication method - PAP, MS-CHAP, TTLS-PAP, etc. Every call is authorized with an API token included with every request as a Bearer token.

 

List of variables sent to the external server:

**login** - contains user's username

**password** - user's password, available only with PAP and TTLS+PAP authentication method

**auth_port** - RADIUS server authentication port that received this request

**mschap_challenge** - if using the MS-CHAP authentication method

**mschap_response** - if using the MS-CHAP authentication method

Sample Request:

```
$ curl -i -X POST https://YOUR_API_ENDPOINT -H "Authorization: Bearer YOUR_API_TOKEN" -H 'Content-Type: application/json' -d '{ "login": "user1", "auth_port": "11111", "mschap_challenge": "99999999", "mschap_response": "888888888888888888"}'
```

Response Status Codes:

2** - return status code indicates success and sample body provides user attributes, access will be approved

```
HTTP/1.1 200 OK
{"return_url":"https://www.google.com","valid_until":"2017/01/10 01:59:59 +0000","valid_from":"2017/01/09 02:03:52 +0000","nt_key":"abcd12345","membership_id":"`123456","membership":{"name":"John Sample","id":"12345678"},"id":"123456789abcdef","attributes":[{"name":"Tunnel-Private-Group-Id","value":"101","op":":="},{"name":"Acct-Interim-Interval","value":"300","op":":="}]}
```

Attributes from the answer will be added to the RADIUS server response and sent to the Wireless Controller.

4** - return status code indicates failure and body provides an error message, and we will reject the access request

```
HTTP/1.1 422 Unprocessable Entity
{"errors":["Email/login or password incorrect."]}
```
