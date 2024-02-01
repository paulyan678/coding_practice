def vaild_par(str):
    stack = 0
    for char in str:
        if char == '(':
            stack += 1
        if char == ')':
            stack -= 1
            if stack < 0:
                return False
    
    if stack == 0:
        return True
    else:
        return False
    
print(vaild_par('((((()))'))