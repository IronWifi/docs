# IronWifi Documentation

- This is IronWifi documentation's GitHub repository, in case you see an error or a possible improvement, please pull a request or open an issue. Any contribution is appreciated.


# API Quickstart

Endpoint: _https://console.ironwifi.com/api_

The API endpoint depends on the region you want to use, if you are using the us-west1 region in the console, the API endpoint will also look as such (https://us-west1.ironwifi.com/api)

## Authorization

In order to use IronWifi REST API to automate tasks or manipulate the with the console programmatically, you need to generate an API key. This can be done in the IronWifi console, section Account under _API keys_. Note that the API key will (for security reasons) only be visible once, upon generation. Therefore, make sure you store the API key in a secure place before closing the popup.

![api_key_screenshot](https://raw.githubusercontent.com/IronWifi/docs/master/api_key.png)

You will need to use this API key in your authorization header as shown below.

```
'Authorization': 'Bearer ' + api_key
```

Do not forget to add the _Content-Type_ header as well.

```
'Content-Type': 'application/json;charset=utf-8'
```

You can now send requests to the API and automate your workflow accordingly.

## Example request

Getting the list of users using JavaScript.

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer your_api_key");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://console.ironwifi.com/api/users", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

---
Full documentation of this REST API can be found [here](https://documenter.getpostman.com/view/10902824/SzmfXxAW).
 
