# Machine Learning Models

Reference notes and short examples for the machine learning programs in this folder. Add each new model as a section below and link its notebook or source file from the index.

## Model Index

| Model | Dataset | Notebook | Test Result |
| --- | --- | --- | --- |
| Support Vector Machine (SVM) | Iris (scikit-learn) | [svm.ipynb](svm.ipynb) | 91.1% accuracy |

## 1. Support Vector Machine (SVM)

- **Goal:** Classify Iris flowers into setosa, versicolor, or virginica.
- **Dataset:** Built-in Iris dataset from scikit-learn; 150 rows and 4 numeric features.
- **EDA:** Class counts, feature correlations, and pairwise feature plots by species.
- **Preprocessing:** Stratified 70/30 train/test split (`random_state=42`); standardize features, then reduce them to 2 PCA components within a pipeline to prevent test-data leakage.
- **Model:** RBF-kernel SVC (`C=1.0`, `gamma="scale"`).
- **Evaluation:** 91.1% test accuracy. The two PCA components retain 96.0% of feature variance. Results and confusion matrix are shown in the notebook.
- **Visualization:** The notebook plots the fitted SVC's decision regions in PCA space, with train/test observations and support vectors.
- **Full walkthrough:** [svm.ipynb](svm.ipynb)

### Short Script

```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.30, random_state=42, stratify=iris.target
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=2)),
    ("svc", SVC(kernel="rbf", C=1.0, gamma="scale")),
])
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Test accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

## Model Entry Template

Copy this structure when documenting another model:

### Model Name

- **Goal:** What the model predicts or explains.
- **Dataset:** Source, size, and target.
- **EDA:** Main checks and visualizations.
- **Preprocessing:** Cleaning, feature transformations, and split strategy.
- **Model:** Algorithm and important parameters.
- **Evaluation:** Metrics and key results.
- **Visualization:** Relevant model or result plots.
- **Notebook/source:** Link to the implementation.

#### Short Script

```python
# Add the minimal runnable example here.
```