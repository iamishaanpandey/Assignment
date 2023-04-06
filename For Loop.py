#For Loop in Python
exp = [3000,1900,1250,3550]
sum=0
for i in exp:
    sum+=i
print(sum)
total =0 
for i in range(len(exp)):
    print("Month :" , i+1 ,"Expense : ",exp[i])
    total+=exp[i]
print("My total expense is : ", total)

#Find the location of car key
key_loc= "chair"
loc= ["hall","bedroom","kitchen","chair","almirah"]
for i in loc:
    if i == key_loc:
        print("Key are at ",i)
        break

#print sqaure of all numbers between0 to 5 except even numbers
for i in range(0,6):
    if (i%2!=0):
        print(i**2)
#using while loop
i=1
while i<6:
    print(i**2)
