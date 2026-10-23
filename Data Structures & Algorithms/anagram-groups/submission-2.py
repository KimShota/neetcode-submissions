class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []

        for s in strs:
            check = [0] * 26 

            for c in s:
                index = ord(c) - ord('a')
                check[index] += 1 
            
            check = tuple(check)
            
            if check not in anagrams:
                anagrams[check] = []

            anagrams[check].append(s)

        for key in anagrams:
            result.append(anagrams[key])

        return result