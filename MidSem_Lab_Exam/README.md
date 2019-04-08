#	Mid Sem Lab Exam - Report
-	Date : 27 March 2019
-	CED15I031

##	Problem Statement
-	[Mushroom Data](https://archive.ics.uci.edu/ml/datasets/Mushroom) @ UCI
1.	Test drive any four built in classifiers supported by your platform to classify the test data sets.
2.	Compare the four classifiers for their performance measures (detailed measures).
3.	Test drive the Association Rule based Classifier implemented as part of your lab exercise over this data set.
4.	Compare the model in (3) to any one in (1) in terms of detailed performance measures.

##	Solution
1.	Classifiers tested
	-	[Complement Naive Bayes Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html) from SciKit Learn
		>	Output
		>	![OP_1.1.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_1.1.png)
	-	[Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) from SciKit Learn
		>	Output
		>	![OP_1.2.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_1.2.png)
	-	[Nearest Neighbors Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) from SciKit Learn
		>	Output
		>	![OP_1.3.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_1.3.png)
	-	[Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) from SciKit Learn
		>	Output
		>	![OP_1.4.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_1.4.png)
2.	Used [Voting Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html) from SciKitLearn
	>	Output
	>	![OP_2.0.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_2.0.png)
	-	Made use of [Cross Validation](https://scikit-learn.org/stable/modules/cross_validation.html) i.e. cross_val_score() and [Model Evaluation Parameters](https://scikit-learn.org/stable/modules/model_evaluation.html)
	-	To compare any parameter of these classifiers, just change the scoring parameter in cross_val_score function @ Line 120
		>	![ScoringParameter.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/ScoringParameter.png)
3.	ARBC Implementation referred from [Big Data - Ruchi09](https://github.com/ruchi09/Big-data)
	-	Step 1 : [Transform data](https://github.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/blob/master/MidSem_Lab_Exam/Transform_Data.py) so that similar value notaions in different attributes are considered as different, else the rule generation is affected
	-	Step 2 : [Selecting K Best attributes](https://github.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/blob/master/MidSem_Lab_Exam/K_Best_and_Apriori.py) as 22 attributes will cause overfitting for the classifier
	-	Step 3 : [Run ARBC](https://github.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/blob/master/MidSem_Lab_Exam/3.0_Association_Rule_Based_Classifier.py) to find rules and their supports and confidence
		-	Step 3.1 : Find the Rule with minimum error and then use it to find the class.
	>	Output
	>	![OP_3.0.1.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_3.0.1.png)
	>	![OP_3.0.2.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_3.0.2.png)
4.	Comparing ARBC with Random Forest Classifier
	-	Step 1 : Run ARBC and find the misclassified points
	-	Step 2 : Run Random Forest Classifier and see the number of misclassified points.
	>	![OP_4.0.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/MidSem_Lab_Exam/Output_Screenshots/OP_4.0.png)
	-	Step 3 : Compare the error rate
	```
		Error rate in ARBC : (3700 / 8124) * 100 = 45.54
		Error rate in RFC : (3624 / 5124) * 100 = 70.73
	```
	-	As we can see above the error rate for ARBC is less implying more accuracy. But the time taken for the algorithm to run is high, and the scans happening over the transaction set is very higher that the RFC.