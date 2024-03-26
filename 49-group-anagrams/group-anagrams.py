class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping char count to list of Anagrams

        for s in strs:    
            count = [0]*26 # a.....z
            for c in s:
                count[ ord(c) - ord("a")]+=1
        
        # convert list into tuple because in python lists can't be appended and tuples are immutable
            res[tuple(count)].append(s)  

        return res.values()