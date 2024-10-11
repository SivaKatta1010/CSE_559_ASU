# Z-Algorithm Pattern Matching

## How to Run the Program

### Command-Line Usage:

To run the program, you need to provide the **input directory** as a command line qrgument. The output files will be automatically saved in a solutions folder within the same directory. 

### Syntax:
```bash
python Question1.py ./samples
```

- `./samples` is the directory containing input files, such as `sample_0`, `sample_1`, etc.
- `./solutions` is the directory where output files, such as `sol_0`, `sol_1`, etc., will be saved.

### Input File Format:
Each input file must follow this format:
1. The **text** (DNA sequence) is on the **first line**.
2. The **pattern** to be matched is on the **second line**.

### Output File Format:
For each input file `sample_<n>`, the program will generate an output file named `sol_<n>` in the output directory. Each output file will contain the 1-based positions of the pattern matches found in the text, with each match printed on a new line.