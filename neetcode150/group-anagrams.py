from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = sorted(strs, key=len)
        strs = self.split_list(strs)  # Returns list of lists (sorted by length)
        result = []

        for s in strs:
            temp = {}  # Store hash_val : list of string elements
            for count, val in enumerate(s):
                hm = self.create_hashtable(''.join(sorted(val)))
                hm_tuple = tuple(sorted(hm.items()))  # Convert dict to hashable tuple
                if hm_tuple in temp:
                    temp[hm_tuple].append(val)
                else:
                    temp[hm_tuple] = [val]
            for key in temp:
                values = temp[key]
                result.append(values)
            print(temp)
        return result

    # Used to create a frequency table for comparison
    def create_hashtable(self, strs):
        hm = {}
        for s in strs:
            if s in hm:
                hm[s] += 1
            else:
                hm[s] = 1
        return hm

    # Used to split list based on the length of each element into a list of lists
    def split_list(self, strs):
        result = []
        temp = []
        for i in range(len(strs)):
            temp.append(strs[i])
            if i < len(strs) - 1 and len(strs[i]) != len(strs[i + 1]):
                result.append(temp)
                temp = []
            if i == len(strs) - 1:
                result.append(temp)

        return result


class OptimisedSolution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())