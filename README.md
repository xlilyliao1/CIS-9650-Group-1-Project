# CIS-9650-Group-1-Project Physiochemical Properties and Quality of Wine
#### Shoma Babulal, Alexandra Garofali, Fang Li, Lily Liao, Tiffany Ramkaran, Ziwen Zhang

**Objective:**
We are trying to determine which physicochemical properties of wine have the most impact on quality. The physiochemical properties in our data set are: fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol. To understand the defintions of these properties, please review the document "Understanding Wine Attributes and Properties" in this repository.

**Files:**
For this project we will use two datasets which total 6499 records, which represent a wine and their properties and their qualities. They are saved in Github but can calso be found using the links below.

-winequality-white.csv 
-winequality-red.csv  

[Wine Quality – Red](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv).<br />
[Wine Quality – Red](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv).<br />
Preview of datasets above: https://archive.ics.uci.edu/ml/datasets/wine+quality <br />

**Tools used:**
Python, Pandas, NumPy, Sklearn, Matplotlib, statsmodels


**Instructions**
Please perform the following tasks in Python.

1. Open and read the csv files using pandas. 
2. Display how many records are in each of the files.
3. The data did not need any cleaning because it did not contain any invalid fields/data.
4. Import the libraries.
5. Exploratory analysis
6. Regression Analysis
7. Box plots
8. Histograms were used to understand where the wine qualities were concentrated. We used quality to plot our histograms.
9. Independent variables are columns (physiochemical properties). dependent is quality

We perform the same analysis for red and white wine.

**Exploratory Analysis:**

We to understand our dependent variable, Quality so we calculated look at min, max and average. Then we also wanted to see the distribution of our data. We created a histogram to visualize where most of our data. Now that we looked at our dependent variable, let's look at our independent variables in relataion to Quantitiy. To do so, we will look at each physiochemical properties quartile ranges for each quality score.  <br />


**Findings:**<br />
The graph shows the most of the wine quality concentrates betwene 5 and 6.
High quality wine has high level of alcohol, citric acid, and sulphates; low level of density and pH.   

**Linear Regression Analysis:**<br />
Based on the linear regression analysis: 
White Wine:
All of the properties have a positive impact on quality, with the exception of volatile acidity. This means that when volatile acidity increases, the quality of White wine diminishes. 
Alcohol and Density have the highest coefficients, meaning they have the highest impact on white wine's quality score. Density is highly correlated to residual sugar, meaning that they move in the same direction. As sugar increases, density will increase, or vice versa.

Red Wine:
Only about 75% of the properties have postitive impact on red wine quality. The properties that have negative impact on Red wine's quality are chlorides, total sulfur dioxide, and volatile acidity. 
Similar to White wine, Alcohol had the highest coefficient, meaning it has the most impact on quality score. pH also has a high coefficient and therefore a high impact on quality. This may be due to the fact that high pH allows Red wine to age faster and have a fuller body.  

**Conclusion:**<br />  
- Rate your wine at home like an expert 
