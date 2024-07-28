arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
element_count = {}

for elem in arr:
    if elem in element_count:
        element_count[elem] += 1
    else:
        element_count[elem] = 1

first_non_repeating = None
for elem in arr:
    if element_count[elem] == 1:
        first_non_repeating = elem
        break

if first_non_repeating is not None:
    print("The first non-repeating element is:", first_non_repeating)
else:
    print("No non-repeating element found.")
