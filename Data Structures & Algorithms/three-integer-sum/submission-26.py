class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums = sorted(nums)           
        # print(nums)

        for i in range(len(nums)-2):
            two_sum = 0 - nums[i]
            
            j = i + 1
            k = len(nums) - 1

            while (j < k):         
                if (nums[j] + nums[k]) < two_sum:
                    j += 1
                elif (nums[j] + nums[k]) > two_sum:
                    k -= 1
                else: # 剛好有match, 【指標要前進!】
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1 
            

        return list(set(tuple(item) for item in ans))
