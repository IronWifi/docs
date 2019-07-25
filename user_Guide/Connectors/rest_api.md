# Rest API Connector

This page describes the format of messages for external authentication using REST API.

During the authentication process, the Rest API connector will POST information in JSON format to your web server (API endpoint) for verification. The information included in the request will depend on the authentication method - PAP, MS-CHAP, TTLS-PAP, etc. Every call is authorized with an API token included with every request as a Bearer token.

 

List of variables sent to the external server:

**login** - contains user's username

**password** - user's password, available only with PAP and TTLS+PAP authentication method

**auth_port** - RADIUS server authentication port that received this request

**mschap_challenge** - if using the MS-CHAP authentication method

**mschap_response** - if using the MS-CHAP authentication method
