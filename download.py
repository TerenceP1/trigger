import httpx
a=open("gogogo.bat",'x')
with a as b:
    b.write(httpx.get("https://raw.githubusercontent.com/TerenceP1/trigger/refs/heads/main/gogogo.bat").text)

a=open("cmd.py",'x')
with a as b:
    b.write(httpx.get("https://raw.githubusercontent.com/TerenceP1/trigger/refs/heads/main/cmd.py").text)
