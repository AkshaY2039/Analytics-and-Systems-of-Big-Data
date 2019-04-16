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
	-	[dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
	-	[visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
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
		>	![OP_1.10.png](https://raw.githubusercontent.com/AkshaY2039/Analytics-and-Systems-of-Big-Data/master/EndSem_Lab_Exam/Output_Screenshots/OP_3.1.png)
4.	Association Rule for Urban and Rural Mortality Rate
	-	
	