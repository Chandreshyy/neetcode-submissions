class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        # print(nums)

        for i in range(n-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # print(total)
                if total > 0:
                    # print(nums[k])
                    k -= 1
                elif total < 0:
                    # print(nums[j])
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # break
                    while j < n -1  and nums[j] == nums[j+1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

        