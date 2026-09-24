class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(nums)
        def cur_sum(cur):
            temp = 0
            for i in range(len(cur)):
                temp = temp + cur[i]
            return temp

        def back(i, cur):
            temp_sum = cur_sum(cur)
            # print(f"temp sum {temp_sum}, i- {i}")
            if i == n or temp_sum >= target:
                if temp_sum == target:
                    res.append(cur.copy())
                return
            
            for j in range(i, n):
                # print(f"cur before {cur}, {i}")
                cur.append(nums[j])
                # print(f"cur after {cur}, {i}")
                back(j, cur)
                cur.pop()
        
        back(0, [])
        return res