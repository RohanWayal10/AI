## PR1: Uninformed Search – Breadth First Search (BFS)
 
### Title
Implementation of Breadth First Search for route finding.
 
### Aim
To implement BFS on a graph of locations and evaluate it by path length, nodes explored and execution time.
 
### Objective
- Represent a route-finding problem as a graph (adjacency list).
- Implement BFS using a FIFO queue that stores the full path.
- Measure path length, nodes explored and execution time with `time.perf_counter()`.
- Use the results as the baseline for comparison with DFS (PR2).
### Theory
Uninformed (blind) search uses no knowledge of how close a state is to the goal. BFS expands the **shallowest** unexpanded node first, level by level, using a **queue (FIFO)**. A visited set prevents re-expansion.
 
- **Complete:** yes (finite graph).
- **Optimal:** yes when all edges have equal cost (fewest edges).
- **Time / Space:** O(b^d) both, where b = branching factor, d = depth of the shallowest goal. Memory is the main weakness.
Graph used: `A→{B,C}, B→{D,E}, C→{F}, D→{G}, E→{G}, F→{G}`, start = `A`, goal = `G`.
 
### Algorithm
 
1. Start with the start node and the goal node.
2. Create a queue and insert the path containing only the start node.
3. Create an empty visited set and set nodes explored to 0.
4. Remove the first path from the queue and take its last node.
5. If this node is already visited, skip it and go to Step 4.
6. Mark the node as visited and increase nodes explored by 1.
7. If the node is the goal, return the path and stop.
8. Otherwise, add each unvisited neighbour to the END of the queue as a new path (current path + neighbour).
9. Repeat Steps 4 to 8 until the queue is empty.
10. If the queue becomes empty without reaching the goal, report that no path exists.
11. Record path length, nodes explored and execution time.
12. Stop.
### Conclusion
BFS returned **A → B → D → G**, path length **3**, exploring **7 nodes** (A, B, C, D, E, F, G). It guarantees the shortest path in number of edges but expands many nodes and needs more memory. BFS is the right choice when the shortest path matters and memory is affordable.
 
---
 
## PR2: Uninformed Search – Depth First Search (DFS)
 
### Title
Implementation of Depth First Search for route finding and comparison with BFS.
 
### Aim
To implement DFS on the same graph as PR1 and compare it with BFS on path length, nodes explored and execution time.
 
### Objective
- Implement DFS using a LIFO stack and a visited set.
- Push neighbours in reverse order so traversal is predictable (left-most child first).
- Compare BFS and DFS on the same three metrics.
- Understand when each strategy is preferable.
### Theory
DFS expands the **deepest** unexpanded node first using a **stack (LIFO)** or recursion.
 
- **Complete:** only on finite graphs with a visited check.
- **Optimal:** no – returns the first path found.
- **Time:** O(b^m); **Space:** O(bm), m = maximum depth (far less memory than BFS).
### Algorithm
 
1. Start with the start node and the goal node.
2. Create a stack and push the path containing only the start node.
3. Create an empty visited set and set nodes explored to 0.
4. Pop the top path from the stack and take its last node.
5. If this node is already visited, skip it and go to Step 4.
6. Mark the node as visited and increase nodes explored by 1.
7. If the node is the goal, return the path and stop.
8. Otherwise, push each unvisited neighbour onto the TOP of the stack as a new path, in reverse order so the left-most neighbour is explored first.
9. Repeat Steps 4 to 8 until the stack is empty.
10. If the stack becomes empty without reaching the goal, report that no path exists.
11. Record path length, nodes explored and execution time and compare with BFS.
12. Stop.
### Conclusion
DFS returned **A → B → D → G**, length **3**, exploring only **4 nodes** versus 7 for BFS. The equal path length is a property of this small graph, not a rule: DFS gives **no** shortest-path guarantee, BFS does. Use BFS for shortest paths; DFS when memory is limited or any solution is acceptable.
 
---
 
## PR3: Informed Search – Greedy Best First Search and A*
 
### Title
Shortest path finding using Greedy Best First Search and A* Search.
 
### Aim
To implement Greedy Best First Search and A* on a weighted graph and analyse optimality, completeness and efficiency.
 
