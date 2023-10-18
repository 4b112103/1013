#!/usr/bin/env python3

def findCh(istr, ch):
    pass
    # Write your code here!
    first = None
    last = None

    for i in range(len(istr)):
        if istr[i] == ch:
            if first is None:
                first = i
            last = i

    if first is None:
        return None
    elif first == last:
        return first
    else:
        return (first, last)

# --------------------------------------------------------------------
# The following code is intended for your personal testing purposes. 
# Feel free to modify it to meet your requirements.
# --------------------------------------------------------------------

def main():
    result = findCh("programming is fun and challenging", "g")
    print(result)
    result = findCh("programming is fun and challenging", "x")
    print(result)
    result = findCh("programming is fun and challenging", "s")
    print(result)

if __name__ == "__main__":
    main()