array_size = int(input("Enter the size of the array: "))
array = [int(x) for x in input("Enter the elements separated by spaces: ").split()]

element_to_find = int(input("Enter the element to find: "))
found = False

for i in range(len(array)):
    if array[i] == element_to_find:
        found = True
        index = i
        break

if found:
    print(f"Element found at index {index}")
else:
    print("Element not found in the array")
