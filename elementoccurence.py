arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
occurrence_count = {}
for element in arr:
    if element in occurrence_count:
        occurrence_count[element] += 1
    else:
        occurrence_count[element] = 1

for element, count in occurrence_count.items():
    print(f"Element {element} occurs {count} times.")
