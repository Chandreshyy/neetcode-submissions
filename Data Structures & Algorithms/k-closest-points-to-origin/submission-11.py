import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        mapp = {}
        min_heap = []
        n = len(points)
        for i in range(n):
            dis = (points[i][0])**2 + (points[i][1])**2
            if dis in mapp:
                mapp[dis].append(i)
            else:
                mapp[dis] = [i]
                heapq.heappush(min_heap, dis)

        # print(mapp)
        i = 0
        res = []
        while i < k:
            min_dis = heapq.heappop(min_heap)
            temp = mapp[min_dis]
            temp_len = len(temp)
            j = 0
            while j + i < k and j < temp_len:
                res.append(points[temp[j]])
                j = j + 1
            i += j
            # i += temp_len

        return res

        