# Lab Notes — Random Variable Generation
**Group:** 8  
**Date started:** 2026-04-10  
**Seed:** 8 (group number)

---

## Group 8 Parameters (from lab PDF table)

| Distribution       | Parameters                  |
|--------------------|-----------------------------|
| Uniform (int)      | [70, 90]                    |
| Uniform (real)     | [7.0, 9.0]                  |
| Normal             | mean = 10, std = 2          |
| Exponential        | mean = 0.25                 |
| Other (Bernoulli)  | p = 0.25                    |

> **Note on Bernoulli p-value:** The PDF table lists `0.25` for group 8 under the "Exponential" mean column, and "Bernoulli" as the "Other" distribution.
> We are using p=0.25 for the Bernoulli as it is the value assigned to group 8 in the exponential column — this needs confirmation with the professor.
> **TODO:** Clarify if the Bernoulli p is the same value as the exponential mean (0.25), or if it is independently defined.

---

## Setup

- **Python environment:** `.venv` in `useej7-performance-eval/`
- **Libraries:** numpy 2.4.4, matplotlib 3.10.8, scipy 1.17.1
- **Script:** `main.py` — generates all individual histograms and 4-panel overview figures
- **Output:** `results/figures/`

---

## Observations

### Uniform Integer [70, 90]

- **n=10:** Very sparse — only 10 integers sampled from a pool of 21. Several values are missing entirely; one value (78) dominates with relative frequency 0.20 due to the small sample. Histogram is clearly irregular.
- **n=100:** Histogram starts to have all (or most) values represented, but variance between bins is still large (e.g., 79 nearly absent vs. 71 at ~0.09).
- **n=1,000:** The shape is visibly converging toward flat. All bins are occupied; spread between min/max bar heights reduces significantly.
- **n=10,000:** Near-perfect uniform distribution. All 21 integer values have relative frequencies very close to the theoretical 1/21 ≈ 0.0476. Clear convergence to the uniform law.
- **Key insight:** The convergence to a flat distribution is a direct illustration of the Law of Large Numbers. With a discrete uniform distribution over 21 integers, each value should appear with equal probability of ~4.76%.

---

### Uniform Real [7.0, 9.0]

- **n=10:** Extremely sparse — only 3 visible bins. Histogram is dominated by a tall bar around 8.0 (density ~1.3), which is an artifact of very few, clustered samples.
- **n=100:** Shape is starting to be recognizable as roughly flat, but significant variation between bins remains (density range ~0.4 to 0.75 instead of theoretical constant 0.5).
- **n=1,000:** Density values settle closer to 0.5, with minor fluctuations. The flat shape is now clearly visible.
- **n=10,000:** Excellent convergence to the theoretical density of 0.5 = 1 / (9.0 - 7.0). All bins hover around 0.5 with very small variance.
- **Key insight:** The theoretical density of a Uniform(a, b) is 1/(b-a) = 1/2 = 0.5. This is clearly achieved at large n. Also note that the continuous uniform looks identical to the discrete uniform in terms of convergence behavior, but density (not count) is plotted.

---

### Normal (μ=10, σ=2)

- **n=10:** Completely unrecognizable as a bell curve. With only 10 points, the histogram shows random, irregular spikes. No symmetric structure visible.
- **n=100:** A rough bell-like shape begins to emerge, but asymmetry and noise are still prominent.
- **n=1,000:** Unmistakable Gaussian bell curve. Peak near μ=10, symmetric tails, most values concentrated in [6, 14] (±2σ range).
- **n=10,000:** Smooth, visually perfect bell curve. The ±1σ range [8, 12] visibly contains ~68% of the area. Long tails extending to ~2–18 are visible.
- **Key insight:** The Normal distribution requires the largest n to become recognizable. The bell shape is one of the most n-sensitive amongst the 5 distributions: small n leads to very misleading histograms.

---

### Exponential (mean=0.25)

- **n=10:** Rough decreasing shape, but with only 5 visible bins; the rightmost bar appears spuriously high due to sampling noise.
- **n=100:** Clearly decreasing, right-skewed shape. The high-density region near 0 is visible, with the tail extending to ~1.0.
- **n=1,000:** Well-defined exponential decay. Sharp peak at 0, smooth decline. Tail extends to ~2.0.
- **n=10,000:** Very smooth exponential curve. Rate λ = 1/mean = 4 visually matches: f(0) ≈ 4, exponential decay clearly visible to the right.
- **Key insight:** The exponential distribution (mean=0.25) converges relatively quickly — the right-skewed shape is recognizable even at n=100. This is because it has a characteristic and distinctive shape (unlike normal or uniform). The extremely small mean (0.25) means most values cluster very close to 0.

---

### Bernoulli (p=0.25)

- **n=10:** Relative frequencies: ~70% zeros, ~30% ones. Already close to theoretical (75%/25%), but with a ±5% error due to small n.
- **n=100:** Very close to theoretical: ~75% zeros, ~23% ones. Differences are within statistical noise.
- **n=1,000:** Almost indistinguishable from n=10,000. P(X=0) ≈ 0.748, P(X=1) ≈ 0.252 — extremely close to theoretical 0.75/0.25.
- **n=10,000:** Converges almost exactly to P(X=0)=0.75, P(X=1)=0.25.
- **Key insight:** Bernoulli converges fastest among all distributions because it has only 2 possible outcomes. Even n=10 gives a qualitatively correct shape. This is why it is easy to estimate a Bernoulli parameter p with relatively few samples compared to a continuous distribution.
- **Comparison note:** Unlike continuous distributions, Bernoulli is already essentially converged by n=100. The practical difference between n=1,000 and n=10,000 is minimal for a Bernoulli.

---

## Cross-Distribution Comparison

| Distribution | Recognizable at n= | Convergence speed | Type |
|---|---|---|---|
| Uniform (int) | ~1,000 | Medium | Discrete |
| Uniform (real) | ~1,000 | Medium | Continuous |
| Normal | ~1,000 | Slow | Continuous |
| Exponential | ~100 | Fast | Continuous |
| Bernoulli | ~10 | Very fast | Discrete |

- **Discrete distributions** (Uniform int, Bernoulli) converge in shape quickly but need n large enough to populate all possible values.
- **Continuous distributions** as a group need more samples, but the rate depends heavily on the shape: exponential (distinctive) < uniform (flat) < normal (subtle bell).

