class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1, 1, 2, 8]
        [48, 24, 6, 1]
        '''

        forward = [1 for _ in range(len(nums))]
        reverse = [1 for _ in range(len(nums))]
        res = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            forward[i] = nums[i-1]*forward[i-1]

        for i in range(len(nums) - 2, -1, -1):
            reverse[i] = nums[i+1]*reverse[i+1]

        for i in range(len(nums)):
            res[i]= forward[i] * reverse[i]
        
        return res
        

