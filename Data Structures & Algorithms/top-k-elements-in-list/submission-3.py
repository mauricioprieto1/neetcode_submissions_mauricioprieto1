class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} # number : frequency 

        for num in nums:
            # add one to the freq of the number, use the get(num, 0) to make sure if the number doesnt have a record, we create one with 0 as the initial number
            count[num] = 1 + count.get(num, 0)

        heap = [] # min heap, the smallest number is kept at the top, the biggest at the bottom

        # iterate over the numbers
        for num in count.keys():
            # tuple(freq, num)
            heapq.heappush(heap, (count[num], num))

            # remove the smallest freq numbers
            if len(heap) > k:
                heapq.heappop(heap)

        
        res = []

        for i in range(k):
            # res.append(heapq.heappop(heap)[1]) # pop and access element at index 1
            freqTuple = heapq.heappop(heap)
            frequency = freqTuple[1]
            res.append(frequency)
        return res