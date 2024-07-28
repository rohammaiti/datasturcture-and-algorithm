n = int(input("Enter the size of the array (excluding the missing number): "))

arr = list(map(int, input(f"Enter {n} numbers (from 1 to {n+1} with one missing): ").split()))

total_sum = (n + 1) * (n + 2) // 2
array_sum = sum(arr)
missing_number = total_sum - array_sum

print(f"The missing number is: {missing_number}")
