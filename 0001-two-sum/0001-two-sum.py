class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i,n in enumerate(nums):
            diff = target-nums[i]
            if diff not in hashm:
                hashm[n]=i
            else: return [hashm[diff],i]
        