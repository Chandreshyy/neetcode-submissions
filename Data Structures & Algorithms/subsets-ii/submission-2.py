class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def solve(arr, index, comb, n, nums):
            if index == n:
                comb.append(arr[:])
                return

            # Pick the current element
            arr.append(nums[index])
            solve(arr, index + 1, comb, n, nums)
            arr.pop()

            # Skip duplicates for the 'not pick' branch
            next_index = index + 1
            while next_index < n and nums[next_index] == nums[index]:
                next_index += 1
            
            solve(arr, next_index, comb, n, nums)

        comb = []
        n = len(nums)  
        nums.sort()
        solve([], 0, comb, n, nums)
        return comb

        