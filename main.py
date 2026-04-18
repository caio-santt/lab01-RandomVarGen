"""
Lab: Random Variable Generation
Course: USEEJ7 - Performance Evaluation of Computer Systems (NCA - CNAM)
Professor: Pedro Braconnot Velloso

Group: 8
Parameters:
  - Uniform (int):  [70, 90]
  - Uniform (real): [7.0, 9.0]
  - Normal:         mean=10, std=2
  - Exponential:    mean=0.25
  - Other:          Bernoulli (p=0.25)

Seed: 8 (group number)
N values: 10, 100, 1000, 10000
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# ─── Configuration ──────────────────────────────────────────────────────────

GROUP = 8
np.random.seed(GROUP)

N_VALUES = [10, 100, 1_000, 10_000]
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Generators ─────────────────────────────────────────────────────────────

def gen_uniform_int(n):
    """Uniform integer distribution in [70, 90]."""
    return np.random.randint(70, 91, size=n)  # randint is exclusive on high end


def gen_uniform_real(n):
    """Uniform real (float) distribution in [7.0, 9.0]."""
    return np.random.uniform(7.0, 9.0, size=n)


def gen_normal(n):
    """Normal distribution with mean=10, std=2."""
    return np.random.normal(loc=10, scale=2, size=n)


def gen_exponential(n):
    """Exponential distribution with mean=0.25."""
    return np.random.exponential(scale=0.25, size=n)


def gen_bernoulli(n):
    """Bernoulli distribution with p=0.25 (Group 8 'other' distribution).
    Uses numpy so it respects the global np.random.seed set before each call.
    """
    return np.random.binomial(n=1, p=0.25, size=n)


# ─── Distributions metadata ──────────────────────────────────────────────────

DISTRIBUTIONS = [
    {
        "key":    "uniform_int",
        "label":  "Uniform Integer [70, 90]",
        "gen":    gen_uniform_int,
        "discrete": True,
    },
    {
        "key":    "uniform_real",
        "label":  "Uniform Real [7.0, 9.0]",
        "gen":    gen_uniform_real,
        "discrete": False,
    },
    {
        "key":    "normal",
        "label":  "Normal (μ=10, σ=2)",
        "gen":    gen_normal,
        "discrete": False,
    },
    {
        "key":    "exponential",
        "label":  "Exponential (mean=0.25)",
        "gen":    gen_exponential,
        "discrete": False,
    },
    {
        "key":    "bernoulli",
        "label":  "Bernoulli (p=0.25)",
        "gen":    gen_bernoulli,
        "discrete": True,
    },
]

# ─── Plotting ────────────────────────────────────────────────────────────────

def plot_histogram(data, dist, n):
    """Generate and save a single histogram for a given distribution and n."""
    fig, ax = plt.subplots(figsize=(7, 4.5))

    if dist["discrete"]:
        # For discrete distributions: bar plot with exact counts
        values, counts = np.unique(data, return_counts=True)
        ax.bar(values, counts / n, color="#4A90D9", edgecolor="white",
               linewidth=0.6, alpha=0.85, width=0.4)
        ax.set_xticks(values)
    else:
        ax.hist(data, bins="auto", density=True,
                color="#4A90D9", edgecolor="white", linewidth=0.6, alpha=0.85)

    ax.set_title(f"{dist['label']}  —  n = {n:,}", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Value", fontsize=11)
    ax.set_ylabel("Density" if not dist["discrete"] else "Relative Frequency", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=9)

    plt.tight_layout()
    fname = f"{dist['key']}_n{n}.png"
    fig.savefig(os.path.join(OUTPUT_DIR, fname), dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: results/figures/{fname}")


def plot_overview(dist):
    """4-panel overview figure for a single distribution across all N values."""
    fig, axes = plt.subplots(1, 4, figsize=(18, 4.5), sharey=False)
    fig.suptitle(dist["label"], fontsize=14, fontweight="bold", y=1.02)

    for ax, n in zip(axes, N_VALUES):
        np.random.seed(GROUP)          # reset seed for reproducibility
        data = dist["gen"](n)
        if dist["discrete"]:
            values, counts = np.unique(data, return_counts=True)
            ax.bar(values, counts / n, color="#4A90D9", edgecolor="white",
                   linewidth=0.6, alpha=0.85, width=0.4)
            ax.set_xticks(values)
        else:
            ax.hist(data, bins="auto", density=True,
                    color="#4A90D9", edgecolor="white", linewidth=0.6, alpha=0.85)

        ax.set_title(f"n = {n:,}", fontsize=11)
        ax.set_xlabel("Value", fontsize=9)
        ax.set_ylabel("Density" if not dist["discrete"] else "Rel. Freq.", fontsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=8)

    plt.tight_layout()
    fname = f"{dist['key']}_overview.png"
    fig.savefig(os.path.join(OUTPUT_DIR, fname), dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: results/figures/{fname}  [overview]")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print(f"=== Random Variable Generation — Group {GROUP} ===")
    print(f"Seed: {GROUP}\n")

    for dist in DISTRIBUTIONS:
        print(f"{'=' * 60}")
        print(f"Distribution: {dist['label']}")
        print(f"{'=' * 60}")

        # Individual histograms for each n
        for n in N_VALUES:
            np.random.seed(GROUP)      # reset seed before each generation
            data = dist["gen"](n)

            # --- Print values to screen (lab requirement) ---
            print(f"\n  n = {n:,} values:")
            print(f"  {data.tolist()}")
            # ------------------------------------------------

            plot_histogram(data, dist, n)

        # Multi-panel overview
        plot_overview(dist)
        print()

    print("Done! All figures saved to results/figures/")


if __name__ == "__main__":
    main()
