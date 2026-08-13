class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        answer = sorted(s1)

        for i in range(n):
            substring = s2[i:i+m]
            list1 = sorted(substring)
            if list1 == answer:
                return True 
        
        return False



