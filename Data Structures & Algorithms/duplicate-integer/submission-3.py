class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for x in nums:
            if x not in seen_set:
                seen_set.add(x)
            else:
                return True
        return False