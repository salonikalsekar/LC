class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            ans = True
        if len(ransomNote) == 0 and len(magazine) == 0:
            ans = True
        for i in set(ransomNote):
            if i in magazine:
                if ransomNote.count(i) <= magazine.count(i):
                    ans = True
                else:
                    ans = False
                    break;
            else:
                ans = False
                break;

        return ans
