class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        res = []
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            print(s[i], s[j])
            l = int(s[i:j])
            # print(l)
            word = s[j+1:j+l+1]
            # print(word)
            j = j + l + 1
            res.append(word)
            i = j
            # print(s[i])
        return res
