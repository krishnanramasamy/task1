# find even numbers and odd numbers 
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# prime numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
prime_count = len(prime_numbers)
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)


# happy numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

happy_numbers = [num for num in numbers if is_happy_number(num)]
happy_count = len(happy_numbers)
print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", happy_count)


# Function to find the sum of the first and last digit
def sum_first_last(num):
    last_digit = num % 10
    while num >= 10:
        num //= 10
    first_digit = num
    return first_digit + last_digit

number = 98764
result = sum_first_last(number)
print(f"The sum of the first and last digits of {number} is: {result}")


# Function to find the minimum difference between max and min mangoes for M students
def min_mango_diff(mangoes, M):
    # Sort the list of mangoes in ascending order
    mangoes.sort()
    
    # Initialize the minimum difference to a large number
    min_diff = float('inf')
    
    # Traverse the sorted list and check the difference for all possible sublists of size M
    for i in range(len(mangoes) - M + 1):
        # Difference between the max and min in the current sublist of size M
        diff = mangoes[i + M - 1] - mangoes[i]
        
        # Update the minimum difference
        if diff < min_diff:
            min_diff = diff
    
    # Return the minimum difference
    return min_diff

# Example
mangoes = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28]
M = 5  # Number of students

result = min_mango_diff(mangoes, M)
print(f"The minimum difference between the maximum and minimum number of mangoes is: {result}")



# Given three lists
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 10]
list3 = [7, 8, 9, 10, 11, 12]

# Convert the lists to sets and find the intersection
duplicates = set(list1) & set(list2) & set(list3)
# Output the common duplicates
print("Duplicates in the three lists:", list(duplicates))



# Function to find the first non-repeating element
def first_non_repeating(lst):
    # Create a dictionary to store the frequency of elements
    count_dict = {}

    # Count the occurrences of each element
    for num in lst:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find the first element with count 1
    for num in lst:
        if count_dict[num] == 1:
            return num

    # If no non-repeating element is found
    return None

# Example
lst = [9, 4, 9, 6, 7, 4, 6, 10]
result = first_non_repeating(lst)
if result:
    print(f"The first non-repeating element is: {result}")
else:
    print("There are no non-repeating elements.")



# Function to find the minimum element in a rotated sorted list
def find_min_in_rotated_sorted_list(nums):
    left, right = 0, len(nums) - 1

    # If the list is not rotated (sorted in increasing order)
    if nums[left] < nums[right]:
        return nums[left]

    # Perform binary search
    while left < right:
        mid = (left + right) // 2

        # If the middle element is greater than the rightmost element,
        # it means the minimum is to the right of mid
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid  # The minimum is either at mid or to the left of mid

    # When the loop ends, left == right, which will be the index of the smallest element
    return nums[left]

# Example
rotated_sorted_list = [6, 7, 9, 15, 19, 2, 3]

# Call the function and print the result
result = find_min_in_rotated_sorted_list(rotated_sorted_list)
print(f"The minimum element in the rotated sorted list is: {result}")




# Function to find a triplet with the given sum
def find_triplet_with_sum(lst, target_sum):
    # Sort the list first
    lst.sort()

    # Traverse the list and use two pointers to find the triplet
    for i in range(len(lst) - 2):
        # Set left and right pointers
        left = i + 1
        right = len(lst) - 1

        # Check for the triplet
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            
            # If the sum matches the target, return the triplet
            if current_sum == target_sum:
                return (lst[i], lst[left], lst[right])
            
            # If the current sum is less, move the left pointer to the right to increase the sum
            elif current_sum < target_sum:
                left += 1
                
            # If the current sum is more, move the right pointer to the left to decrease the sum
            else:
                right -= 1

    # If no triplet is found, return None
    return None

# Example list and target sum
lst = [10, 20, 30, 9]
target_sum = 59

# Call the function and print the result
result = find_triplet_with_sum(lst, target_sum)

if result:
    print(f"Triplet found: {result}")
else:
    print("No triplet with the given sum found.")




# Function to check if there is a sub-list with sum equal to zero
def has_zero_sum_sublist(lst):
    # Create a set to store cumulative sums
    cumulative_sum_set = set()
    cumulative_sum = 0

    # Iterate through the list
    for num in lst:
        # Add the current number to the cumulative sum
        cumulative_sum += num
        
        # Check if the cumulative sum is zero or has been seen before
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True
        
        # Add the cumulative sum to the set
        cumulative_sum_set.add(cumulative_sum)

    # If no zero-sum sub-list is found, return False
    return False

# Example list
lst = [4, 2, -3, 1, 6]

# Call the function and print the result
result = has_zero_sum_sublist(lst)

if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
