class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = []
        suffix = [1]
        prefix = [1]
        for i in range(1, n):
            suffix.append(nums[i-1]*suffix[i-1])
            prefix.append(nums[n-i]*prefix[i-1])
        print(suffix, prefix)
        for i in range(n):
            if nums[i] != 0:
                nums[i] = int(suffix[i]*prefix[n-1-i])
            else:
                nums[i] = int(suffix[i]*prefix[n-1-i])

        return nums