### Objective
- Represent a weighted graph with edge costs and a heuristic h(n).
- Implement Greedy (f = h) and A* (f = g + h) using a priority queue (`heapq`).
- Compare path cost, nodes explored and execution time.
- Analyse optimality, completeness and efficiency.
### Theory
Informed search uses a heuristic h(n) estimating the cost from n to the goal.
 
- **Greedy Best First:** expands the node with the lowest h(n). Fast, but ignores the cost already paid → **not optimal**, not complete in general.
- **A\*:** expands the node with the lowest f(n) = g(n) + h(n). With an **admissible** heuristic (never overestimates) it is **complete and optimal**. Weakness: memory.
Heuristic used: `A=6, B=5, C=3, D=3, E=2, F=2, G=0`.
Edge costs: `A-B 1, A-C 4, B-D 2, B-E 5, C-E 1, C-F 5, D-G 3, E-G 2, F-G 2`.
 
### Algorithm
 
**Greedy Best First Search**
 
1. Start with the start node, the goal node and the heuristic value h(n) of every node.
2. Insert the start node into a priority queue ordered by h(n).
3. Create an empty visited set and set nodes explored to 0.
4. Remove the node with the SMALLEST h(n) from the queue.
5. If it is already visited, skip it and go to Step 4.
6. Mark it as visited and increase nodes explored by 1.
7. If it is the goal, return the path and its cost and go to Step 10.
8. Otherwise, insert every unvisited neighbour into the queue with priority h(neighbour).
9. Repeat Steps 4 to 8 until the queue is empty; if the goal is never reached, report failure.
10. Stop.
**A\* Search**
 
1. Start with the start node, the goal node, edge costs and h(n).
2. Insert the start node into a priority queue with f(start) = 0 + h(start); set best cost of start to 0.
3. Remove the node with the SMALLEST f(n) = g(n) + h(n), where g(n) is the cost from the start.
4. If its cost is higher than the best cost already recorded for it, discard it (outdated entry) and go to Step 3.
5. Increase nodes explored by 1.
6. If the node is the goal, return the path and its cost g and go to Step 9.
7. For each neighbour, compute new g = g(node) + edge cost.
8. If new g is lower than the best known cost of that neighbour, update its best cost and insert it into the queue with f = new g + h(neighbour). Repeat Steps 3 to 8 until the queue is empty; if the goal is never reached, report failure.
9. Record path, cost, nodes explored and execution time and compare with Greedy.
10. Stop.
### Conclusion
Greedy returned **A → C → E → G, cost 7**; A* returned **A → B → D → G, cost 6 (optimal)**. Both explored **4 nodes**, so A* gave the better answer at no extra search effort here. Greedy is quicker in general but can return a suboptimal path; A* with an admissible heuristic guarantees the least-cost path.
 
---
 
## PR4: Knowledge Representation and Expert System
 
### Title
Rule-based expert system using propositional logic with Forward and Backward Chaining.
 
### Aim
To build a rule-based expert system for medical decision making and implement forward and backward chaining inference.
 
### Objective
- Represent knowledge as facts and IF–THEN rules in propositional logic.
- Implement forward chaining (data-driven).
- Implement backward chaining (goal-driven) with a visited set to avoid infinite loops.
- Show how conclusions are derived step by step.
### Theory
An expert system = **knowledge base** (facts + rules) + **inference engine**. In propositional logic each symbol is true/false, and a rule such as `fever ∧ cough → flu` fires when all its conditions are known.
 
- **Forward chaining:** start from known facts, fire every applicable rule, add new facts, repeat until nothing changes. Good when many facts are available.
- **Backward chaining:** start from a goal, find rules that conclude it, recursively prove each condition. Efficient for proving one specific goal.
Knowledge base: facts `{fever, cough, body_pain}`; rules
`fever ∧ cough → flu`, `flu ∧ body_pain → viral_infection`, `viral_infection → take_rest`, `take_rest → recovery`.
 
### Algorithm
 
**Forward Chaining**
 
