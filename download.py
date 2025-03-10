import httpx
a=open("gogogo.bat",'x')
with a as b:
    b.write(bytes(httpx.get("https://raw.githubusercontent.com/TerenceP1/trigger/refs/heads/main/gogogo.bat").text,"utf-8"))

a=open("cmd.py",'x')
with a as b:
    b.write(bytes(httpx.get("https://raw.githubusercontent.com/TerenceP1/trigger/refs/heads/main/cmd.py").text,"utf-8"))
