from time import time
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
        return result

if __name__ == '__main__':
    test = Solution()
    t1 = time()
    res = test.threeSumClosest([87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,
                                10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,
                                -53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,
                                30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,
                                100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,
                                61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,
                                91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,
                                -61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,
                                57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,
                                17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4],
                               -275)
    t2 = time()
    print(res)
    print(t2 - t1)
