
---

### **Day6/notes.md**
```markdown
# Day 6 – Project #1: Student Score Predictor
---

## 🎯 Goals for the Day
- Apply the full ML workflow to a real dataset.
- Use Linear Regression to predict student exam scores.

---

## 📝 Detailed Summary
Today I worked with the **Student Scores dataset**, which has two columns: hours studied and scores.  

Steps followed:
1. Loaded and explored the dataset.
2. Visualized the relationship between hours and scores using a scatter plot.
3. Trained a Linear Regression model.
4. Evaluated it using R² score and MAE.

I recorded a short **Streamlit app demo** for visualizing predictions interactively.

---

## 🔑 Key Concepts Learned
- **EDA (Exploratory Data Analysis)**: Identifying trends before modeling.
- **Regression Line**: Shows the relationship between variables.
- **MAE (Mean Absolute Error)**: Measures prediction error.

---

## 💻 Code Snippet
```python
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.show()

predictions = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, predictions))
