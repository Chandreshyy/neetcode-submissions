class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def back(arr, nums, n, comb):
            if len(nums) == 0:
                comb.append(arr[:])
            
            for i in range(n):
                arr.append(nums[i])
                # print(nums[i])
                temp = nums[:i] + nums[i+1:]
                # print(temp)
                back(arr, temp, len(temp), comb)
                arr.pop()

        comb = []  
        back([], nums, len(nums), comb)
        return comb
        