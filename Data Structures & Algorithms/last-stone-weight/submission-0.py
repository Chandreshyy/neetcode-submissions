import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x != y:
                new_stone = y - x
                heapq.heappush(stones, -new_stone)
        
        if len(stones) == 0:
            return 0
        return -stones[0]


        
        