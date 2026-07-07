import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def can_finish(k):
            cur = 0
            for i in range(n):
                cur += math.ceil(piles[i]/k)
            return cur <= h
        
        maxk = max(piles)
        mink = maxk
        low, high = 1, maxk
        while low <= high:
            mid = low + (high-low)//2
            print(low, mid, high)
            _can_finish = can_finish(mid)
            print(_can_finish)
            if _can_finish:
                mink = mid
                high = mid - 1
            else:
                low = mid + 1

        return mink
            