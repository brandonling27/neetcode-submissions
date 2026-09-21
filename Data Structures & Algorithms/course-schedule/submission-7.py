class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ''' 
        create a graph?
        adjacency matrix

        1:0
        0:1
        seen set => if we already saw it then it's not allowed
        way to track num courses

        numCourses = 2, prerequisites = [[0,1],[1,2],[2,4]]
        1->0
        2->1
        4->3

        4->2->1->0
        4->3 2->1->0
        '''
        course_map = {i:[] for i in range(numCourses)}
        # create adjaceny map
        for c, preq in prerequisites:
            course_map[c].append(preq)
        seen = set()

        #print(course_map)
        def doDFS(course):
            #print('course: ', course)
            if course in seen:
                return False
            if course_map[course] == []:
                return True
            seen.add(course)
            for c in course_map[course]:
                if not doDFS(c): return False
            seen.remove(course) # why??
            course_map[course] = []
            return True 

        for c in range(numCourses):
            if not doDFS(c): return False
        return True
        # how do i know where to start?



        