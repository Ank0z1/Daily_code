class Solution:
    def jump(self, nums: List[int]) -> int:
        fartest = 0
        cur_end = 0
        jumps = 0
        for i in range(len(nums) -1 ):
            fartest = max(fartest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = fartest
        return jumps
