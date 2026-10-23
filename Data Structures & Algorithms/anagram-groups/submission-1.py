class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute-force: 
        result = []
        anagrams = {}

        for s in strs:
            new_s = sorted(s) # sorted() can work with tuple, list, and string 
            new_s = "".join(new_s)
            if new_s not in anagrams:
                anagrams[new_s] = []
                anagrams[new_s].append(s)
                continue

            anagrams[new_s].append(s)

        for key in anagrams:
            result.append(anagrams[key])

        return result
