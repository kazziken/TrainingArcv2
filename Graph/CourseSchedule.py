
def course_schedule(self, numCourses, prereq):
    
    previous_map = { i : [] for i in range(numCourses) }
    
    for crs, pre in prereq:
        previous_map[crs].append(pre)
        
    visited_set = set()
    
    def dfs(crs):
        
        if crs in visited_set:
            return False 
        
        if previous_map[crs] == []:
            return True
        
        visited_set.add(crs)
        #check if prereq return False and not in visited_set
        for pre in previous_map[crs]:
            if not dfs(pre):
                return False
        
        visited_set.remove(crs)
        previous_map[crs] = []
        return True
    
    for crs in previous_map[crs]:
        if not dfs(crs):
            return False
    return True