class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        res = []

        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] += 1

        sorted_list = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        
        for x in sorted_list:
            if k == 0:
                return res
            res.append(x[0])
            k -= 1
        
        return res
