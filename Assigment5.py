ls= []
sum=0
n= int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    ls.append(ele) 
print(ls)

print("Sum of all elements in given list: ", ls)
print(min(ls))
print(max(ls))
ls.sort(reverse=True)
print(ls)
ls.sort(reverse=False)
print(ls)
l1=[1,2,3]
t1=tuple(l1)
print(t1)
del t1
print(t1)
 
