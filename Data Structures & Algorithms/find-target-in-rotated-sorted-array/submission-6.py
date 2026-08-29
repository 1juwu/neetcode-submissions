class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        right = len(nums)-1
        left = 0

        while right >= left:

            mid = (right + left)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # 判斷左半段是否為正常遞增區間
                # target 剛好落在左半段的範圍內
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 3. 若否，則右半段必定是正常遞增區間
            else:
                # target 剛好落在右半段的範圍內
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # 找遍整個陣列都沒找到
        return -1
