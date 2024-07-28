def rearrange_alternating(arr):
    positives = [num for num in arr if num >= 0]
    negatives = [num for num in arr if num < 0]
    
    min_len = min(len(positives), len(negatives))
    
    result = []
    
    for i in range(min_len):
        result.append(negatives[i])
        result.append(positives[i])
    
    if len(positives) > min_len:
        result.extend(positives[min_len:])
    
    if len(negatives) > min_len:
        result.extend(negatives[min_len:])
    
    arr[:len(result)] = result

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

rearrange_alternating(arr)

print("Rearranged array:", arr)
