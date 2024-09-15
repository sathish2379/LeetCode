'''
274. H-Index
Medium

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) 
        count_arr = [0]*(n+1)

        # count_arr gives the count of number of citations
        # Ex: 4 citations - 4 papers, 3 citations - 2 times 
        for num in citations:
            if num >= n:
                count_arr[n] += 1
            else:
                count_arr[num] += 1

        # Now we need to find cumulative
        for i in range(n - 1, -1, -1):
            count_arr[i] += count_arr[i+1]

        #Finding max h-index
        # here index is number of citations 
        # the value is cumulative count of research papers that received those number of citations.
        for i in range(n, -1, -1):
            if count_arr[i] >= i:
                return i        