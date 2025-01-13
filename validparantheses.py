##Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#Input: s = "()"
#Output: true
#Input: s = "(]"
#Output: false

def isvalid(s):
    stack =[] ## initialized a empty stack
    mapping={')':'(',']':'[','}':'{'} ## mapping closoing to opening bracket
    ## loop through each character in string 
    for char in s:
        if char in mapping: ## if it is closoing bracket 
            if stack and stack[-1] == mapping[char]: ## check if the top of the stack matches
                stack.pop() ## pop the stack if mathces
            else:
                return False ## Return false if not matches
        else:
            stack.append(char) ## if it is opening bracket push to the stack
    return not stack ## if stack is empty at the end , return True valid string

y=isvalid("[]")
print(y)