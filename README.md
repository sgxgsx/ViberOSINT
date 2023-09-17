
### About

This is a small script that helps you to automatically send phone numbers in bulk to your VIBER Channel as contacts and thus reveal whether a certain phone number is associated with a registered VIBER account.
There's no need in sharing your contacts with Viber.
Overall it helps you with your Open Source Intelligence (OSINT) workflow on Messangers - specifically Viber.

### Install

```
git clone https://github.com/sgxgsx/ViberOSINT.git

```

#### Token

* Create a VIBER account
* Create a VIBER channel
* Use the following documentation to find your API token - [https://developers.viber.com/docs/tools/channels-post-api/](https://developers.viber.com/docs/tools/channels-post-api/). You can find your token by entering your Channel’s info screen-> scroll down to “Developer Tools” -> copy token -> use the token for posting via API.
* Edit config.json in the repository and change [TOKEN] to your copied token
* Next time you are running the script, it'll automatically update the config file to include your UID and also would activate your channel api token by setting up a webhook.


### Examples


* send a single phone number to a viber channel as a contact

```

python3 viber_contacts.py --phone +498002858585

```

* send phones in bulk

```

python3 viber_contacts --list phones.txt

```



