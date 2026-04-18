# Lab 01: Random Variable Generation

Repository for the Performance Evaluation of Computer Systems (USEEJ7) lab at NCA - CNAM.

## 📊 Overview
Implementation of random variable generators for various probability distributions using Python and NumPy. This project satisfies the requirements for **Group 8** of the lab.

### 🎯 Distributions Implemented
- **Uniform (Integer)**: Range [70, 90]
- **Uniform (Real)**: Range [7.0, 9.0]
- **Normal**: μ = 10, σ = 2
- **Exponential**: mean = 0.25 (λ = 4)
- **Bernoulli**: p = 0.25

## 📁 Project Structure
- `main.py`: The primary script containing the generators and plotting logic.
- `results/`: Contains generated histograms and notes on convergence.
  - `figures/`: Individual and overview plots for $n = \{10, 100, 1000, 10000\}$.
  - `notes.md`: Detailed analysis and observations.

## 🚀 How to Run
1. Ensure you have Python installed.
2. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```
3. Execute the script:
   ```bash
   python main.py
   ```

## 👥 Authors
- **Caio Trigueiro** (Group 8)
- Course: USEEJ7 - Performance Evaluation
- Professor: Pedro Braconnot Velloso
