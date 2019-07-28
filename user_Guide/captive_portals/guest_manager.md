# Guest Manager

This section configures temporary user accounts generated during the authentication process via Captive Portal.

**Username Type** - Specifies the format of generated username, where the user does not provide a username. It can have a format of:

- Digits
- Letters
- Digits and Letters
- Format picture - eg. public-###??? ( # will be replaced with a random number [0-9], ? will be replaced with a random letter [A-Za-z]
- Email address - requires input field with name "email", if missing, we will use random Letters
- Phone number - requires input field with name "phone_number", if value is missing, we will use random Letters
- Client MAC Address - if not known, random Letters will be used

**Username Length** - defines a length of generated username

**Password Type** - Specifies the format of generated password. It can have a form of Digits, Letters, Digits and Letters, Mixed case Letters and Digits, Letters and Digits and Symbols and at least one uppercase/lowercase letter, digit and symbol. This password type is also used with Authentication Providers, where a temporary token is generated and sent to the user for verification.

**Password Length** - defines length of generated password

**Expire After** - Guest accounts are considered to be temporary and can expire after a certain period of time. You can specify the validity of these accounts in this format - 5i = 5 minutes (i = minutes, h = hours, d = days, w = weeks, m = months). If Cookie-Based authentication is enabled, this parameter also defines the Cookie expiration time.

**Expire Action** - specify what should happen to the generated account after a certain period of time. The account can be automatically disabled or deleted after it expires.

