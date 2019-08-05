# API Keys

## Table of Contents

- What are API Keys?
- Create an API Key
- API Key Permissions
- Edit an API Key
- Deactivate an API Key
- Sending requests With an API Key

## What are API Keys?

API keys are used by your application, or website to authenticate access to IronWifi services. They are the preferred alternative to using a username and password because you can revoke an API key at any time without having to change your username and password. We suggest that you use API keys for connecting to all of IronWifi’s services.

You may assign an API key specific Role that will further restrict which API calls it is capable of authenticating. For more detailed information about API key permissions, please visit our [Roles](https://www.ironwifi.com/user-guide/roles/).

When viewing the API keys page, you will see a list of your current API keys along with the following information:

**Name** - The name you defined for your API key.

**Key ID** - The way you would reference your API key for management through the API. (e.g. editing or deleting a key)

**Action** - Actions you can perform on your API keys, such as editing or deleting the key.

## Create an API Key

When you click the "Create Key" button, a popup menu will appear allowing you to enter Key Name and choose Role.

The API key name will follow your API key around through the IronWifi customer portal, so it is important that you choose a name that is meaningful to you.

You will only be shown your API key one time. Please store it somewhere safe as we will not be able to retrieve or restore this generated token.

## Edit an API Key

Click the edit icon in the same row as the key you would like to edit. From here you can delete a key, making it completely inactive, or you can edit your key’s name and role.

## Inactivate an API Key

Once you delete a key, it can no longer be used to access IronWifi’s services.

Click the trash icon in the same row as the key you want to inactivate. Choose "Delete." This will delete the key permanently, making it inactive. Any subsequent API calls using this deleted API key will be rejected by IronWifi.

## Sending Commands with an API Key

You will need an API key to control your IronWifi account, and we have provided basic instructions on how to send requests with our API Keys in case you need them, see [REST API documentation](https://www.ironwifi.com/documentation/api/) .



