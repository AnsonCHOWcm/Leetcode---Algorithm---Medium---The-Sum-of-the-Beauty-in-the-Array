class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:

        asc_score = []
        dsc_score = []
        asc_max = 0
        dsc_min = 100000
        ans_sum = 0

        for index in range(1, len(nums) - 1):

            if index == 1:

                if (nums[index] > nums[index - 1]):

                    asc_score.append(2)

                else:

                    asc_max = nums[index - 1]

                    asc_score.append(0)

                if (nums[len(nums) - 1 - index] < nums[len(nums) - 1 - index + 1]):

                    dsc_score.append(2)

                else:

                    dsc_min = nums[len(nums) - 1 - index + 1]

                    dsc_score.append(0)

            else:

                if (nums[index] > nums[index - 1]):

                    if asc_score[-1] == 2 or nums[index] > asc_max:

                        asc_score.append(2)

                    else:

                        asc_score.append(1)

                else:

                    if (nums[index - 1] > asc_max):
                        asc_max = nums[index - 1]

                    asc_score.append(0)

                if (nums[len(nums) - 1 - index] < nums[len(nums) - 1 - index + 1]):

                    if dsc_score[-1] == 2 or nums[len(nums) - 1 - index] < dsc_min:

                        dsc_score.append(2)

                    else:

                        dsc_score.append(1)

                else:

                    if (nums[len(nums) - 1 - index + 1] < dsc_min):
                        dsc_min = nums[len(nums) - 1 - index + 1]

                    dsc_score.append(0)

        for i in range(len(dsc_score)):

            if asc_score[i] == 0 or dsc_score[len(dsc_score) - 1 - i] == 0:

                ans_sum += 0

            else:

                ans_sum += (asc_score[i] + dsc_score[len(dsc_score) - 1 - i]) // 2

        return ans_sum