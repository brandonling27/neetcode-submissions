class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencies = {}
        for c in s:
            if c not in frequencies:
                frequencies[c] = 1
            else:
                frequencies[c] += 1
        
        for c in t:
            if c not in frequencies:
                return False
            elif frequencies[c] == 1:
                del frequencies[c]
            else:
                frequencies[c] -= 1
        
        return len(frequencies.keys()) == 0