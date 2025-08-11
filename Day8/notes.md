# Day 8 – Logistic Regression for Classification

---

## 🎯 Goals for the Day
- Understand **classification problems**.
- Apply Logistic Regression to a real dataset.

---

## 📝 Detailed Summary
Today I learned that Logistic Regression predicts **probabilities**, not continuous values.  

I applied it to the **Breast Cancer dataset**:
- Preprocessed data
- Trained the model
- Evaluated using accuracy score, confusion matrix, and classification report

---

## 🔑 Key Concepts Learned
- **Sigmoid Function**: Converts scores into probabilities.
- **Confusion Matrix**: Shows correct vs incorrect predictions.
- **Precision & Recall**: Useful for imbalanced datasets.

---

## 💻 Code Snippet
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
