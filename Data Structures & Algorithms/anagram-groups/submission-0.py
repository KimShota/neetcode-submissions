class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        counts = [0] * 26
        
        for word in strs:
            for c in word:
                idx = ord(c) - ord('a')
                counts[idx] += 1
            tup = tuple(counts)
            if tup not in hashMap:
                hashMap[tup] = []
            hashMap[tup].append(word)
            counts = [0] * 26

        return list(hashMap.values())

            
                
        
        