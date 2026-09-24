class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        n = len(nums)

        def back(i, remaining, cur):
            if remaining == 0:
                res.append(cur.copy())
                return
            
            for j in range(i, n):
                if nums[j] > remaining:
                    break
                cur.append(nums[j])
                back(j, remaining-nums[j], cur)
                cur.pop()

        back(0, target, []) 
        return res