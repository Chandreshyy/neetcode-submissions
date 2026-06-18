class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def solve(arr, index, comb, comb_set, n, nums):
            unq_tuple = tuple(sorted(arr))
            if unq_tuple not in comb_set:
                comb.append(arr[:])
                comb_set.add(unq_tuple)
            
            if index == n:
                return

            for i in range(index, n):

                arr.append(nums[i])
                solve(arr, i + 1, comb, comb_set, n, nums)
                arr.pop()

        comb = []
        comb_set = set()
        n = len(nums)  
        solve([], 0, comb, comb_set, n, nums)
        return comb
