"""
Question 1: Implement Z-algorithm for Exact Pattern Matching problem discussed in class for two input DNA
strings p and t where Σ = {A, C, G, T } and p, t ∈ Σ+. You may assume |p| ≤ |t|.
"""

import os
import sys

class ZAlgorithm:
    def __init__(self):
        # Initialize the counters for comparisons, matches, and mismatches
        self.no_of_comparisons = 0
        self.no_of_mismatches = 0
        self.no_of_matches = 0
        
    def calculate_z_array(self, input_string):
        # Initialize the Z array with zeros
        Z = [0] * len(input_string)
        left, right = 0, 0

        # Calculate the Z array values
        for k in range(1, len(input_string)):
            if k > right:
                # If k is outside the current Z-box, we do naive comparison
                left = right = k
                while right < len(input_string) and input_string[right] == input_string[right - left]:
                    self.no_of_comparisons += 1
                    right += 1
                    self.no_of_matches += 1 # When character matched
                if right < len(input_string) and input_string[right] != input_string[right - left]:
                    self.no_of_comparisons += 1 
                    self.no_of_mismatches += 1  # When character mismatched
                # Update the Z value for k
                Z[k] = right - left
                right -= 1
            else:
                # If k is inside the current Z-box, we use the values computed before
                k1 = k - left
                if Z[k1] < right - k + 1:
                    # If Z[k1] is less than the remaining length, we copy the value
                    Z[k] = Z[k1]
                else:
                    # Otherwise, reset the Z-box and do naive comparison
                    left = k
                    while right < len(input_string) and input_string[right] == input_string[right - left]:
                        self.no_of_comparisons += 1
                        right += 1                       
                        self.no_of_matches += 1 # When character matched               
                    if right < len(input_string) and input_string[right] != input_string[right - left]:
                        self.no_of_comparisons += 1  
                        self.no_of_mismatches += 1  # When Character mismatched
                    Z[k] = right - left
                    right -= 1
        # Return the Z array
        return Z

    def match_pattern(self, text, pattern):
        # Concatenate the pattern and text with a $ separator
        new_string = pattern + '$' + text         
        Z = self.calculate_z_array(new_string)

        # Find the indices where the pattern matches the text
        result = []
        for i in range(len(Z)):
            if Z[i] == len(pattern):
                result.append(i - len(pattern) - 1)

        return result
    
    def print_results(self):
        # Print the number of comparisons, matches, and mismatches
        print("Number of comparisons: ", self.no_of_comparisons)
        print("Number of matches: ", self.no_of_matches)
        print("Number of mismatches: ", self.no_of_mismatches)

def read_from_files(input_file, output_file):    
    # Check if the input file exists
    with open(input_file, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:
            text = lines[0].strip()  
            pattern = lines[1].strip()

            # Run the Z-algorithm on the text and pattern
            z_algorithm = ZAlgorithm()
            result = z_algorithm.match_pattern(text, pattern)

            # Output results to new file in the given output directory
            with open(output_file, 'w') as output:
                for index in result:
                    output.write(f"{index + 1}\n")  #As we have 1-based index
            print(f"Results written to {output_file}")
            z_algorithm.print_results()


def main():
    # Check if the input directory is provided    
    input_directory = sys.argv[1]  # Command line argument
    output_directory = input_directory + "/solutions"  # Output directory
    
    # Create the output directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each file in the input directory
    for input_file in os.listdir(input_directory):
        if input_file.startswith("sample_"):
            input_path = os.path.join(input_directory, input_file)
            output_file = f"sol_{input_file.split('_')[1]}"
            output_path = os.path.join(output_directory, output_file)

            # Process each file
            read_from_files(input_path, output_path)


# Run the main function
if __name__ == "__main__":
    main()
