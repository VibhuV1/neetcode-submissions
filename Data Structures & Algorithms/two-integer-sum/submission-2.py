class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force:
        """
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """

        # hashmap:
        hash_map = {ele: index for index, ele in enumerate(nums)}
        for i in range(0, len(nums)):
            ele = target - nums[i]
            if hash_map.get(ele):
                if hash_map.get(ele) != i:
                    return [i,hash_map.get(ele)]