import httpx
with open("gogogo.bat",'x') as b:
    b.write(httpx.get("https://raw.githubusercontent.com/TerenceP1/trigger/refs/heads/main/gogogo.bat").text)

with open("cmd.py",'x') as b:
    b.write(httpx.get("https://raw.githubusercontent.com/TerenceP1/trigger/refs/heads/main/cmd.py").text)
