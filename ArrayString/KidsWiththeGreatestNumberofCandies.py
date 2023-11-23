import copy

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        candies_tmp = copy.deepcopy(candies)
        candies_tmp.sort(reverse=True)
        highest = candies_tmp[0]
        output = []
        for i in candies:
            if i+extraCandies >= highest:
                output.append(True)
            else:
                output.append(False)
        
        return output

def main():
    obj = Solution()
    print(obj.kidsWithCandies([2,3,5,1,3], 3))

main()