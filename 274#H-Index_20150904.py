#274 H-Index
# original approach: linear time
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        if l == 0:
            return 0
        if l == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        citations.sort()
        h = min(citations[0], l)
        for i in range(l - 1):
            fore_h = min(citations[i], l-i)
            next_h = min(citations[i+1], l-(i+1))
            if next_h >= fore_h:
                h = next_h
            else:
                break
        return h

# a much cleverer approach if sort reversely (however 5-8 times slower):
class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        i = 0
        while i < len(citations) and citations[i] >= i+1:
            print(citations[i],"->",i+1)
            i += 1
        return i

# sorted in ascending order also simple:
class Solution(object):
    def hIndex(self, citations):
        N = len(citations)
        if N == 0 or sum(citations) == 0:
            return 0
        citations.sort()
        i = 0
        while N - i > citations[i]:
            i += 1
        return N - i

# binary search approach: O(log n) time
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) / 2
            if N - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return N - left
    

if __name__ == '__main__':
    c = [0,1,0]
    test = Solution()
    h = test.hIndex(c)
    print(h)
            
