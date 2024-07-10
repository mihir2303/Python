print("------Dictonary------")
dict = {"id":"1","name":"BCA"}
print(dict)
print(dict["name"])
print("------Length & OverWrite------")
dict = {"id":"1","name":"BCA","name":"BSCIT"}
print(dict)
print(len(dict))
print("------Keys------")
dict = {"id":"1","name":"BCA"}
x   = dict.get("id")
print(x)
print("------Values------")
x = dict.keys()
print(x)
print("------Append------")
dict["Result"] = "Fail"
print(x)
print("------Update------")
dict.update({"id":"2"})
print(dict)
print("------Update Method 2------")
dict = {"id":"1","name":"BCA"}
dict["name"] = "BSCIT"
print(dict)
print("------Update Method 3------")
dict.update({"Result":"Pass"})
print(dict)
print("------POP------")
dict = {"id":"1","name":"BCA","Result":"Pass"}
dict.pop("Result")
print(dict)
print("------POP Last Item------")
dict = {"id":"1","name":"BCA","Result":"Pass"}
dict.popitem()
print(dict)
print("------Delete Dict------")
del dict
print(dict)
print("------Delete 1 Item------")
dict = {"id":"1","name":"BCA","Result":"Pass"}
del dict["id"]
print(dict)
print("------Using Loop------")
dict = {"id:":"1","name:":"BCA","Result:":"Pass"}
for x in dict:
    print(x)
    print("------Print Values------")
for x in dict:
    print(dict[x])
print("------Print Values------")
for x in dict.values():
    print(x)
print("------Print Keys------")
for x in dict.keys():
    print(x)
print("------Print Keys & Values------")
for x,y in dict.items():
    print(x,y)