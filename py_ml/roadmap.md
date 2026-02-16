# Machine Learning Roadmap: Classical ML Stack

This roadmap outlines the exact order to study these topics, structured like a real-world Data Science pipeline.

---

## Phase 1: The Foundation (Statistics & Visualization)
> **Goal:** Understand the shape of your raw data before writing any logic.

* **Getting Started:** Setting up Python, Pandas, and NumPy.
* **Mean, Median, Mode:** Finding the basic center of your data.
* **Standard Deviation:** Measuring how spread out your data is.
* **Percentile:** Understanding where a specific data point stands relative to the rest.
* **Data Distribution:** Looking at the overall spread of your dataset.
* **Normal Data Distribution:** The "Bell Curve" (crucial because many models assume your data looks like this).
* **Scatter Plot:** Your first visual tool to see if two variables are related (e.g., Age vs. Income).

---

## Phase 2: Data Preprocessing (Cleaning the Mess)
> **Goal:** Translate text into numbers and standardize them so the algorithms don't crash.

* **Categorical Data:** Converting text features (like "USA" or "UK") into numeric codes (like 0 and 1).
* **Scale:** Standardizing your data. If you have "Age" (0-100) and "Salary" (0-150,000), scaling forces them onto the same playing field so Salary doesn't overpower Age.

---

## Phase 3: Regression (Predicting Numbers)
> **Goal:** Draw trend lines to forecast continuous values like pricing or temperatures.

* **Linear Regression:** Drawing a straight line through a Scatter Plot to predict a trend.
* **Multiple Regression:** Upgrading to multiple inputs (e.g., using Age *and* Experience to predict Salary).
* **Polynomial Regression:** Drawing a curved line for data that doesn't fit a straight, linear trend.

---

## Phase 4: The Reality Check (Model Validation)
> **Goal:** Prove your model is actually learning, not just memorizing the answers.

* **Train/Test:** Splitting your data. Train the model on 80%, and test it on the hidden 20%.
* **Cross Validation:** The advanced version of Train/Test. It rotates the 20% test chunk multiple times to ensure your model is robust.

---

## Phase 5: Classification (Predicting Categories)
> **Goal:** Build the core decision engine (like a Yes/No churn predictor).

* **Logistic Regression:** Your first classification model (predicting True/False or Yes/No).
* **Confusion Matrix:** The scorecard for a classification model (checking False Positives vs. False Negatives).
* **AUC - ROC Curve:** A visual graph to prove how accurate your classification model is.
* **Decision Tree:** A flowchart-based model (perfect for logic-based datasets).
* **K-nearest neighbors (KNN):** Predicting a label based on the labels of the data points closest to it mathematically.

---

## Phase 6: Advanced Supervised Learning & Tuning
> **Goal:** Maximize accuracy by tweaking settings and combining models.

* **Bootstrap Aggregation (Bagging):** Taking multiple Decision Trees and combining their votes to get a better answer.
* **Grid Search:** Writing a script to test hundreds of different settings on your model to automatically find the highest accuracy combination.

---

## Phase 7: Unsupervised Learning (Finding Hidden Patterns)
> **Goal:** Group unlabeled data for recommendation engines or user segmentation.

* **K-means:** Asking the algorithm to group your data into *K* number of distinct clusters.
* **Hierarchical Clustering:** Grouping data by building a tree-like hierarchy from the bottom up.