
### About

This is a small script that helps you to automatically send phone numbers in bulk to your VIBER Channel as contacts and thus reveal whether a certain phone number is associated with a registered VIBER account.
There's no need in sharing your contacts with Viber.
Overall it helps you with your Open Source Intelligence (OSINT) workflow on Messangers - specifically Viber.

**It's not a full automation, you will need to do some things manually, but overall it saves more time by automating the most time consuming and dull task - adding phone numbers to the contact book**

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


* send a single phone number to a viber channel as a contact **(this phone number has a registered Viber account)**

```

python3 viber_contacts.py --phone +79124538669

```

* send a single phone number to a viber channel as a contact **(this phone number doesn't have a registered Viber account associated with it)**

```
python3 viber_contacts.py --phone +79124538670

```


* send phones in bulk

```

python3 viber_contacts --list phones.txt

```



### After you ran a script:

* Open Viber Desktop and go to your VIBER channel
* Mostly always VIBER doesn't want to resolve contacts automatically, that's why you might need to do it manually or wait
* **Account is unresolved if its name is still "a"**

![alt text](https://github.com/sgxgsx/ViberOSINT/images/notshown.png?raw=true)

* In order to manually resolve the accounts you need to:
* Click on the "a" name on a popup contact. It'll take you to another view where the name of this contact would change
* **If the name is a phone number and profile picture hasn't changed - it means that this phone number is not on Viber**
![alt text](https://github.com/sgxgsx/ViberOSINT/images/notonviber.png?raw=true)
* **Otherwise, you'll see that the name of the contact is updated or you'll see a profile picture**
![alt text](https://github.com/sgxgsx/ViberOSINT/images/onviber.png?raw=true)


