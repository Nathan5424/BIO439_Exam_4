import os
from kmer_script import read_sequence_from_file, count_kmers, write_kmer_stats_to_file

def test_read_sequence_from_file(tmp_path):
    # Create a temporary file with sample sequence
    test_file = tmp_path / "test_sequence.fa"
    test_file.write_text("ATGC\nGATTACA")

    result = read_sequence_from_file(str(test_file))
    assert result == "ATGCGATTACA"

def test_count_kmers_typical_case():
    sequence = "ATGCG"
    k = 2
    expected = {
        'AT': {'count': 1, 'next': {'G': 1}},
        'TG': {'count': 1, 'next': {'C': 1}},
        'GC': {'count': 1, 'next': {'G': 1}},
    }
    result = count_kmers(sequence, k)
    for kmer in expected:
        assert result[kmer]['count'] == expected[kmer]['count']
        assert result[kmer]['next'] == expected[kmer]['next']

def test_count_kmers_edge_case_short_sequence():
    sequence = "AT"
    k = 3
    result = count_kmers(sequence, k)
    assert result == {}  # k > len(sequence) so should be empty

def test_write_kmer_stats_to_file(tmp_path):
    # Prepare dummy k-mer data
    data = {
        'AA': {'count': 3, 'next': {'T': 2, 'G': 1}},
        'AT': {'count': 2, 'next': {'C': 2}},
    }
    output_file = tmp_path / "output.txt"
    write_kmer_stats_to_file(data, str(output_file))

    # Read and verify contents
    content = output_file.read_text()
    assert "AA -> Count: 3" in content
    assert "AT -> Count: 2" in content
    assert "T: 2" in content

