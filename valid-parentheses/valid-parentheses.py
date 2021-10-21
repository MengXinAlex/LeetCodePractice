class Solution:
    def isValid(self, str: str) -> bool:
        s = []
        for i in str:
            if i == '(' or i == '[' or i == '{':
                s.append(i)
            if i == ')':
                if s == [] or s.pop() != '(':
                    return False
           
            if i == ']':
                if s == [] or s.pop() != '[':
                    return False
           
            if i == '}':
                if s == [] or s.pop() != '{':
                    return False
                
        return s == []