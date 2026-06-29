class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        i, j = 0, n-1

        while i < j:
            total = numbers[i] + numbers[j]
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                return [i+1, j+1]
        return []
        
        