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
 
1. Start with the start node and goal node; put the start path in a queue (FIFO).
2. Create an empty visited set and set nodes explored = 0.
3. Remove the first path from the queue and take its last node.
4. If the node is already visited, skip it; otherwise mark it visited and increase nodes explored.
5. If the node is the goal, return the path and go to Step 8.
6. Add every unvisited neighbour to the END of the queue as a new path.
7. Repeat Steps 3 to 6 until the queue is empty (then report no path).
8. Record path length, nodes explored and time. Stop.
### Advantages
 
- Complete: always finds a solution if one exists in a finite graph.
- Optimal for equal-cost edges: gives the path with the fewest edges.
- Simple to implement and easy to understand.
### Disadvantages
 
- High memory use, O(b^d): stores every node of a level.
- Slow on large or deep graphs.
- Ignores edge costs, so not optimal for weighted graphs.
### Applications
 
- Shortest-path routing in unweighted maps and networks.
- Maze solving and puzzle solving (e.g. 8-puzzle).
- Web crawlers and social-network friend suggestions (degrees of separation).
- Network broadcasting and peer-to-peer discovery.
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
 
1. Start with the start node and goal node; push the start path onto a stack (LIFO).
2. Create an empty visited set and set nodes explored = 0.
3. Pop the top path from the stack and take its last node.
4. If the node is already visited, skip it; otherwise mark it visited and increase nodes explored.
5. If the node is the goal, return the path and go to Step 8.
6. Push every unvisited neighbour onto the TOP of the stack (in reverse order).
7. Repeat Steps 3 to 6 until the stack is empty (then report no path).
8. Record path length, nodes explored and time and compare with BFS. Stop.
### Advantages
 
- Low memory use, O(bm): stores only the current path.
- Can reach deep goals quickly, as seen here (4 nodes vs 7).
- Easy to implement with a stack or recursion.
### Disadvantages
 
- Not optimal: may return a longer path.
- Can go down very deep or infinite branches; needs a visited check.
- Not guaranteed to be complete on infinite graphs.
### Applications
 
- Maze generation and solving.
- Cycle detection and topological sorting.
- Finding connected components and solving puzzles such as Sudoku.
- Game-tree exploration and web crawling to a depth.
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
 
1. Start with the start node, goal node and heuristic h(n) of every node.
2. Put the start node in a priority queue ordered by h(n); create an empty visited set.
3. Remove the node with the SMALLEST h(n); skip it if already visited, else mark it visited.
4. If it is the goal, return the path and cost, and go to Step 7.
5. Add every unvisited neighbour to the queue with priority h(neighbour).
6. Repeat Steps 3 to 5 until the queue is empty (then report failure).
7. Record path cost, nodes explored and time. Stop.
**A\* Search**
 
1. Start with the start node, goal node, edge costs and h(n); set g(start) = 0.
2. Put the start node in a priority queue ordered by f(n) = g(n) + h(n).
3. Remove the node with the SMALLEST f(n); discard it if a cheaper route to it is already known.
4. If it is the goal, return the path and cost g, and go to Step 7.
5. For each neighbour, compute new g = g(node) + edge cost.
6. If new g is lower than the neighbour's best known cost, update it and add the neighbour with f = new g + h. Repeat Steps 3 to 6 until the queue is empty.
7. Record path cost, nodes explored and time and compare with Greedy. Stop.
### Advantages
 
- A* is complete and optimal with an admissible heuristic.
- Both use heuristics to explore fewer nodes than blind search.
- Greedy is very fast and simple.
### Disadvantages
 
- Greedy is neither optimal nor always complete.
- A* needs a good, admissible heuristic and large memory.
- Both depend on the quality of the heuristic.
### Applications
 
- GPS navigation and route planning (A*).
- Game AI and NPC path finding.
- Robot motion planning.
- Puzzle solving (8-puzzle, 15-puzzle) and network routing.
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
 
1. Start with the known facts and the list of rules (IF conditions THEN conclusion).
2. Take a rule and check whether ALL its conditions are in the known facts.
3. If yes and the conclusion is new, add it to the known facts.
4. Repeat Steps 2 and 3 for every rule in the list.
5. If any new fact was added in this pass, go back to Step 2.
6. If no new fact was added, no more rules can fire.
7. Display all derived facts. Stop.
**Backward Chaining**
 
1. Start with the desired goal.
2. If the goal is a known fact, conclude it is true and stop; if it is already being examined, return false (avoids loops).
3. Search for a rule whose conclusion matches the goal.
4. Identify the conditions required by that rule.
5. Check whether each condition is a known fact; if not, treat it as a sub-goal and repeat from Step 2.
6. If all conditions of some rule are established, conclude the goal is true.
7. Otherwise, the goal cannot be established.
8. Stop.
### Advantages
 
