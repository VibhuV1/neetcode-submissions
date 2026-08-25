class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for x in nums:
            if x in counter:
                counter[x] += 1
                return True
            else:
                counter[x] = 1
        return False