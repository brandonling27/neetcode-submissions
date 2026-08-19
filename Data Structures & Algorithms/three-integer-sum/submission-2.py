class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # [-1,0,1,2,-1,-4]
    # [-4,-1,-1,0,1,2]
        sortedNums = sorted(nums)
        res = []
        for i in range(len(sortedNums)):  
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            target = -sortedNums[i]
            j = i + 1
            k = len(sortedNums) - 1
            while j < k:
                if sortedNums[j] + sortedNums[k] < target:
                    j += 1
                elif sortedNums[j] + sortedNums[k] > target:
                    k -= 1
                else:
                    res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    j+=1
                    k-=1
                    while j < len(sortedNums) and sortedNums[j] == sortedNums[j-1]:
                        j+=1
        return res