- Knowledge is stored as readable IF–THEN rules; decisions are explainable.
- Easy to update by adding or editing rules.
- Consistent and available at all times, unlike a human expert.
- Forward chaining derives all consequences; backward chaining answers a specific goal efficiently.
### Disadvantages
 
- Knowledge acquisition from experts is slow and costly.
- Cannot learn from data or handle uncertainty (propositional logic is true/false only).
- Large rule bases become hard to maintain and may be slow.
- Forward chaining may fire many irrelevant rules.
### Applications
 
- Medical diagnosis support (e.g. symptom to disease rules).
- Troubleshooting and technical help-desk systems.
- Loan or credit approval decisions.
- Configuration systems, legal advice and fault diagnosis.
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
 
1. Load the Titanic dataset and inspect it (head, info, describe, isna().sum()).
2. Remove duplicate rows.
3. Handle missing values: fill Age with the mean, Embarked with the mode (assign back), and drop Cabin.
4. Encode Sex (label encoding) and Embarked (one-hot); drop Name and Ticket.
5. Perform statistical analysis: correlation matrix and heatmap.
6. Plot a histogram of Fare and a boxplot of Age.
7. Scale Age and Fare with StandardScaler, then split into X and y (Survived).
8. Split into 80% training and 20% testing sets. Stop.
### Advantages
 
- Improves data quality and model accuracy.
- Scaling and encoding make data usable by most algorithms.
- EDA reveals patterns, outliers and relationships early.
### Disadvantages
 
- Time-consuming and needs domain judgement.
- Imputation can introduce bias; dropping columns loses information.
- Wrong choices (e.g. scaling before the split) can leak information.
### Applications
 
- Preparing data for any machine-learning project.
- Survival or risk prediction models.
- Business analytics, healthcare and finance data pipelines.
- Data-quality auditing and reporting.
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
 
1. Load the California Housing dataset and check shape, missing values and summary.
2. Select MedInc as the input X and Price as the target y.
3. Split the data into 80% training and 20% testing sets.
4. Train Linear Regression on the training set and predict the test set.
5. Create degree-2 polynomial features, train a second model and predict the test set.
6. Calculate MSE, MAE and R² for both models.
7. Tabulate and plot the results and compare the two models.
8. Stop.
### Advantages
 
- Linear regression is simple, fast and interpretable.
- Polynomial regression captures curved relationships.
- MSE, MAE and R² give a clear measure of performance.
### Disadvantages
 
- Linear regression cannot model non-linear patterns.
- Polynomial regression overfits at high degree and is sensitive to outliers.
- Using one feature limits accuracy (R² ≈ 0.46 here).
### Applications
 
- House and real-estate price prediction.
- Sales and demand forecasting.
- Salary, medical-cost and crop-yield estimation.
- Trend analysis in economics and engineering.
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
 
1. Load the Iris dataset; check shape, missing values and duplicates.
2. Drop Id, separate X and y, and encode Species with LabelEncoder.
3. Standardise the features with StandardScaler.
4. Split into 80% training and 20% testing sets.
5. Train Logistic Regression and KNN (e.g. k = 5) on the training set and predict the test set.
6. Calculate accuracy, confusion matrix, precision, recall and F1-score for both models.
7. Compare the results in a table and select the better model.
8. Stop.
### Advantages
 
- Logistic Regression is fast, simple and gives class probabilities.
- KNN needs no training and handles non-linear boundaries.
- Both work well on small, clean datasets such as Iris.
### Disadvantages
 
- Logistic Regression assumes a linear decision boundary.
- KNN is slow on large data and sensitive to scaling and the choice of k.
- Both are affected by irrelevant features and outliers.
### Applications
 
- Spam detection and credit-risk classification (Logistic Regression).
- Disease prediction and customer churn.
- Recommendation systems and image or handwriting recognition (KNN).
- Species and pattern classification.
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
 
1. Load the Iris dataset, drop Id and separate X and y.
2. Split into 80% training and 20% testing sets.
3. Train a Decision Tree (max_depth = 4) and a Gaussian Naïve Bayes model.
4. Predict the test set with both models.
5. Calculate accuracy, precision, recall and F1-score for both.
6. Plot the Decision Tree and build a comparison table.
7. Select the model with the highest accuracy as the most suitable.
8. Stop.
### Advantages
 
