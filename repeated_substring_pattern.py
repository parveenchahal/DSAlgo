# https://leetcode.com/problems/repeated-substring-pattern/

# Method 1
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s[1:] + s[:-1])

# Method 2 (Using LPS(KMP))
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        lps = [0] * n
        j = 0
        i = 1
        while i < n:
            if s[j] == s[i]:
                lps[i] = j + 1
                i += 1
                j += 1
                continue
            elif j <= 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j - 1]
        print(lps)
        l = lps[-1]
        if l == 0:
            return False
        d = n - l
        return n % d == 0

# Method 3
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        tmp = ''
        tl = 0
        for i in range(n - 1):
            tmp += s[i]
            tl += 1
            if n % tl != 0:
                continue
            x = n // tl
            if (tmp * x) == s:
                return True
        return False
