## Exam_4_Documentation

This short document explains how my script works, how I chose to store the k-mers and their context, how I handled edge cases, and how I made sure everything was counted correctly without duplication.

---

### 1. How I Stored the K-mers and Context

To keep track of each k-mer and the character that follows it, I used a **nested dictionary** in Python. The outer dictionary uses the k-mer string as the key. Each value is another dictionary with two parts:
- `"count"`: how many times that exact k-mer shows up in the input sequence
- `"next"`: a dictionary that stores how many times each base (A, T, G, or C) came directly after the k-mer in the original sequence

This structure makes it easy to look up a k-mer and see both how often it occurs and what tends to come next in the sequence.

#### Example:
```python
{
  "GAA": {
    "count": 246780,
    "next": {"A": 61498, "G": 62000, "T": 61656, "C": 61626}
  },
  ...
}
```

---

### 2. Handling Edge Cases

There were a few edge cases I needed to think about:
- **First k-mer in a sequence**: This is no different from any other k-mer, so I treated it the same. It's captured naturally as I loop through the sequence.
- **Last k-mer in a sequence**: The last k-mer might not have a character after it, especially if it's at the end of the file. In this case, I still count the k-mer itself, but I skip updating the `"next"` part since there's no next base to track.

Also, I made sure to **skip any lines in the file that start with “>”**, since these are FASTA headers, not sequence data.

---

### 3. Avoiding Overcounting or Missing Context

To avoid counting things more than once or skipping over valid k-mers:
- I read the full sequence into one long string (ignoring the header lines) so that k-mers could span multiple lines if needed.
- I looped through the sequence one base at a time using a `for` loop and a sliding window of length `k`. This means every overlapping k-mer is considered, as required.
- For each k-mer, I increment its count and also check if there’s a character right after it. If there is, I update the `"next"` dictionary with that base.

This made sure that I captured every valid k-mer and its context exactly once.


