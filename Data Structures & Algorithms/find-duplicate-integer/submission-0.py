class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        slow = 0
        fast = 0

        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        #     fast = nums[fast]
    
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow