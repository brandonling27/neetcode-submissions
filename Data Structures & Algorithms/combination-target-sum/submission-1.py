class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # array to store results 
        res = []
        self.doRecursion(res, [], sorted(nums), target)
        return res
        
    def doRecursion(self, res, curr, nums, target):
        for i in range(len(nums)):
            if sum(curr) + nums[i] < target:
                curr.append(nums[i])
                self.doRecursion(res, curr, nums[i:], target)
                curr.pop()
            elif sum(curr) + nums[i] == target:
                curr.append(nums[i])
                res.append(curr.copy())
                curr.pop()
            else:
                return
           
