# Day 4 Notes – Median of Two Sorted Arrays

### Concepts Used:
- Binary Search
- Partitioning arrays
- Edge handling with float('inf') and float('-inf')

### Key Observations:
- To find the median in `O(log(min(m,n)))`, we binary search on the smaller array.
- Partitions must ensure left half max <= right half min from both arrays.
- Even total elements: average of two middle values.
- Odd total elements: max of left partitions.

### Things I Learned:
- How binary search can be used for partitioning two arrays
- How to think in terms of virtual partitions instead of merging arrays
- How to handle edge cases with empty partitions

### Time Complexity:
- `O(log(min(m, n)))`
