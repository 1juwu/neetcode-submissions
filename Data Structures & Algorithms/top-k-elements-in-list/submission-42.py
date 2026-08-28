class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dist = {}

        for i in range(len(nums)):
            if nums[i] not in dist:
                dist[nums[i]] = 1 
            else:
                dist[nums[i]] += 1
        #print(dist)  

        dist = sorted(dist.items(), key=lambda x: x[1], reverse=True) 
        #print(dist) 
        ans = []

        for i in range(k):
            ans.append(dist[i][0])

        return ans

        