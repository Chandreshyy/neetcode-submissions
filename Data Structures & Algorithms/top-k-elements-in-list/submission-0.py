class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        n = len(nums)
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        buckets =[[] for _ in range((n + 1))]
        print(buckets)
        for key in count:
            value = count[key]
            buckets[value].append(key)
        
        res = []
        for i in range(n, 0, -1):
            if len(buckets[i]) == 0:
                continue
            
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res

        return res            


            
        