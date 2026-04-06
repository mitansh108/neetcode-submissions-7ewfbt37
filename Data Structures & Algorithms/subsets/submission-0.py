class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return None
            
            #decision to add it to the tree
            subset.append(nums[i])
            dfs(i+1)

            #decision not to add it to tree
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return ans