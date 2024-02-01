def longestValidParentheses(string):
    maxlen = 0
    stack = []
    p = -1

    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                p = i
            else:
                left_ind = stack.pop()
                if len(stack) == 0:
                    maxlen = max(maxlen, i - p)
                else:
                    maxlen = max(maxlen, i-left_ind + 1)
    return maxlen



