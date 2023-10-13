**Exercise 1: Divisibility Checker in Python**

Create a Python script that accepts a series of integers from the user as a single line of space-separated values. The task is to identify and print the numbers that are divisible by either 3 or 7 while maintaining the original order. If there are no such divisible numbers, the program should print "None" as the result.

*Testing in the Command Prompt:*
```
$ echo 34 45 22 32 23 58 48 28 74 4 53 49 19 74 24 | python main.py 
45 48 28 49 24
```

*Testing with Input/Output Redirection:*
```
cat data.txt | python main.py 
28 7 39 14 49 48 93 15 69
```

*Testing with testing script:*
```
$ python testing.py 
Input: 17 1 28 67 7 19 4 39 14 58 92 37 4 50
Input: 94 49 1 48 93 100 58 15 10 69 26
Input: 19 18 26 61 95 62 96
Input: 34 45 22 32 23 58 48 28 74 4 53 49 19 74 24
Input: 13 43 78 96 74
Input: 29 43 53 52 14 44 95
Input: 54 86 11 29 71 50 13 5 62 86 30 25
Input: 38 50 100 75 39
Input: 17 20 85 98 53 3 92 99 24 28 96 9
Input: 93 93 32 87 81 23 17 41 91 83 67 90 37
.
----------------------------------------------------------------------
Ran 1 test in 0.269s

OK
```
