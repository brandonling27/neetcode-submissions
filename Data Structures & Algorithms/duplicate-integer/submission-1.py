class Solution:
    # what pattersn does the input have?
    # what format is the output expected to be in?

    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))