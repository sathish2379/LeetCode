'''
295. Find Median from Data Stream**
Hard

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
'''
import heapq
class MedianFinder:

    def __init__(self):
        self.low = [] #max heap, storing negated values as python heapq is min-heap by deafult. Stores the first half of elements.
        self.high = [] #min-heap, stores the second half of the elements.
        #self.elements = []
        

    def addNum(self, num: int) -> None:
        #self.elements.append(num) //Basic algorithm using merge sort to solve O(nlogn) but time limit exceeded so let's try by using two heaps
        #self.elements.sort()
        heapq.heappush(self.low, -num)
        if self.low and self.high and -self.low[0] > self.high[0]:
            heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        # if len(self.elements) % 2 == 0:
        #     mid = len(self.elements)//2
        #     return (self.elements[mid] + self.elements[mid-1])/2.0
        # else:
        #     return self.elements[len(self.elements)//2]
        if len(self.low) > len(self.high):
             return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()