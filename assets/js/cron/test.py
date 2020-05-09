import json
with open("../../data.json") as f:
    dic = json.load(f)
li = list(dic.keys())
for i in range(len(li)):
    if len(dic[li[i]]["2020-03-27"]) !=4 : 
        print("WRONG")
