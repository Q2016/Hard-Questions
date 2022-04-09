Question:
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]


Solution:
ntuition:
First you may have feeling of using sliding window.
Then this idea get stuck in the middle.

This problem will be a very typical sliding window,
if it asks the number of subarrays with at most K distinct elements.

Just need one more step to reach the folloing equation:
exactly(K) = atMost(K) - atMost(K-1)


Explanation
Write/copy a helper function of sliding window,
to get the number of subarrays with at most K distinct elements.
Done.

Complexity:
Time O(N) for two passes.
Space O(K) at most K elements in the counter

Of course, you can merge 2 for loops into one, if you like.

    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res
