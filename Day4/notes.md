# Day 4 – Data Visualization with Matplotlib & Seaborn

---

## 🎯 Goals for the Day
- Learn the basics of **Matplotlib** and **Seaborn** for data visualization.
- Explore common chart types: line plots, bar charts, scatter plots, histograms, boxplots, and heatmaps.
- Visualize insights from a real-world dataset.

---

## 📝 Detailed Summary
Today was all about **turning data into visuals**. I learned that good visualizations are essential to quickly communicate insights.  

I practiced with the **Airbnb NYC dataset** and created:
- Line plots to show price trends
- Histograms to display price distributions
- Boxplots to check for outliers
- Heatmaps to show correlation between variables

I realized the power of Seaborn’s default styles for clean visuals, and how Matplotlib gives more customization control.

---

## 🔑 Key Concepts Learned
- **Matplotlib**: Core Python plotting library for flexible chart creation.
- **Seaborn**: High-level interface built on Matplotlib for statistical plots.
- **Heatmaps**: Show correlation between numeric features.
- **Customizing Plots**: Adding labels, titles, legends, and color palettes.

---

## 💻 Code Snippet
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("AB_NYC_2019.csv")

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()
