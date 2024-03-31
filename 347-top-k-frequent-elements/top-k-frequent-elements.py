class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap
        freq = [[] for i in range (len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n,c in count.items(): # key value pair
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1): #decrementing from right hand side
            for n in freq[i]:
                res.append(n)
                if len(res)== k:
                    return res    

