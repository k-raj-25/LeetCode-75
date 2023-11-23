class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)

        len1 = len(word1)
        len2 = len(word2)
        flag = False
        if len2 > len1:
            word1, word2 = word2, word1
            len2 = len1
            flag = True

        output = ""
        for i, ele in enumerate(word1):
            if flag == False:
                output += ele
                if len2 > i:
                    output += word2[i]
            else:
                if len2 > i:
                    output += word2[i]
                output += ele
        
        return output
    
def main():
    obj = Solution()
    print(obj.mergeAlternately("kaal", "nono"))

main()