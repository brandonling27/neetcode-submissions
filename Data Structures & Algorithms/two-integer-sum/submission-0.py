class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_set= dict()
        for i in range(len(nums)):
            key = target - nums[i]
            if key in diff_set:
                return [diff_set[key], i]
            diff_set[nums[i]] = i
        return False
    '''
    [3,4,5,6], target = 7
    diff_set {3: 0, }
    key = 4
    '''

    '''
    [4,5,6], target = 10
    diff_set { 6:(4,0), 5:1, 4:2  }
    key = 5
    '''
