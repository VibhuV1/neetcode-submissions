class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res_hash_map = defaultdict(list)
        for string in strs:
            count_arr = [0] * 26
            for chars in string:
                count_arr[ord(chars) - ord("a")] += 1 
            res_hash_map[tuple(count_arr)].append(string)
        # print(res_hash_map.values())
        return list(res_hash_map.values())

        # first solve:
        # commenting because of TLE
        # from collections import Counter
        # ans = [] # [["1st-ana-map"], ["2nd-ana-map"]]
        # parent_hash_map = {} # {0: 1st-ana-map, 1: 2nd-ana-map}
        # for i, str_1 in enumerate(strs):
        #     str_hash_map = Counter(str_1)
            # if str_hash_map in parent_hash_map.values():
            #     for k, v in parent_hash_map.items():
            #         if str_hash_map == v:
            #             ans[k].append(str_1)
            #             break
            # else:
            #     new_parent_key = len(parent_hash_map.keys()) or 0
            #     parent_hash_map[new_parent_key] = str_hash_map
            #     ans.append([str_1])
        # return ans