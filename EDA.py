#importing the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
#Load the Dataset
data=pd.read_csv("website_Traffic_Analysis_0.csv")
print(data)
#understanding the DataSet
print("priting top 5 records in the dataset:")
print(data.head)
print("printing the last 5 records of the dataset:")
print(data.tail(5))
print("Dataset Infromation:")
print(data.info())
print("Data Type:")
print(type(data))
print("Column Names:")
print(data.columns)
#Data Quality Check
print("Identifying missing values:")
print(data.isnull().sum())
print("Identifying duplicated values:")
print(data.duplicated().sum())
print("Identifing unique values:")
print(data.nunique)
# Handling Missing Values
data["Exit_Page"]=data["Exit_Page"].fillna("Contact")
print(data)
#Describing the Dataset
print("Data Description:")
print(data.describe())
#Changing the consistent Dataset
df=data
print(df)
print(df.to_csv("Consistent_dataset_1.csv"))
print(os.getcwd())
#Univariate Analysis
sns.boxplot(data["Revenue"],color='yellow',orient='h')
plt.title("Boxplot for Univariate Analysis")
plt.savefig("Boxplot for Revenue")
plt.show()
#BiVariate Analysis
sns.barplot(x="Traffic_Source",y="Revenue",color='green',data=df)
plt.title("Revenue over Traffic Source")
plt.savefig("Revenue over Traffic Source")
plt.show()
#Correlation Analysis
print("Correlation Analysis:")
print(df["Pages_Visited"].corr(df["Revenue"]))
# BUSINESS INSIGHTS

"""
1.Traffic sources contribute differently to revenue generation. The bar chart indicates that some 
traffic sources generate slightly higher average revenue than others, suggesting that marketing
efforts can be focused on the better-performing channels.
2.area with oReferral traffic generates comparatively lower revenue. Compther traffic sources in
 your synthetic dataset, referral traffic contributes less revenue, indicating an opportunity to 
 improve referral campaigns.
3.Revenue distribution is consistent. The univariate analysis of revenue shows no unusual 
distribution or significant outliers, indicating that revenue values are fairly stable in 
the generated dataset.
4.Pages visited have no significant relationship with revenue. The correlation coefficient 
of -0.0013 indicates an almost negligible relationship between the number of pages visited 
and revenue. Simply visiting more pages does not necessarily result in higher revenue.
5.Other business factors may influence revenue more than user engagement. Since pages
 visited show almost no correlation with revenue, variables such as Traffic Source, Conversion
 Status, Device Type, or Visitor Type are likely to have a greater influence on revenue.
6.The dataset is suitable for further business analysis. The cleaned and consistent dataset
 provides a reliable foundation for performing SQL-based business queries and creating 
 interactive Power BI dashboards.
"""