class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_seq = 0
        unq_set = set()
        for i in range(n):
            unq_set.add(nums[i])
        print(unq_set)
        for i in range(n):
            cur = nums[i]
            seq = 1
            print(cur)
            while True:
                if cur+1 in unq_set:
                    seq+=1
                    cur+=1
                    continue
                break
            max_seq = max(max_seq, seq)
        return max_seq
            


        