1. Start with the set of known facts and the list of rules (IF conditions THEN conclusion).
2. Take the first rule and check whether ALL its conditions are present in the known facts.
3. If they are, and the conclusion is not already known, add the conclusion to the known facts and print that the rule fired.
4. Move to the next rule and repeat Steps 2 and 3 for all rules.
5. If at least one new fact was added in this pass, repeat from Step 2.
6. If a full pass adds no new fact, no more rules can fire.
7. Display all derived facts.
8. Stop.
**Backward Chaining**
 
1. Start with the desired goal.
2. If the goal is already a known fact, conclude that it is true and stop.
3. If the goal is already being examined (in the visited set), return false to avoid an infinite loop; otherwise add it to the visited set.
4. Search for a rule whose conclusion matches the goal.
5. Identify the conditions required by that rule.
6. Check whether those conditions are already known facts.
7. If a condition is not known, treat it as a sub-goal and repeat Steps 2 to 6 for it.
8. Continue until all required conditions are established or no suitable rule is found.
9. If all conditions of some rule are satisfied, conclude that the goal is true.
10. Otherwise, the goal cannot be established.
11. Stop.
### Conclusion
Forward chaining fired four rules and derived **flu, viral_infection, take_rest, recovery**. Backward chaining with goal `recovery` traced the same chain back to the known facts and **proved the goal**. Forward chaining is best for deriving everything that follows from the facts; backward chaining for answering a specific question.
 
---
 
## PR5: Data Preprocessing and Exploratory Data Analysis
 
### Title
Data cleaning, preprocessing and EDA on the Titanic dataset.
 
### Aim
To prepare the Titanic dataset for machine learning and explore it statistically and visually.
 
### Objective
- Load the data (891 rows × 12 columns); inspect with `head`, `info`, `describe`.
- Detect/remove duplicates; handle missing values (Age 177, Cabin 687, Embarked 2).
- Encode categoricals (label encoding for Sex, one-hot for Embarked); drop Name, Ticket.
- Scale Age and Fare with `StandardScaler`.
- Perform statistical analysis (correlation matrix, heatmap) and plot histograms and boxplots.
- Split into training and testing sets.
### Theory
- **Cleaning:** remove duplicates and errors.
- **Missing values:** drop columns that are mostly empty (Cabin); impute mean/median (numeric) or mode (categorical).
- **Encoding:** label encoding (one integer per category), one-hot encoding (one binary column per category).
- **Scaling:** standardisation `z = (x − μ) / σ` puts features on comparable scales.
- **EDA:** histograms (distribution), boxplots (spread/outliers), correlation matrix (relationships).
- **Split:** 80/20 train/test so evaluation uses unseen data.
### Algorithm
 
1. Start by loading the Titanic dataset (train.csv) into a DataFrame.
2. Inspect the data using head(), tail(), info(), describe() and isna().sum().
3. Check for duplicate rows and remove them.
4. Fill missing Age values with the mean and missing Embarked values with the mode, and assign the results back to the DataFrame.
5. Drop the Cabin column because most of its values are missing (687 of 891).
6. Encode Sex using label encoding and Embarked using one-hot encoding.
7. Drop the non-useful columns Name and Ticket.
8. Compute the correlation matrix and display it as a heatmap.
9. Plot a histogram of Fare and a boxplot of Age to study distribution and outliers.
10. Standardise Age and Fare using StandardScaler.
11. Separate the features X and the target y (Survived).
12. Split the data into 80% training and 20% testing sets with random_state = 42.
13. Stop.
### Conclusion
No duplicates were found. Cabin was dropped (687 of 891 missing); Age and Embarked were handled by mean and mode imputation. Sex was label-encoded, Embarked one-hot-encoded, Age and Fare standardised. Strongest correlations with `Survived`: **Sex (−0.54)**, **Pclass (−0.34)**, **Fare (+0.26)**. Fare is heavily right-skewed with outliers. The split gave **712 training / 179 testing** samples.
 
---
 
## PR6: Regression Techniques
 
### Title
Linear and Polynomial Regression on the California Housing dataset.
 
### Aim
To implement Linear and Polynomial Regression, evaluate with MSE, MAE and R², and compare the results.
 
