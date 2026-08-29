class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        # 當 left == right 時收斂，該位置即為最小值
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:# 斷崖在右側，最小值在 mid 右邊
                left = mid + 1
            else:  # 右半段正常遞增，最小值在 mid 左邊（包含 mid）
                right = mid

        return nums[left]
                