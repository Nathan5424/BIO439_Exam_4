def read_sequence_from_file(filename):
    """
    Reads a DNA sequence from a file, assuming the file contains only raw sequence data (no headers).

    Args:
    - filename (str): The name of the file containing the sequence data.

    Returns:
    - str: The DNA sequence as a single long string.
    """
    with open(filename, 'r') as file:
        sequence = file.read().replace('\n', '')
    return sequence


def count_kmers(sequence, k):
    """
    Counts k-mers in the sequence and tracks the character that comes after each k-mer.

    Args:
    - sequence (str): The DNA sequence.
    - k (int): The length of the k-mer.

    Returns:
    - dict: A dictionary with k-mers as keys. Each value is another dict with total count and counts of following characters.
    """
    kmer_counts = {}

    for i in range(len(sequence) - k):
        kmer = sequence[i:i + k]
        next_char = sequence[i + k]

        if kmer not in kmer_counts:
            kmer_counts[kmer] = {'count': 0, 'next': {}}

        kmer_counts[kmer]['count'] += 1
        if next_char not in kmer_counts[kmer]['next']:
            kmer_counts[kmer]['next'][next_char] = 0
        kmer_counts[kmer]['next'][next_char] += 1

    return kmer_counts


def write_kmer_stats_to_file(kmer_data, output_filename):
    """
    Writes k-mer statistics to a file.

    Args:
    - kmer_data (dict): Dictionary with k-mer counts and next-character frequencies.
    - output_filename (str): Name of the file to write the results to.
    """
    with open(output_filename, 'w') as file:
        for kmer, data in kmer_data.items():
            next_counts = ', '.join([f"{char}: {count}" for char, count in data['next'].items()])
            line = f"{kmer} -> Count: {data['count']} | {next_counts}\n"
            file.write(line)


if __name__ == "__main__":
    # Adjust this as needed (e.g., add argparse later)
    sequence = read_sequence_from_file("reads.fa")
    k = 3  # Change this value to try different k-mer lengths
    kmer_stats = count_kmers(sequence, k)

    write_kmer_stats_to_file(kmer_stats, "kmer_output.txt")
    print("Done! Output written to kmer_output.txt")

