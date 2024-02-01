digits_letter_map = {
    '2':['a', 'b', 'c'],
    '3':['d', 'e', 'f'],
    '4':['g', 'h', 'i'],
    '5':['j', 'k', 'l'],
    '6':['m', 'n', 'o'],
    '7':['p', 'q', 'r', 's'],
    '8':['t', 'u', 'v'],
    '9':['w', 'x', 'y', 'z']

} 

# 
def letterCombinations(digits):
    return letterCombinationsRecurse(digits)

def letterCombinationsRecurse(digits, cur_pos = 0):
    if len(digits) - 1 == cur_pos:
        return digits_letter_map[digits[cur_pos]]
    sub_prob = letterCombinationsRecurse(digits, cur_pos + 1)
    res = []
    for letter in digits_letter_map[digits[cur_pos]]:
        for sub in sub_prob:
            res.append(letter + sub)
    return res

print(letterCombinations('23'))

class sol:
    def __init__(self) -> None:
        pass