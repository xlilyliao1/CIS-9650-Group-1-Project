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
   

**Linear Regression Analysis:**<br />
1. Model Preparation:
Independent variables are on different scales. 
Need to rescale through normalization.

2. Run multiple regression model:
Assign X and Y -> Run

3. Model Validation:  
Heatmap looking at correlation between variables  
Test for multicollinearity via Variance Inflation Factor (VIF) analysis  

4. Model rerun.   
removing variables with high VIF and strong correlation   
(3 model runs in total)
