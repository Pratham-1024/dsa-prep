# Day 7 of 90: Revision (re-solve from scratch, no hints)
# Problems: #15 3Sum | #347 Top K Frequent Elements
# Status: Solved ✓ / revisit


from typing import List


# ---------------------------------------------------------------
# Problem: 3Sum
# LeetCode: #15
# Difficulty: Medium
# Topic: Array / Two Pointers
# Pattern: Sort + Two Pointers, skip duplicates
# Time: O(n²) | Space: O(1)  # ignoring sort/output
# ---------------------------------------------------------------
class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:                      # sorted: no triplet can sum to 0
                break
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:   # bounds check FIRST
                        l += 1

        return res

# Key insight: Sort so duplicates are adjacent and two pointers work.
# Fix one element, then two-pointer the rest for the negated sum.
# Skip duplicates at BOTH levels (outer i, inner l after a hit).
# Always put the `l < r` guard before indexing in the dedupe loop.
# Early break when a > 0 since the array is sorted.


# ---------------------------------------------------------------
# Problem: Top K Frequent Elements
# LeetCode: #347
# Difficulty: Medium
# Topic: HashMap / Bucket Sort
# Pattern: HashMap + Bucket Sort
# Time: O(n) | Space: O(n)
# ---------------------------------------------------------------
class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]   # index = frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Key insight: Frequency is bounded by n, so use it as an array index.
# Bucket i holds all numbers appearing exactly i times; scan buckets
# from high to low until k elements are collected. No comparison sort
# needed, so O(n) beats the O(n log n) sort approach.



# 📅 Week 1 Self-Review (Days 1-7)

# Covered: Arrays, HashMap/HashSet, Two Pointers, Sliding Window, Prefix Sum
# Problems: 15 new + 5 re-solved | Hardest: Minimum Window Substring

# Strengths:
# - Pattern recognition: sliding window and hashmap come fast
# - Clean code, good variable naming
# - Knowing the optimization exists (maxf, bucket sort, O(1) space prefix)

# Weaknesses:
# - Boundary conditions (3Sum dedupe loop, l < r guard)
# - Defaulting to sort/brute force before the optimal approach (Top K)
# - Forgetting imports and header complexity (Group Anagrams, Top K)
# - Complexity analysis written blank or incorrect in headers

# Revision list for Week 2:
# - #76 Minimum Window Substring
# - #424 Longest Repeating Character Replacement
# - #238 Product Except Self (O(1) space version)

# Week 2 goals:
# - Write time/space complexity in the header BEFORE submitting
# - Try the optimal approach first, brute force only as fallback
# - Dry-run on edge cases (empty input, single element, duplicates)