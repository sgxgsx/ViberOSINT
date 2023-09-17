import requests
import argparse
import json

CONFIG = {}

def set_webhook():
    payload = {
        "auth_token": CONFIG['token'],
        "url":"https://proton.me/",
        "event_types":[
            "failed"
        ],
        "send_name": False,
        "send_photo": False
    }
    r = requests.post("https://chatapi.viber.com/pa/set_webhook", json=payload)
    print(r.text)


def get_account_info():
    r = requests.post("https://chatapi.viber.com/pa/get_account_info", json={"auth_token": CONFIG['token']})
    if r.status_code == 200:
        print(r.json())
        return r.json()["id"]
    else:
        return None


def send_contact_message(phone_number: str):
    if CONFIG['uid'] is None or CONFIG['uid'] == '':
        print("Error in uid")
        raise Exception("Something went wrong uid is None or empty")

    payload = {
        "auth_token": CONFIG['token'],
        "from": CONFIG['uid'],
        "type": "contact",
        "contact": {
            "name":"a",
            "phone_number":phone_number

        }
    }

    r = requests.post("https://chatapi.viber.com/pa/post", json=payload)
    print(r.text)
    if r.status_code == 200:
        print("Sent message for - {}".format(phone_number))


def send_bulk_message(fname):
    phones = [x.strip() for x in open(fname, 'r').read().split('\n')]
    for phone in phones:
        send_contact_message(phone)

def load_config():
    global CONFIG
    CONFIG = json.load(open('config.json','rb'))
    if CONFIG['token'] == '':
        raise Exception("Please specify your TOKEN")
    
    if CONFIG['first_time'] == 1:
        set_webhook()
        CONFIG['first_time'] = 0
        json.dump(CONFIG, open('config.json', 'w'))

    if CONFIG['uid'] == '':
        uid = get_account_info()
        print(uid)
        if uid is None:
            raise Exception("Something went wrong uid is returned as None")
        CONFIG['uid'] = uid
        json.dump(CONFIG, open('config.json', 'w'))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--phone', required=False, type=str, help="phone number +7...")
    parser.add_argument('-l','--list', required=False, type=str, help="list with phone numbers")
    args = parser.parse_args()
    
    load_config()
    
    if  not (args.phone and args.list) and (args.phone or args.list):
        if args.phone:
            send_contact_message(args.phone)
        else:
            send_bulk_message(args.list)
    else:
        parser.print_help()

    print("########## All messages sent ###########")

