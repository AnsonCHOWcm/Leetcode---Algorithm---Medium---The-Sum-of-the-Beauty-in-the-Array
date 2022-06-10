class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:

        score = 0

        n = len(nums)

        min_ = [None for i in range(n)]
        max_ = [None for i in range(n)]

        left_max = float('-inf')
        right_min = float('inf')

        for i in range(n):
            max_[i] = left_max
            left_max = max(nums[i], max_[i])

            min_[n - 1 - i] = right_min
            right_min = min(nums[n - 1 - i], min_[n - 1 - i])

        for i in range(1, n - 1):

            if (nums[i] > max_[i] and nums[i] < min_[i]):

                score += 2

            elif (nums[i] > nums[i - 1] and nums[i] < nums[i + 1]):

                score += 1

            else:

                score += 0

        return score