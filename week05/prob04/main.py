#! /usr/bin/env python3

# Write your code here
def variance(numbers):
    # Check if the input list has fewer than 2 elements and return None
    if len(numbers) < 2:
        return None
    
    # Calculate the mean (average) of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the squared differences and store them in a list
    squared_differences = [(x - mean) ** 2 for x in numbers]
    
    # Calculate the variance using the formula
    variance = sum(squared_differences) / (len(numbers) - 1)
    
    return variance

# Input the list of integers
input_numbers = [int(x) for x in input().split()]

if __name__ == "__main__":
    result = variance(input_numbers)
    if result is not None:
        print(result)
    else:
        print(None)
