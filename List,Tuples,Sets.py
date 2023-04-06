#List in python
item = ["bread","chips","cold-drink"]
print(item[0])
#Change item at an index
item[0]="choclates"
print(item)
#print particular sequence of items
print(item[0:2])
#Append an item in a list
item.append("butter")
print(item)
#Insert item at a particular index
item.insert(3,"milkshake")
print(item)
#Adding two lists
bathroom = ["shampoo","powder"]
item+=bathroom
print(item) 
#printing length of a list
print(len(item))
#finding if an item exists in a list
print("bread" in item)
#extend function
item.extend("bread")
print(item)
#delete a index item
item.pop(3) #--uses a index
print(item)
item.remove("chips")  #--uses a occurence a element
print(item)
#reverse a list
item.reverse()
print(item)
#sort a list
l1 = [1,3,5,6,7,8,5,4,6,8,9]
l1.sort()
print(l1)
#tells the index of a itme
print(l1.index(3))
#counts number of occurences
print(l1.count(8))
#replacing a string value [NOTE - IT CREATES A NEW MEMORY LOCATION AND DOESN'T EFFECT THE ORIGNAL STRING]
a = "Ishaan"
print(a.replace("I","D"))
print(a)
#removing duplicates
print(list(set(l1)))
#adding 1 to all elements
l2 = [1,2,3,4,5,6]
for i in range(len(l2)):
    l2[i]+=1
print(l2)

#Tuple
#creating a tuple
s = (1,2,3,4,5,[1,2,3,4])

#Set
s = {1,2,3,4,5}
s.add(40)
print(s)

