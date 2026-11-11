# Galit, Antonia Chelsea D.
# Activity 6 - Recursion

# Sum the Array
def sum_array(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + sum_array(arr[1:])


# Find the Largest Number
def find_largest(arr):
    if len(arr) == 1:
        return arr[0]

    largest_rest = find_largest(arr[1:])

    if arr[0] > largest_rest:
        return arr[0]
    else:
        return largest_rest

# Count a Chosen Number
def count_number(arr, target):
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


print("===== RECURSIVE ARRAY TOOLKIT =====")

# Test 1: Sum the Array
print("\n1. SUM THE ARRAY")
print("Empty array:", sum_array([]))
print("One number:", sum_array([5]))
print("Several numbers:", sum_array([10, -5, 8, 2]))

# Test 2: Find the Largest Number
print("\n2. FIND THE LARGEST NUMBER")
print("One number:", find_largest([7]))
print("Largest at beginning:", find_largest([20, 5, 10, 3]))
print("Largest at end:", find_largest([4, 8, 12, 25]))
print("Negative numbers:", find_largest([-10, -3, -7, -1]))

# Test 3: Count a Chosen Number
print("\n3. COUNT A CHOSEN NUMBER")
print("Empty array:", count_number([], 5))
print("Target appears several times:", count_number([2, 5, 3, 5, 5, 8], 5))
print("Target does not appear:", count_number([1, 2, 3, 4], 9))