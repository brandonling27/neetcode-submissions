class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [3,4,5,6,1,2]
        l = 3
        r = 2
        mid = 4
        min = 2
        [4,5,0,1,2,3]
        '''
        l = 0
        r = len(nums) - 1
        minimum = float('inf')
        while (l < r): 
            print('left: ', l, '--', nums[l])
            print('right: ', r, '--', nums[r])
            mid = (l + r) // 2
            print('mid: ', mid, '--', nums[mid], '\n')
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]