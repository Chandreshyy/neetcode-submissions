import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        n = len(points)
        for i in range(n):
            x, y = points[i][0], points[i][1]
            dis = x*x + y*y
            heapq.heappush(min_heap, (dis, x, y))

        res = []
        for i in range(k):
            min_dis = heapq.heappop(min_heap)
            temp = [min_dis[1], min_dis[2]]
            res.append(temp)

            # i += temp_len

        return res

        