from collections import Counter

def minWindow( s: str, t: str):
    if t == '':
        return ''
    left = 0
    right = 0

    t_counts = Counter(t)
    required_num = len(t_counts)
    window_counts = dict()
    sat_num = 0

    sub_string_len = len(s) + 1

    
    
    while right < len(s):
        char = s[right]
        if char not in window_counts:
            window_counts[char] = 1
        else:
            window_counts[char] += 1
        
        if char in t_counts and t_counts[char] == window_counts[char]:
            sat_num += 1
        
        while right >= left and sat_num == required_num:
            if right - left + 1 < sub_string_len:
                sub_string = s[left:right+1]
                sub_string_len = len(sub_string)
            char = s[left]
            window_counts[char] -= 1
            if window_counts[char] < t_counts[char]:
                sat_num -= 1
            left += 1

        right += 1
    return sub_string

print(minWindow('abuwiehfdwefhidi', ''))
 