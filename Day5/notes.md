
---

### **Day5/notes.md**
```markdown
# Day 5 – Introduction to Scikit-learn & ML Workflow

---

## 🎯 Goals for the Day
- Understand the basic steps in a Machine Learning pipeline.
- Learn to use **Scikit-learn** for model training.
- Build a simple Linear Regression model.

---

## 📝 Detailed Summary
Today I learned the **ML process**:
1. Load data
2. Split into training and testing sets
3. Train the model
4. Make predictions
5. Evaluate performance

I built a simple **Linear Regression** model to predict house prices based on square footage.  

---

## 🔑 Key Concepts Learned
- **train_test_split()**: Dividing data into train/test sets to evaluate performance.
- **fit()**: Training the model.
- **predict()**: Making predictions.
- **R² Score**: Measures how well the model fits the data.

---

## 💻 Code Snippet
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("housing.csv")
X = df[['sqft_living']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("R² Score:", model.score(X_test, y_test))
