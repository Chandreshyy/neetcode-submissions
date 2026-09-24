class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        n = len(candidates)


        def back(i, remaining, cur):
            if remaining == 0:
                res.append(cur.copy())
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if remaining < candidates[j]:
                    break
                cur.append(candidates[j])
                back(j+1, remaining-candidates[j], cur)
                cur.pop()

        back(0, target, [])
        return res
        