### Objective
- Load California Housing (20,640 samples); predict price from median income (`MedInc`).
- Split into 16,512 training / 4,128 testing samples.
- Fit a linear model and a degree-2 polynomial model.
- Compare MSE, MAE, R² and visualise both fits.
### Theory
- **Linear regression:** `y = b0 + b1·x`, fitted by minimising squared error.
- **Polynomial regression:** adds `x², x³ …` via `PolynomialFeatures`; fits curves, still linear in coefficients; high degree risks overfitting.
- **MSE:** mean of squared errors (penalises large errors). **MAE:** mean of absolute errors. **R²:** fraction of variance explained (1 = perfect, 0 = no better than the mean).
### Algorithm
 
1. Start by loading the California Housing dataset and building a DataFrame with the target column Price.
2. Check the shape, missing values and statistical summary.
3. Select MedInc as the input feature X and Price as the target y.
4. Split the data into 80% training and 20% testing sets (random_state = 42).
5. Train a Linear Regression model on the training data and predict the test data.
6. Calculate MSE, MAE and R² for the linear model.
7. Transform X into degree-2 polynomial features using PolynomialFeatures.
8. Train a second Linear Regression model on the polynomial features and predict the test data.
9. Calculate MSE, MAE and R² for the polynomial model.
10. Tabulate both results and plot the two fitted curves over the data.
11. Compare the models and decide which performs better.
12. Stop.
### Conclusion
| Model | MSE | MAE | R² |
|---|---|---|---|
| Linear | 0.7091 | 0.6299 | 0.4589 |
| Polynomial (deg 2) | 0.7033 | 0.6283 | 0.4633 |
 
Polynomial is slightly better on every metric, but the gain is tiny (≈0.004 in R²). Both explain only ~46% of variance because a single feature is used; **adding more features would help far more than a higher degree**.
 
---
 
## PR7: Classification using Logistic Regression and K-Nearest Neighbors
 
### Title
Classification of the Iris dataset using Logistic Regression and KNN.
 
### Aim
To preprocess the data, implement Logistic Regression and KNN, evaluate them, and compare the results.
 
### Objective
- Load and clean Iris (150 samples, 3 classes, no missing values/duplicates).
- Drop `Id`, label-encode `Species`, standardise the four features.
- Split into 120 training / 30 testing samples.
- Train both classifiers; evaluate with accuracy, confusion matrix, precision, recall, F1.
### Theory
- **Logistic Regression:** applies sigmoid (softmax for multi-class) to a linear combination of features and predicts the most probable class.
- **KNN:** lazy, distance-based; a sample gets the majority class among its k nearest training samples; needs scaled features.
- **Metrics:** accuracy = correct/total; precision = TP/(TP+FP); recall = TP/(TP+FN); F1 = 2PR/(P+R); confusion matrix shows TP/FP/TN/FN per class.
### Algorithm
 
1. Start by loading the Iris dataset.
2. Check the shape, missing values, duplicates and class counts.
3. Drop the Id column and separate the features X and the target y.
4. Encode the Species labels using LabelEncoder.
5. Standardise the features using StandardScaler.
6. Split the data into 80% training and 20% testing sets (random_state = 42).
7. Train a Logistic Regression model on the training data and predict the test data.
8. Train a KNN classifier (choose k, e.g. 5) on the training data and predict the test data.
9. For each model, calculate accuracy, confusion matrix, precision, recall and F1-score.
10. Compare the results of the two models in a table.
11. Select the better model and write the conclusion.
12. Stop.
### Conclusion
The data is clean and balanced (50 per class); petal length and petal width are strongly correlated (0.96). Preprocessing, scaling and the split are complete.
> ⚠️ **To complete:** the code in the source PDF stops after preprocessing and plots. Run steps 5–8 and insert the Logistic Regression and KNN metric values here before submitting.
 
---
 
## PR8: Classification using Decision Tree and Naïve Bayes
 
### Title
Comparison of Decision Tree and Naïve Bayes classifiers on the Iris dataset.
 
### Aim
To implement both classifiers, compare them using standard metrics, and identify the more suitable model.
 
