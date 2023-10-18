#!/usr/bin/env python3

def findCh(istr, ch):
    pass
    # Write your code here!
    first = None
    last = None

    for i, char in enumerate(istr):
        if char == ch:
            if first is None:
                first = i
            last = i

    if first is not None and first != last:
        return f"{first} {last}"
    elif first is not None and first == last:
        return int(first)
    else:
        return None

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