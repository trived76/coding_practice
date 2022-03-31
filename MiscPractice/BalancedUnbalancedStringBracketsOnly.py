def check_balance(string):
    open_bracket = ["{", "(", "["]
    close_bracket = ["}", ")", "]"]

    brack_stack = list()
    for brack in string:
        if brack in open_bracket:
            brack_stack.append(brack)
        elif brack in close_bracket:
            idx = close_bracket.index(brack)
            if open_bracket[idx] == brack_stack[-1]:
                brack_stack = brack_stack[:-1]
            else:
                return "Unbalanced"
        
    if len(brack_stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

string = "{[]{()}}"
print(string,"-", check_balance(string))
  
string = "[{}{})(]"
print(string,"-", check_balance(string))
  
string = "((()"
print(string,"-",check_balance(string))