### Objective
- Train a Decision Tree (`max_depth=4`) and Gaussian Naïve Bayes.
- Evaluate with accuracy, precision, recall, F1-score.
- Visualise the decision tree.
- Select the most suitable model from the comparison table.
### Theory
- **Decision Tree:** splits data on the feature/threshold that best separates classes (Gini impurity or entropy); gives readable rules; limited depth reduces overfitting.
- **Naïve Bayes:** Bayes' theorem `P(C|x) ∝ P(C) · ∏ P(xᵢ|C)` assuming features are independent given the class; Gaussian variant models each feature as normal. Fast and works with small data.
### Algorithm
 
1. Start by loading the Iris dataset and dropping the Id column.
2. Separate the features X and the target y.
3. Split the data into 80% training and 20% testing sets (random_state = 42).
4. Create a Decision Tree classifier with max_depth = 4 and train it on the training data.
5. Predict the test data and calculate accuracy, precision, recall and F1-score for the Decision Tree.
6. Plot the trained tree using plot_tree().
7. Create a Gaussian Naïve Bayes classifier and train it on the training data.
8. Predict the test data and calculate accuracy, precision, recall and F1-score for Naïve Bayes.
9. Build a comparison table of both models.
10. Select the model with the highest accuracy as the most suitable model.
11. Stop.
### Conclusion
| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Decision Tree | 93.33% | 93.33% | 93.33% | 93.33% |
| Naïve Bayes | 96.67% | 96.97% | 96.67% | 96.66% |
 
**Naïve Bayes** was selected. The test set has only 30 samples, so the gap equals **one** misclassified sample; cross-validation is needed before claiming a real difference.
 
---
 
## PR9: Clustering Techniques
 
### Title
K-Means and Hierarchical Clustering on the Iris dataset.
 
### Aim
To implement K-Means and Hierarchical clustering, determine the number of clusters with the Elbow Method and Dendrogram, and analyse the clusters.
 
### Objective
- Standardise the four Iris features.
- Plot WCSS vs k (Elbow Method) and choose k.
- Build a Ward-linkage dendrogram and cut it into clusters.
- Compare cluster sizes and silhouette scores.
### Theory
Clustering is **unsupervised**: it groups similar samples without labels.
- **K-Means:** assign each point to the nearest of k centroids, recompute centroids, repeat; minimises WCSS. **Elbow Method:** plot WCSS vs k and pick where improvement flattens.
- **Hierarchical (agglomerative):** repeatedly merge the two closest clusters (Ward = merge with least variance increase); the **dendrogram** is cut at a height to get clusters.
- **Silhouette score** (−1 to 1): how well a point fits its own cluster vs others; higher is better.
### Algorithm
 
**K-Means with Elbow Method**
 
1. Start by loading the Iris dataset and standardising the features.
2. For k = 1 to 10, run K-Means and record the inertia (WCSS).
3. Plot WCSS against k and choose k at the "elbow" of the curve.
4. Select k initial centroids.
5. Assign every point to its nearest centroid.
6. Recompute each centroid as the mean of its assigned points.
7. Repeat Steps 5 and 6 until the assignments no longer change.
8. Record the cluster sizes and silhouette score.
**Hierarchical Clustering with Dendrogram**
 
9. Treat every data point as its own cluster.
10. Merge the two closest clusters using Ward linkage and repeat until one cluster remains.
11. Plot the dendrogram and cut it at a suitable height to get k clusters.
12. Record the cluster sizes and silhouette score.
13. Compare K-Means and Hierarchical clustering in a table.
14. Stop.
### Conclusion
Both methods indicated **k = 3**.
 
| Algorithm | Cluster sizes | Silhouette |
|---|---|---|
| K-Means | 53 / 50 / 47 | 0.4599 |
| Hierarchical (Ward) | 71 / 49 / 30 | 0.4467 |
 
K-Means gave slightly better separation and more balanced clusters (closer to the true 50/50/50 split); hierarchical clustering provides the dendrogram and does not need k in advance.
 
---
 
## PR10: Dimensionality Reduction using PCA
 
### Title
Principal Component Analysis on the Breast Cancer dataset.
 
### Aim
To apply PCA on a high-dimensional dataset and study its effect on feature count, visualisation and classification performance.
 
