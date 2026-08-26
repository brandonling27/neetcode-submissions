from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        for n in sorted(nums):
            if n - 1 in num_map:
                num_map[n] = num_map[n-1] + 1
            elif n not in num_map:
                num_map[n] = 1
        maxLength = 0
        for n in num_map:
            maxLength = max(maxLength, num_map[n])
        return maxLength