class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.heapSort()
        

    def findMedian(self) -> float:
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return sum([self.data[mid-1], self.data[mid]]) / 2
        return self.data[mid]

    def heapSort(self) -> None:
        n = len(self.data)
        for i in range(n // 2, -1, -1):
            self.heapify(self.data, n, i)

        for i in range(n-1,0,-1):
            self.data[0],self.data[i] = self.data[i], self.data[0]
            self.heapify(self.data, i, 0)
            

    def heapify(self, data: List[int], n: int, i: int) -> None:
        largest = i
        left = i * 2 + 1 
        right = i * 2 + 2 
        if left < n and data[left] > data[largest]:
            largest = left
        if right < n and data[right] > data[largest]:
            largest = right
        if largest != i:
            data[largest], data[i] = data[i], data[largest]
            self.heapify(data, n, largest)
        
        