# 20. Valid Parentheses  (Easy)
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    @classmethod
    def isValid(cls, s: str) -> bool:
        stack: list[str] = []
        matches: dict[str, str] = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for char in s:
            if matches.get(char): 
                stack.append(char)
            else:
                top: str = stack.pop() if stack else ""
                if not matches.get(top) == char:
                    return False
        return not stack

if __name__ =="__main__":
    print(Solution.isValid("("))