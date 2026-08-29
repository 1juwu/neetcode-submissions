"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        visited = {}

        def dfs(node):
            if node in visited: # 如果已經複製過，直接回傳對應的新節點
                return visited[node]
             # 若是新節點，則直接複製一個新的，並存進去visited
            copy = Node(node.val)
            visited[node] = copy # copy 現在是 1
            
            # 走訪所有鄰居，遞迴複製後加入到新節點的 neighbors 清單
            for nei in node.neighbors:
                # 1. 取得新鄰居節點
                new_neighbor = dfs(nei)

                # 2. 抓出目前節點的好友名單 (它是一個 list)
                copy.neighbors.append(new_neighbor)



                # copy.neighbors.append(dfs(nei))
                # dfs(nei) 負責去複製或抓回鄰居
                # copy.neighbors 若沒定義，她就是一個list
                # copy.neighbors.append(...)（負責接上好友關係）：

            return copy

        return dfs(node)

