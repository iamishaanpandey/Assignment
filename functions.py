#function to print sum of lists
def calc_total(exp):
    total = 0
    for i in exp:
        total+=i
    return total

l1 = [1,2,3,4,5]
l2= [6,7,8,9,10]

l1_total = calc_total(l1)
l2_total = calc_total(l2)

print("l1 total is :",l1_total)
print("l2 total is :",l2_total)
print("total sum is ",l1_total+l2_total)

#sum of two numbers
def sum1(a,b):
    total = a+b
    return total

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
sum = sum1(a,b)
print(sum)