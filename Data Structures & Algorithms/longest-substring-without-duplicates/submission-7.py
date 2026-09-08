from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''''
        abcabcbb
        left = 2
        right = 4
        res = 3 (right - left + 1)
        a: 0, b: 4, c: 2
    
        tmmzux
        catch
        res:  
        left:  0
        right:  -
        letterHolders:  defaultdict(
        <
        class
        'int'
        >
        , {'t': 0, 'm': 1,}) 
        dvdf
        d: 0, 
        '''
        letterHolders = set()
        left = 0
        right = 0
        res = 0
        for right in range(len(s)):
            while s[right] in letterHolders:
                letterHolders.remove(s[left])
                left+=1
            res = max(res, right-left+1)
            letterHolders.add(s[right])

        return res