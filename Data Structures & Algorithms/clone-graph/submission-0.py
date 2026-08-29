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
            visited[node] = copy
            
            # 走訪所有鄰居，遞迴複製後加入到新節點的 neighbors 清單
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

