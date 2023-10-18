#!/usr/bin/env python3

# import required libraries/modules
import re
def procTags(istr):
    pass
    # Write your code here!
    # Regular expression pattern to find text between <c> and </c> tags
    c_pattern = re.compile(r'<c>(.*?)<\/c>', re.IGNORECASE)
    
    # Regular expression pattern to find text between <r> and </r> tags
    r_pattern = re.compile(r'<r>(.*?)<\/r>', re.IGNORECASE)
    
    # Replace <c>...</c> tags with the uppercase version of the text inside
    istr = c_pattern.sub(lambda match: match.group(1).upper(), istr)
    
    # Replace <r>...</r> tags with the reversed version of the text inside
    istr = r_pattern.sub(lambda match: match.group(1)[::-1], istr)
    
    return istr


# --------------------------------------------------------------------
# The following code is intended for your personal testing purposes. 
# Feel free to modify it to meet your requirements.
# --------------------------------------------------------------------

data = [
    "<c>programming</c>123456789<r>987654321</r>python",
    "<c>university</c>9876543<r>7654321</r>education",
    "<c>engineering</c>12345<r>54321</r>innovation",
    "<c>technology</c>1234<r>4321</r>advancement",
    "<c>electronic</c>123<r>321</r>innovations",
]

def main():
    global data
    for i, td in enumerate(data, start=1):
        print(f"{i}: {td}")
        result = procTags(td)
        print(result)

if __name__ == "__main__":
    main()