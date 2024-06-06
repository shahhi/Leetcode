class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        i = 0
        # time complexity O(n), Where n and m are len of word1 and word2 respectively. And n<m
        while( i < len(word1) and i < len(word2)):
            merged_str += (word1[i])
            merged_str += (word2[i])
            i+=1
        if len(word1)< len(word2):
            merged_str += (word2[i:])
        else:
            merged_str += (word1[i:])
    
        return merged_str

        
