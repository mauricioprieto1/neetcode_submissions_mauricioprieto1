class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build freq map from nums
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        # min heap for freq
        heap = []
        heapq.heapify(heap)
        for num, freq in freq.items():
            record = [freq,num]
            heapq.heappush(heap,record)
            # pop least frequent num
            if len(heap) > k:
                heapq.heappop(heap)
        # return the nums in heap
        res = []
        for i in range(k):
            record = heapq.heappop(heap)
            res.append(record[1])
        return res

        