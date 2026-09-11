import heapq

class Solution:
    '''
    nums = [2,3,1,5,4], k = 2
    heap = [1, 2, 3, 4, 5]
    len = 5 
    index = 5 - 2 = 3
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # defaults to minheap
        popN = len(nums) - k + 1 # 3
        res = 0
        while popN > 0:
            res = heapq.heappop(nums)
            popN-=1
        return res

