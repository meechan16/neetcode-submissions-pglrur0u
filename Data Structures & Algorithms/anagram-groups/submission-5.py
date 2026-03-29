class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j) - ord('a')] +=1
            dicti[tuple(count)].append(i)
        return list(dicti.values())
