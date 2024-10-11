from q1 import randomized_motif_search
from q2 import gibbs_sampling_motif_search
from motif_utils import *
import sys

# Read the motif data
def read_motif_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Running Randomized Motif Search for a given number of iterations
def run_randomized_motif_search(dna, k, num_iterations):
    best_motifs, best_score = None, float('inf')
    #print("Number of DNAs: ", len(dna))
    for _ in range(num_iterations):
        motifs, score = randomized_motif_search(dna, k, len(dna))
        if score < best_score:
            best_motifs, best_score = motifs, score
    return best_motifs, best_score

# Running Gibbs Sampling for a given number of iterations
def run_gibbs_sampling(dna, k, num_iterations):
    best_motifs, best_score = None, float('inf')
    for _ in range(1):
        motifs, score = gibbs_sampling_motif_search(dna, k, len(dna), num_iterations)
        if score < best_score:
            best_score = score
            best_motifs = motifs
    return best_motifs, best_score


def main():
    input_file = sys.argv[1]

    # Read the motif data
    dna = read_motif_data(input_file)
    k = 15

    #Randomized Motif Search for different iterations
    print("Randomized Motif Search Results:")
    iterations_list = [1000, 10000, 100000]
    for num_iterations in iterations_list:
        best_motifs, best_score = run_randomized_motif_search(dna, k, num_iterations)
        consensus = consensus_sequence(best_motifs)
        print(f"Iterations: {num_iterations}")
        print(f"Consensus Sequence: {consensus}")
        print(f"Score: {best_score}\n")

    # Gibbs Sampling for different iterations
    print("Gibbs Sampling Results:")
    iterations_list = [1000, 2000, 10000]
    for num_iterations in iterations_list:
        best_motifs, best_score = run_gibbs_sampling(dna, k, num_iterations)
        consensus = consensus_sequence(best_motifs)
        print(f"Iterations: {num_iterations}")
        print(f"Consensus Sequence: {consensus}")
        print(f"Score: {best_score}\n")

if __name__ == "__main__":
    main()