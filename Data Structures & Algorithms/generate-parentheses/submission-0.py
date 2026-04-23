class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(left, right, s):

            #base case
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                helper(left+1, right, s+'(')

            if right < left:
                helper(left, right+1, s+')')
        
        helper(0, 0, "")
        return res
            

        