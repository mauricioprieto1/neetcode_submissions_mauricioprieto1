class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq map num : freq
        # push tuple(freq, num) into heap (pop if len > k)
        # iterate k times to pop tuple and append num to result
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n,0)
        
        heap = []
        for n, f in freq.items():
            heapq.heappush(heap, (f,n))
            if len(heap) > k:
                heapq.heappop(heap) # remove the smallest freq value
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # pop from heap, append number from tuple
        return res 

        