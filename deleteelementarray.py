arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
position = int(input("Enter the position of the element you want to delete (0-indexed): "))

if position < 0 or position >= len(arr):
    print("Invalid position.")
else:
    new_arr = []
    for i in range(len(arr)):
        if i != position:
            new_arr.append(arr[i])
    
    print("Array after deletion:", new_arr)
