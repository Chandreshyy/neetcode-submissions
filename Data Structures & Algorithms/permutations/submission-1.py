class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []

        def back(arr, cur):

            if len(cur) == n:
                res.append(cur.copy())
            
            for i in range(len(arr)):
                cur.append(arr[i])
                back(arr[:i] + arr[i+1:], cur)
                cur.pop()
            
        back(nums, [])
        return res
