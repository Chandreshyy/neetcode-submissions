class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        arr_set = set()

        first_index = 0
        sec_index = 1

        for i in range(n):
            if target - nums[i] in arr_set:
                sec_index = i
                break
            arr_set.add(nums[i])

        print(sec_index)
        for j in range(n):
            if j != sec_index and target -  nums[j] == nums[sec_index]:
                first_index = j
                print(first_index)

        return [first_index, sec_index]