class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs, curset = [], [] 
        self.helper(1, combs, curset, n, k)
        return combs 

    def helper(self, i, combs, curset, n, k):
        if len(curset) == k:
            combs.append(curset.copy())
            return 
        if i > n:
            return 

        for j in range(i, n + 1):
            curset.append(j)
            self.helper(j + 1, combs, curset, n, k)
            curset.pop()
