class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        res_set = set()
        n = len(nums)
        nums.sort()

        def back(i, cur):
            # print(f"i - {i}, cur- {cur}")
            if i == n:
                if tuple(cur.copy()) not in res_set:
                    res_set.add(tuple(cur.copy()))
                    res.append(cur.copy())
                return
            
            cur.append(nums[i])
            back(i+1, cur)
            cur.pop()
            back(i+1, cur)

        back(0, [])
        return res
        