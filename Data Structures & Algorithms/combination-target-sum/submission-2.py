class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(nums)

        def back(i, cur, cur_sum):
            # print(f"temp sum {temp_sum}, i- {i}")
            if i == n or cur_sum >= target:
                if cur_sum == target:
                    res.append(cur.copy())
                return
            
            for j in range(i, n):
                # print(f"cur before {cur}, {i}")
                cur.append(nums[j])
                # print(f"cur after {cur}, {i}")
                back(j, cur, cur_sum + nums[j])
                cur.pop()
        
        back(0, [], 0)
        return res