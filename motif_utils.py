import random

# Choosing random motifs from the DNA sequences
def choose_random_motifs(dna, k, t):
    motifs = []
    for i in range(t):
        start = random.randint(0, len(dna[0]) - k)
        motifs.append(dna[i][start:start+k])
    return motifs

# Finding the consensus sequence from the motifs
def consensus_sequence(motifs):
    consensus = ''
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        consensus += max(set(column), key=column.count)
    return consensus

# Calculating the Hamming distance between two sequences
def hamming_distance(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

# Scoring the motifs based on the consensus sequence
def score_the_motifs(motifs):
    consensus = consensus_sequence(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(motif, consensus)
    return score

# Finding the most probable k-mer in a sequence based on the profile
def find_most_probable_kmer(sequence, profile, k):
    most_probable_kmer = ''
    best_probability = -1
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        probability = 1
        for j in range(len(kmer)):
            probability *= profile[j][kmer[j]]
        if probability > best_probability:
            best_probability = probability
            most_probable_kmer = kmer
        elif probability == best_probability:
            most_probable_kmer = random.choice([most_probable_kmer, kmer])
    return most_probable_kmer

# Creating a profile matrix from the motifs
def create_profile(motifs):
    profile = []
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        # Apply pseudocounts of 1 to avoid zero probabilities
        profile.append({base: (column.count(base) + 1) / (len(column) + 4) for base in 'ACGT'})
    return profile