class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        temp = [value, timestamp]
        
        self.store[key].append(temp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        curMax = 0

        for item in self.store[key]:
            if timestamp == item[1]:
                return item[0]

        left = 0
        right = len(self.store[key]) - 1
        answer = -1 

        while left <= right:
            mid = (left + right) // 2

            if self.store[key][mid][1] <= timestamp:
                answer = mid 
                left = mid + 1
            else:
                right = mid - 1 

        if answer == -1:
            return ""
        else:
            return self.store[key][answer][0]
        
        return ""
        
