Question:
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]  
  
  
  
Solution:

class Solution(object):
def wordBreak(self, s, wordDict):
    return self.helper(s, wordDict, {})
    
def helper(self, s, wordDict, memo):
    if s in memo: return memo[s]
    if not s: return []
    
    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res  
