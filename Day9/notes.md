
---

### **Day9/notes.md**
```markdown
# Day 9 – Decision Trees & Random Forests

---

## 🎯 Goals for the Day
- Learn how Decision Trees work.
- Understand ensemble methods like Random Forests.

---

## 📝 Detailed Summary
Today I built **Decision Tree** and **Random Forest** classifiers on the Titanic dataset.  

Decision Trees split data based on feature thresholds, but they can overfit easily.  
Random Forests combine multiple trees to improve generalization.

---

## 🔑 Key Concepts Learned
- **Gini Impurity**: Measures node impurity.
- **Ensemble Learning**: Combining models for better accuracy.
- **Feature Importance**: Shows which features impact predictions most.

---

## 💻 Code Snippet
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

tree = DecisionTreeClassifier()
forest = RandomForestClassifier(n_estimators=100)

tree.fit(X_train, y_train)
forest.fit(X_train, y_train)

print("Tree Accuracy:", tree.score(X_test, y_test))
print("Forest Accuracy:", forest.score(X_test, y_test))
