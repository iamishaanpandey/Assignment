#creating a dictionary
d = {"a":1,"b":2,"c":3}
print(d)
#fetching value using key
print(d["a"])
#adding a key-value pair in dictionary
d["d"] = 4
print(d)
#del entry from dict
del d["c"]
print(d)
#print all the values of dict
for i in d:
    print(d[i])
#list can be used as a value of key 
d5 = {"company" : "pwskills" , "c": ["ds","ml","ai"]}
print(d5["c"])
#fetching keys
print(d5.keys())
#fetching values
print(d5.values())
