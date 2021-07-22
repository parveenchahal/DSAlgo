# https://leetcode.com/problems/stickers-to-spell-word/

class Solution:
    
    def _get_remaining(self, curr, x):
        count = [0] * 26
        for c in curr:
            i = ord(c) - ord('a')
            count[i] += 1
        for c in x:
            i = ord(c) - ord('a')
            if count[i] > 0:
                count[i] -= 1
        res = []
        for i in range(26):
            if count[i] > 0:
                res.append(chr(ord('a') + i) * count[i])
        return ''.join(res)
    
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_set = set(list(target))
        graph = {}
        for s in stickers:
            for x in set(s):
                if x in target_set:
                    try:
                        graph[x].append(s)
                    except KeyError:
                        graph[x] = [s]
        
        q = deque()
        visited = set()
        
        r = self._get_remaining(target, '')
        q.append((r, 0))
        
        while len(q) > 0:
            x, d = q.popleft()
            for s in stickers:
                r = self._get_remaining(x, s)
                if r == '':
                    return d + 1
                if r not in visited:
                    q.append((r, d + 1))
                    visited.add(r)
        return -1
