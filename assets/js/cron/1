import requests
from datetime import *
import json

r = requests.get("https://api.covid19india.org/v2/state_district_wise.json")
anna = r.json()
banna = {}
for i in anna:
    if i['state'] == "Tamil Nadu":
        banna = i["districtData"]

with open("../../data/tn_data.json") as f:
    data = json.load(f)

tod = date.today()
string = tod.strftime("%Y-%m-%d")
translate = {
        'Viluppuram' : 'Villupuram',
        'Thirunelveli': 'Tirunelveli',
        'Tiruchirappalli' : 'Tiruchirapalli',
        'Kancheepuram': 'Kanchipuram',
        'Krishna' : 'Krishnagiri',
        'The Nilgiris' : 'Nilgiris',
        'Sivaganga' : 'Sivagangai',
        'Virudhunagar' : 'Virudhnagar',
        'Thoothukkudi': 'Thoothukudi'
}
print(type(banna))
for i in range(len(banna)):
    name = banna[i]['district']
    if data.get(name) is not None:
        data[name][string] = [banna[i]['confirmed'],0,0,0]
    elif translate.get(name) is not None:
        if data.get(translate[name]) is not None:
            data[translate[name]][string] = [banna[i]['confirmed'],0,0,0]
        
key =list(data.keys())
print(key)
for i in range(len(key)):
    if data[key[i]].get(string) is None:
        data[key[i]][string] = [0,0,0,0]
print(data)
f.close()
with open("../../data/tn_data.json","w") as f:
    json.dump(data,f,indent=6)
