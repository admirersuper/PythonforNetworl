from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://192.168.3.5/include/auth_action.php")

postData = parse.urlencode([
    ("action", "logout"),
    ("username" ,"222015602053038"),
    ("password", "19970706"),
    ("ajax", "1"),
])
req.add_header("Host","192.168.3.5")
req.add_header("Origin","http://192.168.3.5")
req.add_header("Referer","http://192.168.3.5/srun_portal_pc.php?ac_id=1&")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36")
resp = urlopen(req,data = postData.encode('utf-8'))

print(resp.read().decode("utf-8"))
