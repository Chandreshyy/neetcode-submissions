class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, h = 0, len(nums) - 1
        mine = nums[0]

        while l <= h:
            mid = l + (h-l)//2
            # print(l, mid, h)
            # print(nums[l], nums[mid], nums[h])
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                mine = min(nums[h], mine, nums[mid])
                h = mid - 1

        return mine