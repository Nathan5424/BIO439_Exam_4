# BIO439_Exam_4
Python Assignment
# K-mer Frequency Analysis Script

## Overview

This project analyzes a DNA sequence file by identifying all k-mers (substrings of length *k*) and recording:
- The total frequency of each k-mer
- The frequency of each character that appears immediately after that k-mer

This information is the basis for computational genome assembly techniques.

The project:
- Reads raw DNA sequence data from a `.fa` file
- Generates frequency tables of k-mers and their following characters
- Outputs this data to a file
- Includes fully-tested, well-documented Python code

## Files Included

- `kmer_script.py` – Main Python script for k-mer analysis
- `test_kmer_script.py` – Test suite using `pytest`
- `kmer_output.txt` – Output file with k-mer statistics
- `README.md` – Project overview and instructions
- `kmer_analysis_notes.md` – Documentation explaining data structures and edge case handling (see below)

## Usage

### Requirements
- Python 3.6+
- `pytest` (for running tests)

### Run the Script

To run the script from the command line:

```bash
python kmer_script.py reads.fa 3
