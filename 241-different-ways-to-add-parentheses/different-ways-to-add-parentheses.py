class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def recurse(start, end):
            key = (start, end)
            if key in memo:
                return memo[key]
            cur_str = expression[start:end]
            if cur_str.isdigit():
                memo[key] = [int(cur_str)]
                return memo[key]
            
            results = []
            for k in range(start, end):
                char = expression[k]
                if char in '+-*':
                    left_res = recurse(start, k)
                    right_res = recurse(k + 1, end)
                    for l in left_res:
                        for r in right_res:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)

            memo[key] = results
            return memo[key]

        return recurse(0, len(expression))
