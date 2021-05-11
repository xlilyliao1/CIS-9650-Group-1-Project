#CIS 9650 Group 1 Project 
# Shoma Babulal, Alexandra Garofali, Fang Li, Lily Liao, Tiffany Ramkaran, Ziwen Zhang

#importing the libraries

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 
import seaborn as sns
import sklearn 
from sklearn.preprocessing import MinMaxScaler
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

## WHITE WINE ## 

# Step 1: Reading file

wData = pd.read_csv("winequality-white.csv", sep=";")

print("There are", len(wData.index), "records in this data set.")

#Step 2
## EXPLORATORY ANALYSIS ## 

#We want to understand our dependent variable, Quality. We will look at min, max and average.
minQuality = wData["quality"].min()
maxQuality = wData["quality"].max()
avgQuality = wData["quality"].mean()

print("\nOur dependent variable is the Quality of White wine. Quality ranges from 1-10, where 1 is the lowest quality and 10 is the highest; however, in our white wine dataset, the quality of white wine ranges from", minQuality, "to", maxQuality, ".\n")
print( "The average quality of white wine in this dataset is ", avgQuality)

#We want to take a look at the distrubution of the quality of white wine in this dataset. 
wData.hist(['quality'])
plt.title('White Wine Quality')
plt.ylabel('Frequency')
plt.xlabel('Quality')

print("The quality of white wine in this data set is concentrated between 5-7. \n")

#Now that we looked at our dependent variable, let's look at our independent variables in reltaion to Quality. To do so, we will look at each physiochemical properties quartile ranges for each quality score.  

fig, ax = plt.subplots(3, 4, figsize=(20, 15))
a = wData.columns.tolist()
for i in range(3):
    for j in range(4):
        wData.boxplot(a[i*4+j], 'quality', ax=ax[i][j])
        if i == 2 and j == 3:
            fig.delaxes(ax[i][j])
fig.suptitle("Boxplot Grouped by White Wine Quality", fontsize=25)
plt.show()
            
# Let's look at the interquartile ranges for each property in high quality white wines 
pr = ["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol" ]
prp = wData[wData["quality"] == 9]
for item in pr:
    q1 = prp[item].quantile(0.25)
    q3 = prp[item].quantile(0.75)       
    IQR = q3 - q1
    print("The", item, "in white wines that have a quality score of 9 has a interquartile range of:", IQR,"\n")

#Step 3
## NORMALIZE THE INDEPENDENT VARIABLES ## 

#Since the properties are on adifferent scales, we need to normalize them before modeling. 
   
scaler = MinMaxScaler()
wDataScaled = pd.DataFrame(scaler.fit_transform(wData),
                      columns = wData.columns, index = wData.index)

# print(wDataScaled)

#Step 4 
## REGRESSION ANALYSIS ##

