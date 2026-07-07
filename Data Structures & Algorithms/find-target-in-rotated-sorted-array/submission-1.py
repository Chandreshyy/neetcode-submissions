class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, h = 0, len(nums) - 1

        while l <= h:
            mid = l + (h-l)//2
            if nums[mid] == target:
                    return mid
            if nums[mid] > nums[h]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if target < nums[mid] or target > nums[h]:
                    h = mid - 1
                else:
                    l = mid + 1
        return -1


        