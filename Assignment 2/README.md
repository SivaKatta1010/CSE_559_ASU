### **My Comparison of Randomized Motif Search and Gibbs Sampling**

I ran both the **Randomized Motif Search (RMS)** and **Gibbs Sampling (GS)** algorithms to identify conserved motifs of length 15 in a DNA dataset. Here's what I found:

#### **Overview of Results**

**Randomized Motif Search (RMS):**

| **Run** | **Iterations** | **Consensus Sequence** | **Score** |
|---------|-----------------|------------------------|-----------|
| **1**   | 1,000           | AAAAAAGAGAGGGGT        | 40        |
|         | 10,000          | AAGAAAGAGCGGGGT        | 40        |
|         | 100,000         | AAAAAAGAGGGGGGT        | 39        |
| **2**   | 1,000           | ACAAAAAAGAGAGGG        | 43        |
|         | 10,000          | AAGAAAGAGCGGGGT        | 40        |
|         | 100,000         | AAAAAAGAGGGGGGT        | 38        |
| **3**   | 1,000           | AAAAATAGAGGGGTG        | 41        |
|         | 10,000          | AAAAAAGAGGGGGGT        | 39        |
|         | 100,000         | AAAAAATAGAGGGGT        | 39        |

**Gibbs Sampling (GS):**

| **Run** | **Iterations** | **Consensus Sequence** | **Score** |
|---------|-----------------|------------------------|-----------|
| **1**   | 1,000           | AAAAAAAAAGGAGGG        | 48        |
|         | 2,000           | AAAAAAGAGAGGGGT        | 40        |
|         | 10,000          | AAAAAATAGAGGGGT        | 38        |
| **2**   | 1,000           | AAGAAAAAGTAGGGG        | 46        |
|         | 2,000           | AAAAAAGAGGGGGGT        | 39        |
|         | 10,000          | AAAAAAGAGAGGGGG        | 41        |
| **3**   | 1,000           | CAAAAAAAAGGGGGG        | 43        |
|         | 2,000           | AAAATAGAGGGGGGT        | 42        |
|         | 10,000          | CAAAAAAAAGAGGGG        | 39        |


#### **Motif Scores:**
- **Randomized Motif Search (RMS):**
  - As I increased the iterations from **1,000** to **100,000**, the scores steadily improved. Starting with scores around 40-43 at 1,000 iterations, the scores decreased to 38-39 at 100,000 iterations.
  - **Best Score:** I achieved a score of **38** after **100,000 iterations**, indicating high conservation.
  
- **Gibbs Sampling (GS):**
  - GS reached competitive scores much faster. By **2,000 iterations**, I got a score of **39**, and it stayed around that level even up to **10,000 iterations** reaching its best score of 38.
  - **Best Score:** The lowest score I got was **38** within **10,000 iterations**.

#### **Convergence Speed:**
- **RMS:**
  - It took a large number of iterations (**up to 100,000**) to consistently reach the best scores.
  - The improvement was gradual, requiring significant computational effort.
  
- **GS:**
  - GS converged much quicker, finding near-optimal scores within just **2,000 iterations** and maintaining these scores up to **10,000 iterations**.
  - Although there was some variability in the results, overall, GS was much faster.

#### **Overall Observations:**
- **Efficiency:** GS was clearly more efficient, achieving good motif scores with far fewer iterations compared to RMS.
- **Score Optimization:** While RMS eventually found slightly better scores, it demanded a lot more iterations, making it less practical in terms of computational resources.
- **Consistency:** RMS provided more consistent improvements as I increased the iterations. On the other hand, GS had some variability but generally delivered solid results quickly.