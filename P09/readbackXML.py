'''
External library
python -m pip install xmltodict
'''

import xmltodict
allFriend = {}
newFriend = {}
newFriend["nama"] = "Andi"
newFriend["umur"] = 20
newFriend["telp"] = "022-1231234"
allFriend["newFriend"] = newFriend
xml_str = xmltodict.unparse(allFriend, pretty=True)
print("Dictionary:")
print(allFriend)
print("XML:")
print(xml_str)
print("","","")
f = open("dict2xml.xml",'w')
f.write(xml_str)
f.close()

f = open("dict2xml.xml",'r')
xmlstr = f.read()
f.close()

friendDict = xmltodict.parse(xmlstr)
print(friendDict)
print(friendDict["newFriend"])
print(friendDict["newFriend"]["nama"])
print(friendDict["newFriend"]["umur"])
print(friendDict["newFriend"]["telp"])
xmlstr = xmltodict.unparse(friendDict, pretty=True)
print(xmlstr)

