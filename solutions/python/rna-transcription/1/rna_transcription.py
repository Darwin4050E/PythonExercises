"""Function to help determine the RNA complement of a given DNA sequence.
"""
def to_rna(dna_strand):
    """Transcribe from DNA to RNA sequence.
    
    :param dna_strand: str - DNA sequence.
    :return: str - RNA sequence.
    """
    conversions = {"G":"C", "C":"G", "T":"A", "A":"U"}
    return "".join([conversions[nucleotide] for nucleotide in dna_strand])
