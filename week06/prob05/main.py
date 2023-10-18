#!/usr/bin/env python3

# import required libraries/modules

def procTags(istr):
    pass
    # Write your code here!
    result = ""
    # Initialize an empty stack to keep track of the currently open tags
    tag_stack = []
    
    i = 0
    while i < len(istr):
        # If we encounter an opening tag "<", check for "<c>" or "<r>"
        if istr[i] == "<":
            tag_end = istr.find(">", i)  # Find the closing ">" of the tag
            if tag_end != -1:
                tag = istr[i+1:tag_end]  # Extract the tag content
                if tag == "c":
                    tag_stack.append("c")  # Push "c" onto the stack
                elif tag == "r":
                    tag_stack.append("r")  # Push "r" onto the stack
                i = tag_end + 1  # Move the pointer to the character after ">"
            else:
                # If there's no closing ">", just append the character and move on
                result += istr[i]
                i += 1
        # If we encounter a closing tag "</", check for "</c>" or "</r>"
        elif istr[i:i+2] == "</":
            tag_end = istr.find(">", i)  # Find the closing ">" of the tag
            if tag_end != -1:
                tag = istr[i+2:tag_end]  # Extract the tag content
                if len(tag_stack) > 0:
                    current_tag = tag_stack.pop()  # Pop the top tag from the stack
                    if tag == current_tag:
                        if tag == "c":
                            # Convert text between <c> and </c> to capital letters
                            result += istr[i+2:tag_end-3].upper()
                        elif tag == "r":
                            # Reverse text between <r> and </r>
                            result += istr[i+2:tag_end-3][::-1]
                    else:
                        # If there's a mismatch between opening and closing tags, just append the character
                        result += istr[i]
                i = tag_end + 1  # Move the pointer to the character after ">"
            else:
                # If there's no closing ">", just append the character and move on
                result += istr[i]
                i += 1
        else:
            # If it's not a tag, just append the character
            result += istr[i]
            i += 1

    return result

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