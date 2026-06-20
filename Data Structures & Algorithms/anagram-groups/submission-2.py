class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)
        str_dict = {}
        res = []
        if len(strs) == 0:
            return [[""]]

        for i in range(n):
            temp = [0]*26

            for ch in strs[i]:
                index = ord(ch) - ord('a')
                temp[index] += 1
            
            key = tuple(temp)
            if key in str_dict:
                str_dict[key].append(strs[i])
            else:
                str_dict[key] = [strs[i]]
            
        for key in str_dict:
            res.append(str_dict[key])

        return res
        

            
