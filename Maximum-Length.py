"""

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

[ "cos", "meto", "log", "ia" ]

cosia
metoia -> s  maximum possible length
logia

len s = 6

"""


class Solution:
    def maxLength(self, arr: List[str]) -> int: