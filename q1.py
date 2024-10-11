from motif_utils import *
import sys
import os

def parse_input_file(file_path):
    try:
        # Reading the input file
        with open(file_path, 'r') as file:
            file_data = file.readlines()
            
            # Extracting motif length, number of motifs and DNA sequences
            motif_length, num_motifs = file_data.pop(0).split()
            dna = [line.strip() for line in file_data]
            return int(motif_length), int(num_motifs), dna
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading or parsing file {file_path}: {e}")
        sys.exit(1)

# Motifs <- Motifs(Profile, Dna)
def make_motifs_from_profile(dna, profile, k):
    motifs = []
    
    # For each DNA sequence, find the most
    for sequence in dna:
        motifs.append(find_most_probable_kmer(sequence, profile, k))
    return motifs

# Motifs <- RandomizedMotifSearch(Dna, k, t) 
def randomized_motif_search(dna, motif_length, num_motifs):
    # Randomly select k-mers Motifs = {Motif1, …, Motift} in each string from Dna
    motifs = choose_random_motifs(dna, motif_length, num_motifs)
    
    # BestMotifs <- Motifs
    best_motifs = motifs
    best_score = score_the_motifs(best_motifs)

    # While Forever
    while True:
        # Profile <- Profile(Motifs)
        profile = create_profile(motifs)
        
        # Motifs <- Motifs(Profile, Dna)
        motifs = make_motifs_from_profile(dna, profile, motif_length)
        score = score_the_motifs(motifs)

        # If Score(Motifs) < Score(BestMotifs)
        if score < best_score:
            # BestMotifs <- Motifs
            best_motifs = motifs
            best_score = score
        
        # return BestMotifs
        else:
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
        output_file = f"sol_q1_t{test_num}.txt"
        output_path = os.path.join(output_directory, output_file)

        motif_length, num_motifs, dna = parse_input_file(input_file)
        best_score_overall = float('inf')
        best_motifs_overall = []

        # Run the randomized motif search algorithm 1500 times
        iterations = 1500
        for _ in range(iterations):
            best_motifs, best_score = randomized_motif_search(dna, motif_length, num_motifs)
            if best_score < best_score_overall:
                best_score_overall = best_score
                best_motifs_overall = best_motifs
            
        print(f"Best score: {output_file}, {best_score_overall}")

        # Write the best motifs to the output file
        with open(output_path, 'w') as output:
            for motif in best_motifs_overall:
                output.write(f"{motif}\n")

if __name__ == "__main__":
    main()
