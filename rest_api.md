# REST API

If you are a software developer or integrator, you might want to use the provided API (Application Programming Interface) to integrate the IronWifi authentication service with your existing system easily. Possible system integrations include:

- Building access control system
- Human resources system
- Visitor tracking system
- Billing system
- Hotel check-in, checkout system

The API communication interface is available at https://console.ironwifi.com/api, and communication is provided strictly through the HTTPS protocol and JSON arrays.

Full documentation of our API is available on [this webpage](https://documenter.getpostman.com/view/10902824/SzmZdLRy?version=latest).

All requests have to include authorization header with valid API token which is generated in Console -> Account -> API Keys.

## Examples on how to use the Rest API

https://curl.haxx.se/download.html is one method of working with our API.

Generate an [API key](https://www.ironwifi.com/user-guide/api-keys/) and add it to the variable below. This key will be used with all requests sent to the API.

key=’xxxxxxxxxxxxxxxxxxxx’;

### To get a list of users
```php
<?php
$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/users",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer " . $api_key
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>

```

### Create new user
```php
<?php
$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/users",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS =>"{\"username\": \"Milan.Hand\"}",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer " . $api_key,
    "Content-Type: application/json"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>
```
Response includes the user_id. It is required to manipulate the user profile.

user_id=2969744;

### Set a user password (add attribute)
```php
<?php
$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/attributes",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS =>"{\n\t\n\"value\":\"tlGkkAjKw7xtCMq\",\n\"userid\": $user_id,\n\"attribute\":\"Cleartext-Password\",\n\"operator\":\":=\",\n\"table\":\"radcheck\"\n\t\n}",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer " . $api_key,
    "Content-Type: application/json"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>
```
 

### Get a list of user attributes
```php
<?php
$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/attributes?table=radcheck&userid=" . $user_id,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer " . $api_key
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>
```

Response provides attribute_id. It is required to manipulate the attribute.

attribute_id=5505687;

### To delete an attribute
```php
<?php

$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/attributes/" . $attribute_id . "?table=radcheck",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer " . $api_key
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>
``` 

### Download a report data synchronously, works with data up to 4 hours old.

```php
<?php
$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/110?earliest=-4h&latest=now&page=1&period=1",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer " . $api_key
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>
```

### Get report data asynchronously, returns task_name.
```php
<?php
$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/reports/115?earliest=-1d@d&format=csvfile&latest=now&page=1&period=1&columns=fullname,email,phone,client_mac,address,creationdate",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer $api_key"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>
```

### To retrieve prepared report data.
```php
<?php
$api_key = "";
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://console.ironwifi.com/api/reports/tasks?format=csvfile&task_name=" . $task_name,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer " . $api_key
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>
```
