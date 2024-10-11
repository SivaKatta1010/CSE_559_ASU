from motif_utils import *
import sys
import os
import random

def parse_input_file(file_path):
    try:
        # Reading the input file
        with open(file_path, 'r') as file:
            file_data = file.readlines()
            
            # Extracting motif length, number of motifs, number of iterations and DNA sequences
            motif_length, num_motifs, num_iters = file_data.pop(0).split()
            dna = [line.strip() for line in file_data]
            return int(motif_length), int(num_motifs), int(num_iters), dna
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading or parsing file {file_path}: {e}")
        sys.exit(1)
        
# Pick a random number i by RANDOM(p_1,p_2,...,p_n) and pick i-th k- mer (profile-randomly generated k-mer)
def weighted_random_choice_kmer(probabilities):
    # Calculate the total sum of all probabilities
    total = 0
    for p in probabilities:
        total += p
    
    rand_num = random.random() * total
    
    cumulative_sum = 0
    for index, probability in enumerate(probabilities):
        cumulative_sum += probability
        if rand_num < cumulative_sum:
            return index
    return len(probabilities) - 1

# For each k-mer in Dna, compute probability based on input profile —> (p_1,p_2,...,p_n)
import random

def compute_kmer_probabilities(gene, k, profile):
    # Calculating probabilities of all the possible k-mers
    probability_list = []
    sequence_length = len(gene)
    
    # Iterate over all possible k-mers in the DNA sequence
    for j in range(sequence_length - k + 1):
        kmer = gene[j:j + k]
        probability = 1.0
        
        for idx, nucleotide in enumerate(kmer):
            probability *= profile[idx][nucleotide]
        
        probability_list.append(probability)
    
    # Calculate the total probability to normalize the list
    total = sum(probability_list)
    probability_list = [p / total for p in probability_list]
    
    return probability_list


# Motifs <- GibbsSampler(Dna, k, t, N)
def gibbs_sampling_motif_search(dna, motif_length, num_motifs, num_iters):
    # Randomly select k-mers Motifs = {Motif1, …, Motift} in each string from Dna
    motifs = choose_random_motifs(dna, motif_length, num_motifs)
    
    # BestMotifs <- Motifs
    best_motifs = motifs
    best_score = score_the_motifs(best_motifs)

    # for j from 1 to N
    for _ in range(num_iters):
        # i <- Random(t)
        i = random.randint(0, num_motifs - 1)
        updated_motifs = motifs[:i] + motifs[i+1:]
        
        # Profile <- Profile(Motifs except Motif i)
        profile = create_profile(updated_motifs)
        
        # Motif i <- Profile-randomly generated k-mer in the i-th sequence
        probability_list = compute_kmer_probabilities(dna[i],motif_length, profile)
        new_motif_index = weighted_random_choice_kmer(probability_list)
        new_motif = dna[i][new_motif_index:new_motif_index + motif_length]
        motifs = updated_motifs[:i] + [new_motif] + updated_motifs[i:]
        
        # Score <- Score(Motifs)
        score = score_the_motifs(motifs)

        # If Score < Score(BestMotifs)
        if score < best_score:
            # BestMotifs <- Motifs
            best_motifs = motifs
            best_score = score
        else:
            continue
    
    # return BestMotifs
    return best_motifs, best_score

def main():
    input_files_list = sys.argv[1:]
    output_directory = "solutions"
    
    # Creating a directory to store the output files
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # For each input file in the input directory
    for input_file in input_files_list:
        print(f"Processing {input_file}")
        basename = os.path.basename(input_file)
        test_num = basename.split('_')[1].split('.')[0]
        output_file = f"sol_q2_t{test_num}.txt"
        output_path = os.path.join(output_directory, output_file)
        motif_length, num_motifs, num_iters, dna = parse_input_file(input_file)
        best_score_overall = float('inf')
        best_motifs_overall = []

        # Run the gibbs sampling motif search algorithm 30 times
        for _ in range(30):
            best_motifs, best_score = gibbs_sampling_motif_search(dna, motif_length, num_motifs, num_iters)
            if best_score < best_score_overall:
                best_score_overall = best_score
                best_motifs_overall = best_motifs
                    
        print(f"Best score: {output_file}, {best_score_overall}")

        # Write the best motifs to the output file
        with open(output_path, 'w') as output:
            for motif in best_motifs_overall:
                output.write(f"{motif}\n")
            #output.write(f"Score: {best_score_overall}\n")

if __name__ == "__main__":
    main()
