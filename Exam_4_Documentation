# Exam 4 Documentation

## 1. Data Structures Used to Store k-mers and Their Context

The main data structure used in this script is a **nested dictionary**. Each k-mer is stored as a key in a dictionary, and its value is another dictionary that holds:
- The total count of that k-mer (`"count"`)
- A dictionary (`"next"`) of characters that follow that k-mer, along with how many times each one occurs

Example:
```python
{
  "GAA": {
    "count": 246780,
    "next": {"A": 61498, "G": 62000, "T": 61656, "C": 61626}
  },
  ...
}
```

This structure allows fast lookups, avoids duplicate entries, and makes it easy to keep track of both overall and contextual frequencies for each k-mer.

## 2. Handling Edge Cases (e.g., First and Last k-mer in a Sequence)

- **First k-mer**: Treated normally; the loop begins at the first character of the sequence.
- **Last k-mer**: The loop stops at `len(sequence) - k`, so the final k-mer is only included if it has a character after it. This prevents out-of-range errors and ensures all k-mers included have full context.
- Edge k-mers are handled safely and consistently by constraining the loop to valid index ranges.

## 3. Avoiding Overcounting or Missing Context

- The script counts **each k-mer once per valid position** in the sequence.
- It updates counts using `dict.get()` to safely initialize or increment values without duplication.
- The loop moves one character at a time to generate overlapping k-mers, ensuring complete coverage.
- Next characters are only counted if they exist — preventing false context at the end of the sequence.
- These measures ensure counts are accurate and no context is missed or overstated.

