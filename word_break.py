def word_break(str, wordDict):
    memo = {}
    def recurse(sub_str):
        if sub_str in memo:
            return memo[sub_str]
        
        if len(sub_str) == 1:
            memo[sub_str] = sub_str in wordDict
            return memo[sub_str]
        if sub_str in wordDict:
            memo[sub_str] = True
            return True
        res = False
        for i in range(1, len(sub_str)):
            left_str = sub_str[:i]
            right_str = sub_str[i:]
            left_word_break = recurse(left_str)
            right_word_break = recurse(right_str)
            res = res or (left_word_break and right_word_break)
        memo[sub_str] = res
        return res
    return recurse(str)
    

wordDict = ["apple", "pen"]
str = "applepenapplepen"
print(word_break(str, wordDict))

