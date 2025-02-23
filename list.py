# Read input and convert to list of integers
num_list = list(map(int, input().split()))

# Remove duplicates and sort in descending order
unique_list = sorted(set(num_list), reverse=True)

# Print result
print(unique_list)


