import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_ext = np.arange(df["Year"].min(), 2051)
    sea_levels_ext = result.slope * years_ext + result.intercept
    ax.plot(years_ext, sea_levels_ext, 'r', label="Best Fit Line (All Data)")

    df_recent = df[df["Year"] >= 2000]
    result_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    sea_levels_recent = result_recent.slope * years_recent + result_recent.intercept
    ax.plot(years_recent, sea_levels_recent, 'g', label="Best Fit Line (Since 2000)")

    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    plt.savefig('sea_level_plot.png')
    return ax
