import requests
import json
import random
import time
import os



def get_context():
    context_list = [
        "!faucet 0x4ea5050f62fa71bd22f6e02b0f80563b82919deb",
    ]
    text = random.choice(context_list)
    return text


def chat(chanel_list,authorization_list):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        for chanel_id in chanel_list:
            msg = {
                "content": get_context(),
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False,
            }
            url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
            print(url)
            try:
                res = requests.post(url=url, headers=header, data=json.dumps(msg))
                print(res.content)
            except:
                pass
            continue
        time.sleep(random.randrange(1, 3))


if __name__ == "__main__":
    chanel_list = ["971488439931392130"]
    authorization_list = [os.environ.get('authcode')]
    while True:
        try:
            chat(chanel_list,authorization_list)
            sleeptime = random.randrange(5000, 5500)
            time.sleep(sleeptime)
            print("sleep {}s".format(sleeptime))
        except:
            break