- Decision Tree is easy to interpret and visualise.
- Naïve Bayes is very fast and works with small training sets.
- Decision Tree needs little preprocessing and no scaling.
### Disadvantages
 
- Decision Trees overfit easily and are unstable to small data changes.
- Naïve Bayes assumes feature independence, which is rarely true.
- Gaussian Naïve Bayes assumes normally distributed features.
### Applications
 
- Medical diagnosis and loan approval (Decision Tree).
- Spam filtering and text/sentiment classification (Naïve Bayes).
- Real-time prediction and document categorisation.
- Customer segmentation and fault detection.
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
 
1. Load the Iris dataset and standardise the features.
2. For k = 1 to 10, run K-Means and record the WCSS (inertia).
3. Plot WCSS vs k and choose k at the elbow.
4. Run K-Means with the chosen k (assign points to nearest centroid, update centroids until no change).
5. Record cluster sizes and silhouette score. Stop.
**Hierarchical Clustering with Dendrogram**
 
1. Treat each data point as its own cluster and merge the two closest clusters (Ward linkage) until one remains.
2. Plot the dendrogram, cut it to get k clusters, and record cluster sizes and silhouette score.
3. Compare both methods in a table. Stop.
### Advantages
 
- Clustering needs no labels (unsupervised).
- K-Means is fast and scales to large data.
- Hierarchical clustering gives a dendrogram and does not need k in advance.
### Disadvantages
 
- K-Means needs k beforehand, is sensitive to initial centroids and outliers, and assumes round clusters.
- Hierarchical clustering is slow and memory-heavy on large data.
- Merges in hierarchical clustering cannot be undone.
### Applications
 
- Customer segmentation in marketing.
- Image compression and segmentation.
- Document and news grouping.
- Gene-expression analysis and anomaly detection.
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
 
1. Load the Breast Cancer dataset (30 features) and split into 80% training and 20% testing sets.
2. Train StandardScaler + Logistic Regression on all 30 features and record the accuracy.
3. Apply StandardScaler + PCA (retain 95% variance) and record the number of components.
4. Train Logistic Regression on the PCA features and record the accuracy.
5. Apply PCA with 2 components and plot a scatter plot coloured by class.
6. Plot cumulative explained variance with a 95% line.
7. Compare features and accuracy before and after PCA. Stop.
### Advantages
 
- Reduces the number of features (30 → 10) and training time.
- Removes correlated features and noise.
- Allows 2D/3D visualisation of high-dimensional data.
- Helps to reduce overfitting.
### Disadvantages
 
- Principal components are hard to interpret.
- Some information is lost (4.73% of variance here).
- Linear only; sensitive to feature scaling.
- Does not use class labels, so components may not be the most discriminative.
### Applications
 
- Image and face recognition.
- Gene and medical data analysis.
- Data visualisation and noise reduction.
- Preprocessing for machine-learning models and finance.
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
 
1. Load the Breast Cancer dataset and split into 80% training and 20% testing sets (stratified).
2. Define the baseline models: SVM (with scaling), Random Forest and AdaBoost.
3. Run 5-fold stratified cross-validation on each and record the metrics.
4. Define a hyperparameter grid for each model.
5. Run GridSearchCV for each model and keep the best estimator.
6. Evaluate baseline and tuned models on the test set (accuracy, precision, recall, F1, ROC-AUC).
7. Compare before and after optimisation and select the best model.
8. Stop.
### Advantages
 
- SVM is effective in high dimensions and with non-linear kernels.
- Random Forest reduces overfitting and handles many features.
- AdaBoost improves weak learners and often gives high accuracy.
- Cross-validation and Grid Search give reliable estimates and better parameters.
### Disadvantages
 
- Grid Search is computationally expensive.
- SVM is slow on very large data and needs scaling.
- AdaBoost is sensitive to noisy data and outliers.
- Random Forest is less interpretable.
### Applications
 
- Cancer and disease diagnosis.
- Fraud and spam detection.
- Image and text classification.
- Credit scoring, customer churn and face detection.
### Conclusion
| Model | Baseline CV acc | Tuned CV acc | Test acc (before → after) |
|---|---|---|---|
| SVM | 96.92% | 97.58% | 98.25% → 98.25% |
| Random Forest | 96.26% | 96.26% | 95.61% → 95.61% |
| AdaBoost | 96.70% | 98.02% | 95.61% → 95.61% |
 
AdaBoost (`learning_rate=1.0`, `n_estimators=100`) was best by cross-validation, but **tuning did not change test accuracy** for any model on this small, easy dataset. **SVM** had the best test accuracy and F1 (98.61%).
 
