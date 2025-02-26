import http.client
import json

conn = http.client.HTTPSConnection("192.168.28.118", 32771)
payload = json.dumps({
   "task_id": "5d273a55de6b4e1b935ebbfa79b97195"
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}
conn.request("POST", "/api/contracts/v3/parser/external/result", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))