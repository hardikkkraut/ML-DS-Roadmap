
---

### **Day10/notes.md**
```markdown
# Day 10 – Project #2: Titanic Survivor Prediction

---

## 🎯 Goals for the Day
- Build multiple classification models on the Titanic dataset.
- Compare their performance.

---

## 📝 Detailed Summary
Today’s project was about predicting whether a passenger survived the Titanic disaster.  

Steps:
1. Loaded Titanic dataset from Kaggle.
2. Cleaned missing values (`Age`, `Embarked`).
3. Encoded categorical features using OneHotEncoder.
4. Trained Logistic Regression, Random Forest, and XGBoost.
5. Compared models using accuracy and ROC-AUC score.

---

## 🔑 Key Concepts Learned
- **Feature Engineering**: Creating `FamilySize` from `SibSp` and `Parch`.
- **Encoding**: Converting categorical variables into numeric form.
- **Model Comparison**: Using multiple metrics, not just accuracy.

---

## 💻 Code Snippet
```python
from sklearn.metrics import roc_auc_score

for model in [log_reg, forest, xgb]:
    y_pred = model.predict(X_test)
    print(model.__class__.__name__, "AUC:", roc_auc_score(y_test, y_pred))
