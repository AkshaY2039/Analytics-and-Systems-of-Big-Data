#	Analytics-and-Systems-of-Big-Data
Analytics and Systems of Big Data Lab Work
-	Course Code : COM406P
-	Course Faculty : Dr. Sivaselvan B

Batch No : 08
-	Viraj Sonatkar	(CED15I015)
-	Gowtham Munukutla (CED15I019)
-	Akshay Kumar	(CED15I031)
-- --

##	Practice Set 01
1.	Use Python / R library for
	*	Apriori (ARM) : *by testing it for atleast 5 measures of pattern evaluation / interestingness other than Support and Confidence*
		*	[Selecting the right interestingness measure for association patterns](https://dl.acm.org/citation.cfm?id=775053)
		*	Lift
		*	Conviction
		*	Leverage
		*	Collective Strength
		*	Added Value
	*	Bayes or Decision Tree (Classifier) : *All measures of classifier accuracy*
		*	F1 Score
		*	Specificity
		*	Sensitivity
		*	Recall
		*	Precision
		*	AUC (Area Under Curve)
	*	K-Means (Clustering) : *atleast 3 parameters of cluster quality*
		*	Radius
		*	Clustering
		*	Parity of Clusters
2.	Explore all FIM (Frequent Itemset Mining) library support in Python / R : *Atleast 5 algorithms other than Apriori*
3.	Implement DIC (Dynamic Itemset Counting) in Python / R
4.	Implement efficient version of K-Means / Hierarchical (Dendrogram)
	*	*Clue : Min Heap data structure*
5.	Implement any one ARBC (Association Rule Based Classifiers) algorithm
	*	E.g. CMAR
	*	[Classification Based on Association Rules Algorithm](https://rdrr.io/cran/arulesCBA/man/CBA.html)
	*	[Rules-based Software for Classification](https://www.kdnuggets.com/software/classification-rules.html)
6.	Explore all information evaluation measures of Decision Tree *(atleast 3)*
	*	Shanon's Entropy Theorem (Information Gain)
7.	Explore data preprocessing support in Python / R *(atleast 5)*
	*	[Data Preprocessing Techniques for Data Mining - IASRI](http://iasri.res.in/ebook/win_school_aa/notes/Data_Preprocessing.pdf)
	*	Data Smoothing
	*	Data Binning
8.	Explore Python / R library support for ECLAT (Equivalence CLAss Transformation)
-- --

##	Practice Set 02
1.	Try out all efficient variants of Apriori
	*	Hashing
	*	Transaction Reduction
	*	Partitioning
2.	Implement A-Close as well as Pincer Search. Look at 2 more algorithms for same and implement them. (Or use library if found) E.g. CHARM & MAFIA.
3.	Test [DEAP](https://deap.readthedocs.io/en/master/) package in python
-- --

##	Practice Set 03
1.	Implement a variant of the Decision Tree Classification algorithm which uses Simple Genetic Algorithm to prioritize the selection of paths to generate class label. You may redirect the tree output of a built in Decision Tree classifier as if then rules and then perform GA operation using an appropriate fitness measure.
2.	Test Drive the Problem in 1 using  bucket brigade strategy of fitness apportionment.
3.	Test Drive the BPN classification algorithm for a large data set of your choice (use of built in support / user defined functions is fine).
4.	Test Drive the other variants of Neural Network classifiers supported in Python / R  and analyse the results in comparsion to (3).
-- --

##	Dataset Source
-	[Kaggle](https://www.kaggle.com/)
-	Random Generated Dataset
-- --

##	Other References
-	[ml-algorithms-on-scikit-and-keras](https://github.com/sourcecode369/ml-algorithms-on-scikit-and-keras)