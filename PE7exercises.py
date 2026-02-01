# Task 1: Basic Range Sum
# Find the sum of all numbers from 1 to 20 inclusive.
def sum_to_twenty():
    total = 0
    # TODO: Loop from 1 to 20
   
    return total

# Task 2: Factorial of 5
# Calculate 5! (1 * 2 * 3 * 4 * 5). 
# Note: Start your product variable at 1, not 0!
def factorial_five():
    product = 1
    # TODO: Loop to calculate the product

    return product

# Task 3: Counting Characters
# Iterate through the string below and count how many times "e" appears.
def count_letter_e():
    text = "experience"
    count = 0
    # TODO: Loop through 'text' and check for "e"

    return count

# Task 4: The Even Accumulator
# Find the sum of all EVEN numbers between 1 and 30 inclusive.
def sum_evens():
    total = 0
    # TODO: Use range with a step or an if-statement

    return total

# Task 5: Countdown String
# Create a string that counts down from 5 to 1: "54321"
def countdown_string():
    result = ""
    # TODO: Use a range with a negative step

    return result

# Task 6: List Summation
# Sum all the numbers in the 'prices' list.
def sum_prices():
    prices = [10.50, 20.00, 5.25, 4.25]
    total = 0
    # TODO: Iterate through the list 'prices'

    return total

# Task 7: Finding the Maximum (Simple)
# Find the highest number in the list. 
# Hint: Compare each number to the 'current_max'.
def find_max():
    nums = [12, 45, 2, 67, 34, 18]
    current_max = nums[0]
    # TODO: Iterate through the list
    for num in nums:

    return current_max

# ==========================================
# AUTOCHECK - COMPARISON TABLE
# ==========================================
def run_tests():
    tasks = [
        {"name": "Task 1: Sum (1-20)", "act": sum_to_twenty(), "exp": 210},
        {"name": "Task 2: Factorial 5", "act": factorial_five(), "exp": 120},
        {"name": "Task 3: Count 'e'", "act": count_letter_e(), "exp": 4},
        {"name": "Task 4: Sum Evens", "act": sum_evens(), "exp": 240},
        {"name": "Task 5: Countdown", "act": countdown_string(), "exp": "54321"},
        {"name": "Task 6: Sum List", "act": sum_prices(), "exp": 40.0},
        {"name": "Task 5: Find Max", "act": find_max(), "exp": 67},
    ]

    print(f"\n{'EXERCISE':<25} | {'STATUS':<8} | {'YOURS':<10} | {'EXPECTED':<10}")
    print("-" * 65)

    for t in tasks:
        passed = str(t["act"]) == str(t["exp"])
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{t['name']:<25} | {status:<8} | {str(t['act']):<10} | {str(t['exp']):<10}")

if __name__ == "__main__":
    run_tests()
