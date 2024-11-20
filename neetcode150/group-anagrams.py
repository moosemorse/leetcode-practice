class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    
        strs.sort()
        strs = self.split_list(strs) # Returns list of lists (sorted in length)
        result = []

        for s in strs: 
            temp = []
            for count, val in enumerate(s):
                temp.append(val) 
                if i < len(strs) - 1 and len(strs[i]) != len(strs[i+1]): 
                    result.append(temp)
                    temp = []
                if i == len(strs) - 1: 
                    result.append(temp)
    
    # Used to compare elements 
    def create_hashtable(self, strs):
        hm = {} 
        for s in strs: 
            if s in hm: 
                hm[s] += 1
            else: 
                hm[s] = 1
        return hm 

    # Used to split list based on length of each element
    def split_list(self, strs): 
        result = []
        temp = []
        for i in range(len(strs)): 
            temp.append(strs[i]) 
            if i < len(strs) - 1 and len(strs[i]) != len(strs[i+1]): 
                result.append(temp)
                temp = []
            if i == len(strs) - 1: 
                result.append(temp)

                    
        