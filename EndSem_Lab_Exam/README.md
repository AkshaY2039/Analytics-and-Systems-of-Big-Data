#	End Sem Lab Exam - Report
-	Date : 16 April 2019
-	CED15I031

##	Problem Statement
-	For the [Health Indicator ONE](./HealthIndicatorONE.csv) dataset
1.	Generate descriptive statistics for any three attributes with the dependent attribute using python support.
2.	Handle missing values using three different techniques
3.	Predict any three gender ratios mortality rates based on task relevant attributes fitting a regression model.
4.	Establish associations between urban and rural mortality attributes, etc with the dependent attributes.
5.	Develop a parallelized version of the Hash based variant of the Apriori algorithm using Map Reduce framework for frequent itemset mining.

##	Solution
1.	Descriptive Statistics using PANDAS
	-	basic statistics using [dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html) from pandas
	-	plots form the [visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html) support of pandas
	-	Output :
		>	![OP_1.0.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.0.png)
		>	![OP_1.1.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.1.png)
		>	![OP_1.2.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.2.png)
		>	![OP_1.3.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.3.png)
		>	![OP_1.4.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.4.png)
		>	![OP_1.5.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.5.png)
		>	![OP_1.6.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.6.png)
		>	![OP_1.7.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.7.png)
		>	![OP_1.8.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.8.png)
		>	![OP_1.9.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.9.png)
		>	![OP_1.10.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_1.10.png)
2.	Handling Missing Data
	-	Using PANDAS - [Working with missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)
	-	Using SkLearn - [Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html)
	-	The techniques of handling missing values are :
		*	Remove Rows With Missing Values
		>	![OP_2.1.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_2.1.png)
		*	Fill NA Forward or Backward
		>	![OP_2.2.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_2.2.png)
		*	Imputing mean with help of SkLearn
		>	![OP_2.3.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_2.3.png)
3.	Regression using SciKitLearn
	-	[Generalized Linear Models](https://scikit-learn.org/stable/modules/linear_model.html#generalized-linear-models)	
	-	[Polynomial Features Preprocessing](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
	-	[Ridge Regression using polynomial Attributes](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)
	-	Output :
		>	![OP_3.1.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_3.1.png)
4.	Association Rule for Urban and Rural Mortality Rate
	-	Reading data and transforming it into categorical data
		-	L --> Low Mortality Rate (0-30)
		-	M --> Moderate Mortality Rate (30-50)
		-	H --> High Mortality Rate (50 above)
	-	To avoid the consideration of different data points of different columns as same, column number is being added to the transformed data
	-	[Using Transaction Encoder](http://rasbt.github.io/mlxtend/user_guide/preprocessing/TransactionEncoder/), the transactions are encoded and the [Using MlXtend Apriori](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/) rules are generated with support of 50% and above.
	-	Output :
		>	![OP_4.1.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_4.1.png)
		>	![OP_4.2.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_4.2.png)
5.	Parallelized version of the Hash based variant of the Apriori algorithm using Map Reduce framework for frequent itemset mining
	-	Using Spark Framework - PySpark
	-	Dataset used is smoking hours dataset as the implementation is only for integer type data
	-	Dividing the dataset into partitions for parallelizing and Hashing
		>	![OP_5.1.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_5.1.png)
		>	![OP_5.2.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_5.2.png)
	-	Hashing the frequent itemsets
		```
		def nextFrequent_hash (itemsets,i1):
			global minSupport
			bucket_size = 17
			hashtable = [ [] for _ in range (0,bucket_size) ]
			frequent = list ()
			for i in itemsets:
				for j in range (0, len (str (i))-1):
					for k in range (j+1,len (i)):
						hash = (i[j]*10 + i[k])%bucket_size
						hashtable[hash].append ( (i[j],i[k]))
			print ("\n\n Hash Table:\n")
			for i in range (0,bucket_size):
				x = Counter (hashtable[i])
				print (x)
				for a in x.keys ():
					if x[a]>=minSupport:
						frequent.append (a)
			return frequent
		```