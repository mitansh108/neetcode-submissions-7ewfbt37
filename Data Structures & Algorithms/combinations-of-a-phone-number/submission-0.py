class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        check = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }
        res = []
        if not digits:
            return []
        def helper(index, sub):

            

            if index >= len(digits):
                res.append("".join(sub))
                return

            for c in check[digits[index]]:
                sub.append(c)
                helper(index+1, sub)
                sub.pop()
        
        helper(0, [])
        return res

        