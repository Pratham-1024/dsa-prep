# 📅 Week 1: Arrays, Strings & Hashing

**Topics:** Two Pointers · Sliding Window · Prefix Sums · HashMap / HashSet

**Series:** *Patterns Over Problems* · DSA Sunday #1

> Patterns are not memorised, they are mastered. A problem only counts as **solved** when you can solve it from scratch, with no hints, and explain why the pattern works.

---

## 🧩 Problems (Days 1–5)

| Number | Problem | LeetCode | Level | Pattern | Hint | Solution |
|-----|---------|----------|-------|---------|------|----------|
| 1 | Two Sum | [#1](https://leetcode.com/problems/two-sum/) | Easy | HashMap / Frequency Count | Store the complement in a map | [day1](day1/two_sum.py) |
| 2 | Best Time to Buy and Sell Stock | [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Greedy / Track Running Min | Track the running minimum price | [day1](day1/best_time_stocks.py) |
| 3 | Contains Duplicate | [#217](https://leetcode.com/problems/contains-duplicate/) | Easy | HashSet Membership Check | Set size ≠ array size means a duplicate | [day2](day2/contains_duplicate.py) |
| 4 | Valid Anagram | [#242](https://leetcode.com/problems/valid-anagram/) | Easy | HashMap / Frequency Count | Compare character frequency counts | [day2](day2/valid_anagram.py) |
| 5 | 3Sum | [#15](https://leetcode.com/problems/3sum/) | Medium | Sort + Two Pointers | Sort, fix one element, two pointers on the rest | [day2](day2/three_sum.py) |
| 6 | Container With Most Water | [#11](https://leetcode.com/problems/container-with-most-water/) | Medium | Two Pointers (Opposite Ends) | Move the shorter pointer inward | [day2](day2/container_water.py) |
| 7 | Longest Substring Without Repeating Characters | [#3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Variable Size Sliding Window | Expand right, shrink left on a duplicate | [day3](day3/longest_substring.py) |
| 8 | Maximum Average Subarray I | [#643](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | Fixed Size Sliding Window | Drop the leftmost, add the rightmost | [day3](day3/max_avg_subarray.py) |
| 9 | Longest Repeating Character Replacement | [#424](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Variable Size Sliding Window | Window is valid if size − maxFreq ≤ k | [day3](day3/longest_repeating.py) |
| 10 | Product of Array Except Self | [#238](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix Product / Prefix Sum | Prefix × suffix at each index, no division | [day4](day4/product_except_self.py) |
| 11 | Subarray Sum Equals K | [#560](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Prefix Sum + HashMap | If curSum − k is in the map, count it (start with `{0: 1}`) | [day4](day4/subarraySum_Equals_k.py) |
| 12 | Group Anagrams | [#49](https://leetcode.com/problems/group-anagrams/) | Medium | HashMap / Frequency Count | Use the sorted string as the map key | [day4](day4/group_anagrams.py) |
| 13 | Top K Frequent Elements | [#347](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Bucket Sort | Count frequencies, then bucket by frequency | [day5](day5/topK_frequentElement.py) |
| 14 | Longest Consecutive Sequence | [#128](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | HashSet + Sequence Start Detection | Only start counting when num − 1 is not in the set | [day5](day5/longest_consecutive_sequence.py) |
| 15 | Minimum Window Substring | [#76](https://leetcode.com/problems/minimum-window-substring/) | Hard | Variable Size Sliding Window | Two counters (have / need) track window validity | [day5](day5/minimum_window_substring.py) |

**Totals:** 15 problems · 5 Easy · 9 Medium · 1 Hard · 10 patterns

---

## ⏱️ Day 6: Timed Practice

Pick any **3 problems from Days 1–5 that you found hardest** and solve them in a single **90-minute** session.

- No notes, no hints
- Treat it like an interview: talk through your approach as you go
- Choose your own problems, the ones that hurt are the right ones

## 🔁 Day 7: Review & Consolidate

- **Re-solve the 2 problems you struggled with most** this week, from scratch, with no hints
- Write your own cheat sheet: every pattern with a 2-line explanation and an example problem
- Count what you solved and which patterns you can now explain from memory

---

## 🧠 Patterns

| Pattern | Use when | Problems |
|---------|----------|----------|
| HashMap / Frequency Count | You need O(1) lookup, counting frequency, or finding complements | Two Sum #1, Valid Anagram #242, Subarray Sum Equals K #560, Group Anagrams #49, Minimum Window Substring #76 |
| Greedy / Track Running Min | A locally optimal choice leads to the global optimum, no need to look back | Best Time to Buy and Sell Stock #121 |
| Sort + Two Pointers | Finding pairs/triplets with a target sum: sort first, then use two pointers from both ends | 3Sum #15 |
| Two Pointers (Opposite Ends) | Shrinking the search space from both ends, classic for container/pair problems | Container With Most Water #11 |
| HashSet Membership Check | You only need to know if duplicates exist, not their count | Contains Duplicate #217 |
| Variable Size Sliding Window | The window grows/shrinks based on a condition; track the max valid window | Longest Substring Without Repeating Characters #3, Longest Repeating Character Replacement #424, Minimum Window Substring #76 |
| Fixed Size Sliding Window | Window size k is given and you need max/min/avg over subarrays | Maximum Average Subarray I #643 |
| Prefix Product / Prefix Sum | The answer at index i depends on all elements before and after it. Build a prefix array left→right, a suffix array right→left, then combine | Product of Array Except Self #238, Subarray Sum Equals K #560 |
| Bucket Sort | Values are bounded (e.g. frequency ≤ n). Use the value as an index into a buckets array and scan high to low. Avoids comparison sort → O(n) | Top K Frequent Elements #347 |
| HashSet + Sequence Start Detection | Finding consecutive sequences. Convert to a set for O(1) lookup and only begin counting from a sequence start (num − 1 not in the set). Each element is visited at most twice → O(n) | Longest Consecutive Sequence #128 |

---

## 🛠️ How I Practice

1. **Attempt for 20 minutes before looking at any hint**
2. **Write the pattern in your own words** after every problem
3. **Re-solve from memory** a day or two later
4. **Explain the solution out loud** as if in an interview
5. **Push the solution** with a header comment (problem, LeetCode number, difficulty, pattern, complexity)

---

⭐ Part of my [dsa-prep](../README.md) repository.