#	Mid Sem Lab Exam
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
	-	[Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) from SciKit Learn
	-	[Nearest Neighbors Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) from SciKit Learn
	-	[Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) from SciKit Learn
2.	Used [Voting Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html) from SciKitLearn
	-	Made use of [Cross Vhttps://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.htmlalidation](https://scikit-learn.org/stable/modules/cross_validation.html) i.e. cross_val_score() and [Model Evaluation Parameters](https://scikit-learn.org/stable/modules/model_evaluation.html)
	-	To compare any parameter of these classifiers, just change the scoring parameter in cross_val_score function @ Line 120
3.	