# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "matplotlib",
#   "seaborn"
# ]
# ///

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Autolysis started")

# Read filename from command line
filename = sys.argv[1]

# Load CSV
df = pd.read_csv(filename)

print("CSV loaded successfully")

# Basic info
rows, cols = df.shape
missing = df.isna().sum()

# Plot missing values
plt.figure(figsize=(8,4))
missing.plot(kind="bar")
plt.title("Missing Values per Column")
plt.tight_layout()
plt.savefig("missing.png")
plt.close()

# Correlation plot (numeric only)
numeric = df.select_dtypes(include="number")
if not numeric.empty:
    plt.figure(figsize=(6,5))
    sns.heatmap(numeric.corr(), cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("correlation.png")
    plt.close()

# Write README
with open("README.md", "w") as f:
    f.write("# Automated Analysis\n\n")
    f.write(f"Rows: {rows}\n\n")
    f.write(f"Columns: {cols}\n\n")
    f.write("## Missing Values\n")
    f.write(missing.to_string())
    f.write("\n\n")
    f.write("## Visualizations\n")
    f.write("![Missing](missing.png)\n")
    if not numeric.empty:
        f.write("![Correlation](correlation.png)\n")

print("Analysis complete")
