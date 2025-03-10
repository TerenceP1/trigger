import httpx as requests
import sys
import os
import json
from datetime import datetime
import time
import keyboard
import math

if len(sys.argv) == 1:
    os.system(r"C:\Users\teren\anaconda3\python.exe -u cmd.py 0 | cmd.exe 2>&1 | C:\Users\teren\anaconda3\python.exe cmd.py 1")

token = "7916790982:AAHfrFvAHSYtCw5Qx6DhmdAGcq2yE6H5yYo"

if sys.argv[1] == "0":
    print("echo test")
    offset = 0
    tstart = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()

    while True:
        rq = requests.post(
            f"https://api.telegram.org/bot{token}/getUpdates",
            data={
                "offset": offset,
                "allowed_updates": ["message"]
            }
        )

        rqj = json.loads(rq.text)["result"]

        for i in rqj:
            if i["update_id"] < offset:
                continue
            if "message" not in i:
                continue
            if "text" not in i["message"]:
                continue

            offset = int(i["update_id"]) + 1

            if i["message"]["from"]["username"] != "terryp12":
                continue
            if i["message"]["date"] < tstart:
                continue

            if i["message"]["text"] == "/shutup":
                os.system("echo test > SHUTUP")
                continue
            if i["message"]["text"] == "/talk":
                os.system("echo test > TALK")
                continue
            if i["message"]["text"] == "/restart":
                raise Exception("Must restart")
            if i["message"]["text"] == "/enter":
                keyboard.press_and_release("Enter")
                continue
            if i["message"]["text"] == "/record":
                os.system("echo hi > RECORD")
                continue
            if i["message"]["text"] == "/replay":
                os.system("echo hi > REPLAY")
                continue
            if i["message"]["text"][:5] == "kill ":
                os.system("taskkill " + i["message"]["text"][5:] + ">NUL 2>NUL")
                continue

            print(i["message"]["text"])

        rq = requests.post(
            f"https://api.telegram.org/bot{token}/getUpdates",
            data={
                "allowed_updates": ["message"]
            }
        )
        js = json.loads(rq.text)
        cid = 0

        try:
            cid = int(js["result"][-1]["message"]["chat"]["id"])
        except IndexError:
            os.system("taskkill /f /fi \"IMAGENAME EQ python.exe\"")
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data={
                    "chat_id": cid,
                    "text": "Sorry, there was an internal error!"
                }
            )

        shutup = False
        record = False
        rpbuf = ""

        while True:
            prm = input()
            print(prm)

            if os.path.exists("SHUTUP"):
                shutup = True
                os.system("del SHUTUP")
                try:
                    requests.post(
                        f"https://api.telegram.org/bot{token}/sendMessage",
                        data={
                            "chat_id": cid,
                            "text": "Fine, I shut up until you say /talk"
                        }
                    )
                except Exception:
                    pass

            if os.path.exists("TALK"):
                shutup = False
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

            if os.path.exists("RECORD"):
                record = True
                os.system("del RECORD")
                try:
                    requests.post(
                        f"https://api.telegram.org/bot{token}/sendMessage",
                        data={
                            "chat_id": cid,
                            "text": "Recording 'till /replay"
                        }
                    )
                except Exception:
                    pass

            if os.path.exists("REPLAY"):
                record = False
                os.system("del REPLAY")
                try:
                    requests.post(
                        f"https://api.telegram.org/bot{token}/sendMessage",
                        data={
                            "chat_id": cid,
                            "text": f"{math.ceil(len(rpbuf) / 4096)} chunks"
                        }
                    )
                    for i in range(0, len(rpbuf), 4096):
                        requests.post(
                            f"https://api.telegram.org/bot{token}/sendMessage",
                            data={
                                "chat_id": cid,
                                "text": rpbuf[i:i + 4096]
                            }
                        )
                    rpbuf = ""
                except Exception:
                    pass

            if record:
                rpbuf += prm + "\n"
                continue

            if shutup:
                continue

            try:
                if len(prm) == 0:
                    prm = "."
                requests.post(
                    f"https://api.telegram.org/bot{token}/sendMessage",
                    data={
                        "chat_id": cid,
                        "text": prm
                    }
                )
            except Exception:
                pass
