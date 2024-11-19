class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_1 = {} # hashmap for first string 
        hm_2 = {} # hashmap for second string
        hm_1 = self.create_dict(s, hm_1) 
        hm_2 = self.create_dict(t, hm_2)
        if hm_1 == hm_2:
            return True 
        return False 

    def create_dict(self, string, hm): 
        
        for n in string: 
            if n in hm:
                hm[n] = hm[n] + 1 
            else: 
                hm[n] = 1
        return hm 
    
test = Solution()
print(test.isAnagram("racecar", "carrace"))
print(test.isAnagram("jar", "jam")) 