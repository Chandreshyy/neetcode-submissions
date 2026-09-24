class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)

        def back(index, cur):
            if index == n:
                res.append(cur.copy())
                return
            back(index + 1, cur)
            cur.append(nums[index])
            back(index + 1, cur)
            cur.pop()
        cur = []
        back(0, cur)

        return res
