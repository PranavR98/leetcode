class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for ch in s:
            if ch not in hashmap:
                hashmap[ch] = 1
            else:
                hashmap[ch] += 1
        for ch in t:
            if ch not in hashmap:
                return False
            else:
                hashmap[ch] -= 1
                if hashmap[ch] == 0:
                    del hashmap[ch]
        if len(hashmap) == 0:
            return True