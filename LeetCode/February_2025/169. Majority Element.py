class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidat, count = None, 0
        for num in nums:
            if count == 0:
                candidat = num
            if num == candidat :
                count += 1
            else:
                count -= 1
        return candidat