n=int(input("Enter the size of array-"))
arr=list(map(int, input("Enter elements- ").split()))
unique_element=set()
duplicates=[]

for i in arr:
    if i in unique_element:
        duplicates.append(i)
    else:
        unique_element.add(i)

if duplicates:
    print("Duplicates found- ", *duplicates)
else:
    print("Not found")
