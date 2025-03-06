import httpx as requests
import sys
import os
import json
from datetime import datetime
import time
import keyboard
if len(sys.argv)==1:
    os.system(r"C:\Users\teren\anaconda3\python.exe -u cmd.py 0 | cmd.exe 2>&1 | C:\Users\teren\anaconda3\python.exe cmd.py 1")
token="7916790982:AAHfrFvAHSYtCw5Qx6DhmdAGcq2yE6H5yYo"
#print(sys.argv)
if sys.argv[1]=="0":
    print("echo test")
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
        rqj=rqj["result"]
        for i in rqj:
            if i["update_id"]<offset:
                continue
            offset=int(i["update_id"])+1
            if i["message"]["from"]["username"]!="terryp12":
                #print("PHONY")
                continue
            if i["message"]["date"]<tstart:
                #print("EARLY")
                continue
            if i["message"]["text"]=="/shutup":
                os.system("echo test > SHUTUP")
                continue
            if i["message"]["text"]=="/talk":
                os.system("echo test > TALK")
                continue
            if i["message"]["text"]=="/restart":
                raise Exception("Must restart")
            if i["message"]["text"]=="/enter":
                keyboard.press_and_release("Enter")
                continue
            if i["message"]["text"][:5]=="kill ":
                os.system("taskkill "+i["message"]["text"][5:]+">NUL 2>NUL")
                continue
            print(i["message"]["text"])
            #os.system(f"start cmd.exe /k echo {i['message']['text']}")

rq=requests.post(
    f"https://api.telegram.org/bot{token}/getUpdates",
    data={
        "allowed_updates": ["message"]
    }
)

print(rq.text)
js=json.loads(rq.text)
cid=0
try:
    cid=int(js["result"][-1]["message"]["chat"]["id"])
except IndexError:
    os.system("taskkill /f /fi \"IMAGENAME EQ python.exe\"")
requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data={
        "chat_id": cid,
        "text": "Sorry, there was an internal error!"
    }
)
shutup=False
while True:
    prm=input()
    print(prm)
    if (os.path.exists("SHUTUP")):
        shutup=True
        os.system("del SHUTUP")
        try:
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data={
                    "chat_id": cid,
                    "text": "Fine, I shut up untill you say /talk"
                }
            )
        except Exception:
            pass
    if (os.path.exists("TALK")):
        shutup=False
        os.system("del TALK")
        try:
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data={
                    "chat_id": cid,
                    "text": "I may talk again!!!"
                }
            )
        except Exception:
            pass
    if (shutup):
        continue
    try:
        if (len(prm)==0):
            prm="."
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={
                "chat_id": cid,
                "text": prm
            }
        )
    except Exception:
        pass
