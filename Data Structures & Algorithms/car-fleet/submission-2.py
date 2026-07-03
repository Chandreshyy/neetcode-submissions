class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        pos_time = []
        stack = []
        
        for i in range(n):
            pos_time.append((position[i], (target - position[i])/speed[i]))
        
        pos_time.sort(reverse=True)
        for i in range(n):
            pos, time = pos_time[i]
            # print(pos, time)
            if not stack or stack[-1] < time:
                stack.append(time)
        # print(pos_time)

        return len(stack)