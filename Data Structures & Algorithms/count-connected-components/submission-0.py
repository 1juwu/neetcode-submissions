class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # 找老大
        parent = list(range(n))
        count = n  # 一開始有 n 個獨立集合

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # 路徑壓縮
            return parent[x]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            # 老大不同，合併兩個集合，總集合數 - 1
            if root_u != root_v:
                parent[root_u] = root_v
                count -= 1

        return count