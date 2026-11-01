# Day 6 of 90: Timed Mock Session (90 min, no notes)
# Problems: #76 Minimum Window Substring | #424 Longest Repeating Character Replacement | #560 Subarray Sum Equals K
# Status: Solved ✓ / revisit


from typing import List


# ---------------------------------------------------------------
# Problem: Minimum Window Substring
# LeetCode: #76
# Difficulty: Hard
# Topic: String / HashMap / Sliding Window
# Pattern: Variable Sliding Window + Dual HashMap
# Time: O(n + m) | Space: O(n + m)
# ---------------------------------------------------------------
class MinWindow:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""

# Key insight: Track "have" (chars meeting required count) vs "need"
# (unique chars required). Expand right; when have == need the window
# is valid, so record it and shrink from the left to minimise it.
# Only increment have when window[c] EXACTLY equals countT[c], and
# decrement it only when the count drops BELOW the requirement.


# ---------------------------------------------------------------
# Problem: Longest Repeating Character Replacement
# LeetCode: #424
# Difficulty: Medium
# Topic: String / Sliding Window
# Pattern: Variable Sliding Window + Frequency Map
# Time: O(n) | Space: O(1)  # max 26 keys
# ---------------------------------------------------------------
class CharReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = l = maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

# Key insight: A window is valid if (size - most frequent char) <= k,
# because only the non-dominant chars need replacing. maxf never needs
# to shrink: a stale, larger maxf can't produce a longer window than
# one already recorded in res.


# ---------------------------------------------------------------
# Problem: Subarray Sum Equals K
# LeetCode: #560
# Difficulty: Medium
# Topic: Array / Prefix Sum / HashMap
# Pattern: Prefix Sum + HashMap
# Time: O(n) | Space: O(n)
# ---------------------------------------------------------------
class SubarraySum:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            cur_sum += num
            res += prefix_sums.get(cur_sum - k, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

        return res

# Key insight: If cur_sum - k was seen as an earlier prefix sum, the
# elements between that point and here sum to k. Store prefix-sum
# FREQUENCIES (negatives/zeros make repeats possible), and seed {0: 1}
# so subarrays starting at index 0 are counted.
# Sliding window fails here because negatives break monotonicity.



# ⏱ Session: 90 min | Problems: #76, #424, #560

# Time split (adjust to yours):
# - Min Window Substring: ~40 min (hardest)
# - Longest Repeating Char Replacement: ~25 min
# - Subarray Sum Equals K: ~25 min

# What went well:
# - Recognized sliding window and prefix sum patterns quickly
# - Remembered the "have == need" exact-match condition
# - Used the maxf optimization without hints

# What went wrong:
# - Hesitated on when to decrement `have` in #76
# - Almost missed the {0:1} seed in #560
# - Spent time debugging instead of dry-running first

# Fix for next time:
# - Dry-run on a tiny input BEFORE coding
# - Write the invariant as a comment first (e.g. "window valid if size - maxf <= k")