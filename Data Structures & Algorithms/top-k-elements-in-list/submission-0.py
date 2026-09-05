class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freq = Counter(nums)
        heap_k = heapq.nlargest(k, freq.items(), key=lambda x: x[1])
        return [x for (x,y) in heap_k]