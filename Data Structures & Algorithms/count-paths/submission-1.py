class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = dict()

        def inBounds(x,y):
            return (0 <= x < m) and (0 <= y < n)

        def dfs(x,y):
            #print(x,y)
            if x == m -1 and y == n-1:
               # print('here: ', (x,y))
                return 1
            if not inBounds(x,y):
                #print('not in bounds')
                return 0
            if (x,y) in seen:
                return seen[(x,y)]
            seen[(x,y)] = dfs(x+1, y) + dfs(x, y+1)
            return seen[(x,y)]

        # X X
        # X X

        # seen=
        '''
        (0,0) =1 
        (1,0) = 2
        (0,1) = 2
        
        '''
        
        return dfs(0,0)
       # return seen[(m-1, n-1)]
