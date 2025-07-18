import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
low = df["value"].quantile(0.025)
high = df["value"].quantile(0.975)
df = df[(df["value"] >= low) & (df["value"] <= high)]


def draw_line_plot():
    # Copy DataFrame
    df_line = df.copy()

    # Create figure and plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line["value"], color="red", linewidth=1)

    # Set titles and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Return image
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and prepare data
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Group and pivot for bar plot
    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Ensure month order
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    df_grouped = df_grouped[month_order]

    # Plot
    fig = df_grouped.plot(kind="bar", figsize=(12, 8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.tight_layout()
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month

    # Sort by month number for proper order
    df_box = df_box.sort_values("month_num")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.tight_layout()
    fig.savefig("box_plot.png")
    return fig