wDataModel = pd.DataFrame(wDataScaled, columns= ["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"])
X = wDataModel[["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]]
Y = wDataModel["quality"]

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

print("\n According to this output, alcohol has the most impact on the quality of white wine. All properties have a positive impact on quality besides volatile acidity. To validate our model results, we want to look at correlations between the properties and their variance inflation factors (VIF)\n")

mask = np.zeros_like(wDataScaled.corr())
mask[np.triu_indices_from(mask)] = True

sns.set(rc={'figure.figsize': (8.5,8.5)})
sns.heatmap(wData.corr().round(2), square=True, cmap='YlGnBu', annot=True, mask=mask);

print("As we can see, there are high correlations between properties. Therefore; we need to test for multicollinarity by doing a VIF analysis. \n")

## MODEL VALIDATION - TESTING FOR MULTICOLLINARITY 
X = wDataModel[["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]]
vif_data = pd.DataFrame()
vif_data["Physiochemical Property"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
  
print(vif_data)

print("\nMost of our indepedent variables have VIFs higher than 10, meaning they are highly correlated. This makes sense because density is determined by residual sugar and alcohol. Sulphates also mitigate the impact of acidity/pH.")


## DROPPING COLUMNS WITH HIGH VIF - DENSITY & FIXED ACIDITY
print("\nThis is the updated model after dropping Density and Fixed Acidity\n")
wDataModel = pd.DataFrame(wDataScaled, columns= ["total sulfur dioxide", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "pH", "sulphates", "alcohol", "quality"])
X = wDataModel[["total sulfur dioxide", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "pH", "sulphates", "alcohol"]]
Y = wDataModel["quality"]

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

## VIF CHECK 
X = wDataModel[["volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "pH", "sulphates", "alcohol"]]
vif_data = pd.DataFrame()
vif_data["Physiochemical Property"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
  
print(vif_data)

print("After dropping Density and Fixed Acidity, we checked VIF again. Total sulfur dioxide still had a VIF over 10, so we dropped it from our next model run.")
## DROPPING COLUMNS WITH HIGH VIF - TOTAL SULFUR DIOXIDE 

print("\nThis is the updated model after dropping density, fixed acidity and total sulfur dioxide.\n")
wDataModel = pd.DataFrame(wDataScaled, columns= ["volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "pH", "sulphates", "alcohol", "quality"])
X = wDataModel[["volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "pH", "sulphates", "alcohol"]]
Y = wDataModel["quality"]

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

## VIF CHECK 
X = wDataModel[["volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide","pH", "sulphates", "alcohol"]]
vif_data = pd.DataFrame()
vif_data["Physiochemical Property"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]

print(vif_data)
print("\nThe VIFs are all below 10; therefore, we consider our model results conclusive. Alcohol has the most impact on quality of white wine, followed by resuidual sugar.\n")  

#### RED WINE ANALYSIS ####
print("Now that we analyzed white wine, let's look at how red wine compares.\n")
# Step 1: Reading file

rData = pd.read_csv("winequality-red.csv", sep=";")
print("There are", len(rData.index), "records in this data set.\n"  )

#Step 2
## EXPLORATORY ANALYSIS ## 

#We want to understand our dependent variable, Quality. We will look at min, max and average.

minQuality = rData["quality"].min()
maxQuality = rData["quality"].max()
avgQuality = rData["quality"].mean()

print("Our dependent variable in this analysis the quality of red wine. Similar to the White wine dataset, quality ranges from 1-10, where 1 is the lowest quality and 10 is the highest. In our red wine dataset, the quality of ranges from", minQuality, "to", maxQuality,"which is a lower range than in the white wine dataset.\n")
print("The average quality of red wine in this dataset is ", avgQuality)

#We want to take a look at the distrubution of the quality of Red wine in this dataset. 

rData.hist(['quality'])
plt.title('Red Wine Quality')
plt.ylabel('Frequency')
plt.xlabel('Quality')

print("The quality of Red wine is concentrated at 5 and 6. \n")

#Now that we looked at our dependent variable, let's look at our independent variables in reltaion to Quality. To do so, we will look at each physiochemical properties quartile ranges for each quality score.  

fig, ax = plt.subplots(3, 4, figsize=(20, 15))
a = rData.columns.tolist()
for i in range(3):
    for j in range(4):
        rData.boxplot(a[i*4+j], 'quality', ax=ax[i][j])
        if i == 2 and j == 3:
            fig.delaxes(ax[i][j])
fig.suptitle("Boxplot Grouped by Red Wine Quality", fontsize=25)
plt.show()

# Let's look at the interquartile ranges for each property in high quality red wines 

pr = ["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol" ]
prp = rData[rData["quality"] == 8]
for item in pr:
    q1 = prp[item].quantile(0.25)
    q3 = prp[item].quantile(0.75)       
    IQR = q3 - q1
    print("The", item, "in red wines that have a quality score of 8 has a interquartile range of:", IQR,"\n")

#Step 3
## NORMALIZE THE INDEPENDENT VARIABLES ## 

#Since the properties are on adifferent scales, we need to normalize them before modeling. 
      
scaler = MinMaxScaler()
rDataScaled = pd.DataFrame(scaler.fit_transform(rData),
                      columns = rData.columns, index = rData.index)    
    
# print(rDataScaled)

#Step 4 
## REGRESSION ANALYSIS ##

rDataModel = pd.DataFrame(rDataScaled, columns= ["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"])
X = rDataModel[["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]]
Y = rDataModel["quality"]

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

print("\nOnly about 75% of the properties have postitive impact on red wine quality. The properties that have negative impact on Red wine's quality are chlorides, total sulfur dioxide, and volatile acidity. \n")

print("\nSimilar to White wine, Alcohol had the highest coefficient, meaning it has the most impact on quality score. pH also has a high coefficient and therefore a high impact on quality. This may be due to the fact that high pH allows Red wine to age faster and have a fuller body. Similar to our methodology in white wine, we want to test for correlation and VIF amongst the independent variables.\n")

mask = np.zeros_like(rDataScaled.corr())
mask[np.triu_indices_from(mask)] = True

sns.set(rc={'figure.figsize': (8.5,8.5)})
sns.heatmap(rData.corr().round(2), square=True, cmap='YlGnBu', annot=True, mask=mask);
plt.tight_layout() 
plt.show()

## MODEL VALIDATION - TESTING FOR MULTICOLLINARITY 
X = rDataModel[["fixed acidity", "volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]]
vif_data = pd.DataFrame()
vif_data["Physiochemical Property"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
  
print(vif_data)

print("\n Less of our indepedent variables in the red wine dataset have VIFs higher than 10 in comparison to White wine. However, we still need to eliminate those with high VIFs and rerun the model.")


## DROPPING COLUMNS WITH HIGH VIF - FIXED ACIDITY, DENSITY 
print("\nThis is the updated model after Fixed Acidity and Density \n")
rDataModel = pd.DataFrame(rDataScaled, columns= ["volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide","pH", "sulphates", "alcohol", "quality"])
X = rDataModel[["volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide","pH", "sulphates", "alcohol"]]
Y = rDataModel["quality"]

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

## VIF CHECK

X = rDataModel[["volatile acidity","citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide","pH", "sulphates", "alcohol"]]
vif_data = pd.DataFrame()
vif_data["Physiochemical Property"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
  
print(vif_data)
print("Some variables still have high VIFs. pH has a high coefficient; therefore, we do not want to remove it from the model. We removed volatile acidity instead of pH, although pH has a higher VIF.")

## DROPPING COLUMN WITH HIGH VIF - VOLATILE ACIDITY 

print("\nThis is the updated model after fixed acidity, density and volatile acidity \n")
rDataModel = pd.DataFrame(rDataScaled, columns= ["citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide","pH", "sulphates", "alcohol", "quality"])
X = rDataModel[["citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide","pH", "sulphates", "alcohol"]]
Y = rDataModel["quality"]

model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

## VIF CHECK

X = rDataModel[["citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide","pH", "sulphates", "alcohol"]]
vif_data = pd.DataFrame()
vif_data["Physiochemical Property"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
  
print(vif_data)

print("Now that all of the variables have VIFs under 10, we accept these results as conclusive. Sulphates has the most impact on the quality of red wine, followed by alcohol and pH.")

#Step 5
## COMPARISON ##

#For an accurate comparison, we reduced the white records as they are about 3x more than red.

wReduced = wData.sample(frac=0.326)  

rData['wine_type'] = 'red'   
wReduced['wine_type'] = 'white'
# merge red and white wine datasets
wines = pd.concat([rData, wReduced])
cp = sns.countplot(x="quality", hue="wine_type", data=wines,   palette={"red": "#FF9999", "white": "#FFE888"})
cp.set_title("Red vs White Wine Quality (0-10)")