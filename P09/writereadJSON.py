import json
allFriend = {}
newFriend = {}
newFriend["nama"] = "Andi"
newFriend["umur"] = 20
newFriend["telp"] = "022-1231234"
allFriend["newFriend"] = newFriend
json_str = json.dumps(allFriend)
print(json_str)
f = open("dict2json.json",'w')
f.write(json_str)
f.close()

f = open("dict2json.json",'r')
jsonstr = f.read()
f.close()
print(jsonstr)
myfriend = json.loads(jsonstr)
print(myfriend)


