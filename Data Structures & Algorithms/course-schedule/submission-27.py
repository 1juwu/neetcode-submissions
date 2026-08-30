class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 建立鄰接表（圖）：course -> [先修條件 / 接續課程]
        # [a, b] 代表修 a 之前必須先修 b (b -> a)
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        print(graph)
            
        # 2. 狀態紀錄：0 = 未走訪, 1 = 當前路徑走訪中, 2 = 已確認安全無環
        state = [0] * numCourses
        
        # 3. 定義 DFS 函式：檢查特定課程出發是否存在環
        def has_cycle(course):
            # 走到正在當前 DFS 路徑上的節點 -> 發現環！
            if state[course] == 1:
                return True
            # 已經檢查過且確認無環 -> 直接跳過
            if state[course] == 2:
                return False
            
            # 標記為「正在走訪中」
            state[course] = 1
            
            # 檢查這門課的所有先修課
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            
            # 底下全部檢查完畢都沒問題，標記為「已安全」
            state[course] = 2
            return False
        
        # 4. 檢查每一門課（因為可能由多個不相連的子圖組成）
        for course in range(numCourses):
            if has_cycle(course):
                return False  # 只要任何一門課存在環，就無法完成所有課程
                
        return True