### Objective
- Load Breast Cancer (569 samples, 30 features); standardise.
- Apply PCA retaining 95% variance.
- Visualise in 2D and plot cumulative explained variance.
- Compare Logistic Regression accuracy before and after PCA.
### Theory
PCA is an unsupervised linear technique that finds orthogonal axes (principal components) ordered by the variance they capture. Projecting onto the first few components reduces features, noise and computation, lessens the curse of dimensionality and enables 2D/3D plots. Features must be standardised first. Trade-off: components are mixtures of original features and are harder to interpret.
 
### Algorithm
 
1. Start by loading the Breast Cancer dataset (569 samples, 30 features).
2. Split the data into 80% training and 20% testing sets (random_state = 42, stratified).
3. Build a pipeline of StandardScaler followed by Logistic Regression and train it on the original 30 features.
4. Record the test accuracy as "accuracy without PCA".
5. Build a second pipeline of StandardScaler, PCA (retain 95% variance) and Logistic Regression and train it.
6. Record the number of components kept, the variance retained and the test accuracy as "accuracy with PCA".
7. Apply PCA with 2 components on the scaled data and plot a scatter plot coloured by class.
8. Plot the cumulative explained variance against the number of components with a 95% line.
9. Compare features and accuracy before and after PCA in a table.
10. Stop.
### Conclusion
| Measure | Before PCA | After PCA |
|---|---|---|
| Number of features | 30 | 10 |
| Test accuracy | 98.25% | 97.37% |
 
10 components retain **95.27%** of variance; the first two explain 63.24%. The accuracy drop is **0.88 points (one of 114 test samples)** — a threefold reduction in features at almost no cost.
 
---
 
## PR11: Advanced Machine Learning and Model Optimization
 
### Title
SVM, Random Forest and AdaBoost with Cross-Validation and Grid Search.
 
### Aim
To implement and compare SVM, Random Forest and AdaBoost, and evaluate them before and after hyperparameter tuning.
 
### Objective
- Train the three models on Breast Cancer (455 train / 114 test, stratified).
- Apply 5-fold stratified cross-validation.
- Tune hyperparameters with `GridSearchCV`.
- Compare accuracy, precision, recall, F1, ROC-AUC before and after optimisation.
### Theory
- **SVM:** finds the maximum-margin hyperplane; kernels (RBF) handle non-linear boundaries; parameters C, kernel, gamma; needs scaled data.
- **Random Forest:** bagging of many decision trees on random data/feature subsets; majority vote reduces variance.
- **AdaBoost:** boosting – weak learners trained sequentially, misclassified samples get higher weight; weighted vote.
- **Cross-validation:** train on k−1 folds, validate on 1, rotate; a more reliable estimate than one split.
- **Grid Search:** tries every hyperparameter combination, keeps the best CV score.
### Algorithm
 
1. Start by loading the Breast Cancer dataset.
2. Split the data into 80% training and 20% testing sets (stratified, random_state = 42).
3. Define the baseline models: SVM (with StandardScaler), Random Forest and AdaBoost.
4. Create a 5-fold stratified cross-validation object.
5. Run cross-validation on each baseline model and record mean accuracy, precision, recall, F1 and ROC-AUC.
6. Define a hyperparameter grid for each model (SVM: C, kernel, gamma; Random Forest: n_estimators, max_depth, min_samples_split; AdaBoost: n_estimators, learning_rate).
7. Run GridSearchCV for each model and store the best parameters and the best estimator.
8. Evaluate every baseline model and every tuned model on the test set using the five metrics.
9. Compare performance before and after optimisation in a table and a bar chart.
10. Select the best model based on the cross-validation score.
11. Stop.
### Conclusion
| Model | Baseline CV acc | Tuned CV acc | Test acc (before → after) |
|---|---|---|---|
| SVM | 96.92% | 97.58% | 98.25% → 98.25% |
| Random Forest | 96.26% | 96.26% | 95.61% → 95.61% |
| AdaBoost | 96.70% | 98.02% | 95.61% → 95.61% |
 
AdaBoost (`learning_rate=1.0`, `n_estimators=100`) was best by cross-validation, but **tuning did not change test accuracy** for any model on this small, easy dataset. **SVM** had the best test accuracy and F1 (98.61%).
 
