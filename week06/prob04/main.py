#!/usr/bin/env python3

def replaceOdd(istr):
    pass
    # Write your code here!
    # Initialize a counter for tracking the occurrences of 'h'
    h_count = 0
    # Initialize an empty result string
    result = ""

    # Loop through each character in the input string
    for char in istr:
        if char == 'h':
            # Increment the count for each 'h' found
            h_count += 1
            # Replace 'h' with 'H' for odd occurrences (1-based index)
            if h_count % 2 == 1:
                char = 'H'
        result += char

    return result
# --------------------------------------------------------------------
# The following code is intended for your personal testing purposes. 
# Feel free to modify it to meet your requirements.
# --------------------------------------------------------------------

data = [
    "hello world",
    "hello "*10,
    "hH"*10,
    "Hello",
    "hHhHhHhH",
    "123h456h789",
    "abcdefg",
    "hhhhhhhhhhhhhhhhhhhh",
    "HhHhHhHhHhHhHhHhHh",
    "1h2h3hHHH4h5hHHH6h7h8hHHH9h"
]    

def main():
    for ss in data:
        result = replaceOdd(ss)
        print(result)

if __name__ == "__main__":
    main()