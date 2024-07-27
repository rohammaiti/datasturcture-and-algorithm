arr = list(map(int, input("Enter elements- ").split()))

new_element=int(input("Enter new element- "))
position = int(input("Enter the position- "))

if(position<0 or position>len(arr)):
    print("Invalid")

else:
    new_arr=[]
    for i in range(len(arr)+1):
        if i<position:
            new_arr.append(arr[i])

        elif i==position:
            new_arr.append(new_element)
        else:
            new_arr.append(arr[i-1])

    print("Array after insertion:", new_arr)
