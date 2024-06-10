from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # gain contains net gain between points i and i+1
        # altitudes array starts with 0

        #  method 1
        # altitudes = [0]
        # for i in range(len(gain)):
        #     altitudes.append(gain[i]+ altitudes[i])
        # return max(altitudes)

        # method 2

        return max(accumulate(gain, initial = 0))
        




        
