class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        dict = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for a,b in zip(s, s[1:]):
            print(a,b)
            if dict[a] < dict[b]:
                res -= dict[a]
            else:
                res += dict[a]

        return res + dict[s[-1]]