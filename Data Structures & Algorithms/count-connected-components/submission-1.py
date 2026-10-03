from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make a dict
        edgesDict = defaultdict(list)
        for i, j in edges:
            edgesDict[i].append(j)
            edgesDict[j].append(i)

        """
        0:3
        1:4
        seen = 
        totals = 

        """
        
        seen = set() # 0,1,2,3,
        totals = 0
        def dfs(i):
            seen.add(i)
            for j in edgesDict[i]:
                if j not in seen:
                    dfs(j)
            return

        for n in range(n):
            if n not in seen:
                dfs(n)
                totals+=1
        return totals
                
                
            

