# CIS-9650-Group-1-Project Physiochemical Properties and Quality of Wine
#### Shoma Babulal, Alexandra Garofali, Fang Li, Lily Liao, Tiffany Ramkaran, Ziwen Zhang

**Overview**
This repository will allow one to determine which physiochemical properties of wine have the most impact on the quality of white wine and red wine. This analysis is done via regression analysis where quality is the dependent variable, and the different physiochemical properties are the independent variables. Quality values in the datasets are predetermined – not calculated. The physiochemical properties are as follows:  fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol. To understand the definitions of these properties, please review the document "Understanding Wine Attributes and Properties" in this repository. 

Before the regression analysis, the program conducts a multitude of exploratory analyses on the dependent and independent variables. The physicochemical properties and quality are on different scales; therefore, the program normalizes each variable before running the regression analysis. After the regression analysis, this program tests for multicollinearity by looking at Variance Inflation Factor (VIF). Regression analyses are repeated with each run eliminating independent variables with high VIF to allow one to learn more about model validation via VIF.  Due to the nature of wine, where the physiochemical properties work together to create quality wine, the acceptable maximum VIF for each property modeled is 10. 

**Files:**
This project uses two datasets: [one white wine dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv), and [one red wine dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv). The two datasets combine for a total of 6,499 records, which represent a wine and their properties and their qualities. The datasets are saved in this repository. Please download and save in the same folder you will run your code. 


Preview of datasets above: https://archive.ics.uci.edu/ml/datasets/wine+quality <br />

**Tools used:**
Python, Pandas, NumPy, Sklearn, Matplotlib, statsmodels, Seaborn
	
**Instructions to run .py file**
Please perform the following tasks in Python.

1.	Download both datasets in the same folder as .py file 
2.	Import all libraries listed above
3.	Run code 

** Code walk through ** 

1.	Import all libraries above 
2.	Open and read the white wine csv file using pandas. Separate by “;”. The data does not need to be cleaned – all fields are valid. 
3.	Display the number of records in the file 
4.	Exploratory analysis
a.	Min/Max of Quality 
b.	Histogram of Quality 
c.	Boxplots of physiochemical properties 
d.	Interquartile ranges for physiochemical properties at highest quality value
5.	Normalize independent variables (physiochemical properties)
6.	Regression analysis 
a.	X = physiochemical properties 
i.	Y = quality 
7.	Model validation
a.	Correlation analysis using heatmap of independent variables
b.	VIF analysis to test for multicollinearity 
8.	Model Reruns & model validations until VIF for each independent variable has VIF < 10
9.	Repeat Steps 2-8 for red wine dataset

**Exploratory Analysis**
The purpose of the exploratory analysis is to understand the modeled variables in terms of range and distribution. 

Quality Exploratory Analysis 
-	Minimum, maximum, average
-	Histogram 

Physicochemical Properties Exploratory Analysis in relation to Quality
-	Boxplots of each property at each quality score 
-	Interquartile ranges for each quality score
<br />

** Regression Analysis & Model Validation ** 
Regression analysis is a statistical process which allows one to estimate the strength of a relationship between a dependent and independent variable(s). This analysis determines the relationship strength between wine quality and physiochemical properties. All properties were modeled in the first iteration of the model. After testing for VIF, it became evident that there was multicollinearity between variables, as many VIFs were higher than 10. This means that the properties are too correlated with each other, and so when modeled, they behave the same way. Therefore, the model is unable to get an accurate read of the individual impact of each property since the properties are acting in a similar manner. The second run removes variables with high VIF; however, after testing for VIF again, there were still variables with VIFs higher than 10. After removing more variables, the third model ended up with the strongest results, as VIF for each variable was less than 10. Although VIF should usually be under 5, for this analysis we decided 10 would be acceptable, as the physiochemical properties all work together to create quality wine. 


