import praw
import requests
import json
import requests.auth

headers = {"Authorization": "bearer K26qHg2TX0ezepchk0iO4uBj0Tc","User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0"}

r= requests.get("https://oauth.reddit.com",headers=headers)
data = r.json()
print(data)
e
requests.post(url="""https://discordapp.com/api/webhooks/604070862064451600/_xEU6u03l31TQwREqIOQuTSoRyqqsid5pFHgkaNtMgDFEXgRetSanxr4tlkRmeMdb1ks""",data={"content":"HI"},headers=headers)
