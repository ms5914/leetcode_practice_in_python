class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0 for _ in range(length)]
        
        for start, end, inc in updates:
            arr[start] = arr[start]+inc
            if end+1 < len(arr):
                arr[end+1] = arr[end+1]-inc
        
        prefix_sum = arr[0]
        for i in range(1, len(arr)):
            arr[i] = prefix_sum+arr[i]
            prefix_sum = arr[i]
        
        return arr
            
            
            
        