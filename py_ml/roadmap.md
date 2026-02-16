Phase 1: The Foundation (Statistics & Visualization)
Before you touch any AI, you need to understand the shape of your data.

Getting Started: (Setting up Python, Pandas, NumPy).

Mean Median Mode: The basic center of your data.

Standard Deviation: How spread out your data is.

Percentile: Understanding where a specific data point stands.

Data Distribution: Looking at the overall spread.

Normal Data Distribution: The "Bell Curve" (crucial because many models assume your data looks like this).

Scatter Plot: Your first visual tool to see if two things are related (e.g., Age vs. Income).

Phase 2: Data Preprocessing (Cleaning the Mess)
Models only understand numbers. You have to translate the real world into math before feeding it to an algorithm.

Categorical Data: Converting text like "USA" or "UK" (from your CSV) into numbers (like 0 and 1).

Scale: Standardizing your data. If you have "Age" (0-100) and "Salary" (0-150,000), the model will weigh Salary too heavily. Scaling forces them onto the same playing field.

Phase 3: Regression (Predicting Numbers)
Now you build your first predictive models. You start here because drawing a line through data is the easiest concept to grasp.

Linear Regression: Drawing a straight line through a Scatter Plot to predict a trend.

Multiple Regression: Upgrading to multiple inputs (e.g., using Age and Experience to predict Salary).

Polynomial Regression: Drawing a curved line for data that doesn't fit a straight trend.

Phase 4: The Reality Check (Model Validation)
Before moving to harder models, you must learn how to test if your model is actually learning or just memorizing the answers.

Train/Test: Splitting your data. Train on 80%, test on the hidden 20%.

Cross Validation: The advanced version of Train/Test. It rotates the 20% chunk to make sure your model is robust and not just lucky.

Phase 5: Classification (Predicting Categories)
Now you switch from predicting numbers to predicting labels (like the "YES/NO" in your comedian dataset).

Logistic Regression: Despite the word "regression," this is your first classification model (predicting True/False).

Confusion Matrix: How you grade a classification model (checking False Positives vs. False Negatives).

AUC - ROC Curve: A visual graph to prove how good your classification model is.

Decision Tree: A flowchart-based model (perfect for that Comedian dataset).

K-nearest neighbors (KNN): Predicting a label based on the labels of the data points closest to it.

Phase 6: Advanced Supervised Learning & Tuning
Making your existing models stronger.

Bootstrap Aggregation (Bagging): Taking multiple Decision Trees and combining their votes to get a better answer (the foundation of Random Forest).

Grid Search: Writing a script to test hundreds of different settings on your model to automatically find the most accurate combination.

Phase 7: Unsupervised Learning (Finding Hidden Patterns)
Finally, you tackle data that has no answers or labels.

K-means: Asking the algorithm to group your data into K number of distinct clusters.

Hierarchical Clustering: Grouping data by building a tree-like hierarchy from the bottom up.