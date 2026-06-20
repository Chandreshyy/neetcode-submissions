class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        arr_set = set()
        # n = len(nums)
        for i in nums:
            if i not in arr_set:
                arr_set.add(i)
            else:
                return True
        
        return False