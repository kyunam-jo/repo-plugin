import requests, time
r = requests.post('http://requestb.in/17s7e6c1', data={"ts":time.time()})
print r.status_code
print r.content
