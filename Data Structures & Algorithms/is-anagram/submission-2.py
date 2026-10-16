class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapX = {}
        hashMapY = {}

        for char in s:
            hashMapX[char] = 1 + hashMapX.get(char, 0)
        
        for char in t:
            hashMapY[char] = 1 + hashMapY.get(char, 0)

        if hashMapX == hashMapY:
            return True 
        else:
            return False