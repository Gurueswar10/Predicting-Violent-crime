#!/usr/bin/env python
# coding: utf-8

# # Predicting Violent Crime

# ### Data Set Information:
# 
# Many variables are included so that algorithms that select or learn weights for 
# attributes could be tested. However, clearly unrelated attributes were not included; 
# attributes were picked if there was any plausible connection to crime (N=122), plus 
# the attribute to be predicted (Per Capita Violent Crimes). The variables included in 
# the dataset involve the community, such as the percent of the population considered 
# urban, and the median family income, and involving law enforcement, such as per capita 
# number of police officers, and percent of officers assigned to drug units.
# 
# The per capita violent crimes variable was calculated using population and the sum of 
# crime variables considered violent crimes in the United States: murder, rape, robbery, 
# and assault. There was apparently some controversy in some states concerning the 
# counting of rapes. These resulted in missing values for rape, which resulted in 
# incorrect values for per capita violent crime. These cities are not included in the 
# dataset. Many of these omitted communities were from the midwestern USA.
# 
# Data is described below based on original values. All numeric data was normalized into 
# the decimal range 0.00-1.00 using an Unsupervised, equal-interval binning method. 
# Attributes retain their distribution and skew (hence for example the population 
# attribute has a mean value of 0.06 because most communities are small). E.g. An 
# attribute described as 'mean people per household' is actually the normalized (0-1) 
# version of that value.
# 
# The normalization preserves rough ratios of values WITHIN an attribute (e.g. double 
# the value for double the population within the available precision - except for 
# extreme values (all values more than 3 SD above the mean are normalized to 1.00; all 
# values more than 3 SD below the mean are nromalized to 0.00)).
# 
# However, the normalization does not preserve relationships between values BETWEEN 
# attributes (e.g. it would not be meaningful to compare the value for whitePerCap with 
# the value for blackPerCap for a community)
# 
# A limitation was that the LEMAS survey was of the police departments with at least 100 
# officers, plus a random sample of smaller departments. For our purposes, communities 
# not found in both census and crime datasets were omitted. Many communities are missing 
# LEMAS data.

# ### Features description
# 
# - state: US state (by number) - not counted as predictive above, but if considered, should be consided nominal (nominal) 
# - county: numeric code for county - not predictive, and many missing values (numeric) 
# - community: numeric code for community - not predictive and many missing values (numeric) 
# - communityname: community name - not predictive - for information only (string) 
# - fold: fold number for non-random 10 fold cross validation, potentially useful for debugging, paired tests - not predictive (numeric) 
# - population: population for community: (numeric - decimal) 
# - householdsize: mean people per household (numeric - decimal) 
# - racepctblack: percentage of population that is african american (numeric - decimal) 
# - racePctWhite: percentage of population that is caucasian (numeric - decimal) 
# - racePctAsian: percentage of population that is of asian heritage (numeric - decimal) 
# - racePctHisp: percentage of population that is of hispanic heritage (numeric - decimal) 
# - agePct12t21: percentage of population that is 12-21 in age (numeric - decimal) 
# - agePct12t29: percentage of population that is 12-29 in age (numeric - decimal) 
# - agePct16t24: percentage of population that is 16-24 in age (numeric - decimal) 
# - agePct65up: percentage of population that is 65 and over in age (numeric - decimal) 
# - numbUrban: number of people living in areas classified as urban (numeric - decimal) 
# - pctUrban: percentage of people living in areas classified as urban (numeric - decimal) 
# - medIncome: median household income (numeric - decimal) 
# - pctWWage: percentage of households with wage or salary income in 1989 (numeric - decimal) 
# - pctWFarmSelf: percentage of households with farm or self employment income in 1989 (numeric - decimal) 
# - pctWInvInc: percentage of households with investment / rent income in 1989 (numeric - decimal) 
# - pctWSocSec: percentage of households with social security income in 1989 (numeric - decimal) 
# - pctWPubAsst: percentage of households with public assistance income in 1989 (numeric - decimal) 
# - pctWRetire: percentage of households with retirement income in 1989 (numeric - decimal) 
# - medFamInc: median family income (differs from household income for non-family households) (numeric - decimal) 
# - perCapInc: per capita income (numeric - decimal) 
# - whitePerCap: per capita income for caucasians (numeric - decimal) 
# - blackPerCap: per capita income for african americans (numeric - decimal) 
# - indianPerCap: per capita income for native americans (numeric - decimal) 
# - AsianPerCap: per capita income for people with asian heritage (numeric - decimal) 
# - OtherPerCap: per capita income for people with 'other' heritage (numeric - decimal) 
# - HispPerCap: per capita income for people with hispanic heritage (numeric - decimal) 
# - NumUnderPov: number of people under the poverty level (numeric - decimal) 
# - PctPopUnderPov: percentage of people under the poverty level (numeric - decimal) 
# - PctLess9thGrade: percentage of people 25 and over with less than a 9th grade education (numeric - decimal) 
# - PctNotHSGrad: percentage of people 25 and over that are not high school graduates (numeric - decimal) 
# - PctBSorMore: percentage of people 25 and over with a bachelors degree or higher education (numeric - decimal) 
# - PctUnemployed: percentage of people 16 and over, in the labor force, and unemployed (numeric - decimal) 
# - PctEmploy: percentage of people 16 and over who are employed (numeric - decimal) 
# - PctEmplManu: percentage of people 16 and over who are employed in manufacturing (numeric - decimal) 
# - PctEmplProfServ: percentage of people 16 and over who are employed in professional services (numeric - decimal) 
# - PctOccupManu: percentage of people 16 and over who are employed in manufacturing (numeric - decimal) ######## 
# - PctOccupMgmtProf: percentage of people 16 and over who are employed in management or professional occupations (numeric - decimal) 
# - MalePctDivorce: percentage of males who are divorced (numeric - decimal) 
# - MalePctNevMarr: percentage of males who have never married (numeric - decimal) 
# - FemalePctDiv: percentage of females who are divorced (numeric - decimal) 
# - TotalPctDiv: percentage of population who are divorced (numeric - decimal) 
# - PersPerFam: mean number of people per family (numeric - decimal) 
# - PctFam2Par: percentage of families (with kids) that are headed by two parents (numeric - decimal) 
# - PctKids2Par: percentage of kids in family housing with two parents (numeric - decimal) 
# - PctYoungKids2Par: percent of kids 4 and under in two parent households (numeric - decimal) 
# - PctTeen2Par: percent of kids age 12-17 in two parent households (numeric - decimal) 
# - PctWorkMomYoungKids: percentage of moms of kids 6 and under in labor force (numeric - decimal) 
# - PctWorkMom: percentage of moms of kids under 18 in labor force (numeric - decimal) 
# - NumIlleg: number of kids born to never married (numeric - decimal) 
#  PctIlleg: percentage of kids born to never married (numeric - decimal) 
# - NumImmig: total number of people known to be foreign born (numeric - decimal) 
# - PctImmigRecent: percentage of _immigrants_ who immigated within last 3 years (numeric - decimal) 
# - PctImmigRec5: percentage of _immigrants_ who immigated within last 5 years (numeric - decimal) 
# - PctImmigRec8: percentage of _immigrants_ who immigated within last 8 years (numeric - decimal) 
# - PctImmigRec10: percentage of _immigrants_ who immigated within last 10 years (numeric - decimal) 
# - PctRecentImmig: percent of _population_ who have immigrated within the last 3 years (numeric - decimal) 
# - PctRecImmig5: percent of _population_ who have immigrated within the last 5 years (numeric - decimal) 
# - PctRecImmig8: percent of _population_ who have immigrated within the last 8 years (numeric - decimal) 
# - PctRecImmig10: percent of _population_ who have immigrated within the last 10 years (numeric - decimal) 
# - PctSpeakEnglOnly: percent of people who speak only English (numeric - decimal) 
# - PctNotSpeakEnglWell: percent of people who do not speak English well (numeric - decimal) 
# - PctLargHouseFam: percent of family households that are large (6 or more) (numeric - decimal) 
# - PctLargHouseOccup: percent of all occupied households that are large (6 or more people) (numeric - decimal) 
# - PersPerOccupHous: mean persons per household (numeric - decimal) 
# - PersPerOwnOccHous: mean persons per owner occupied household (numeric - decimal) 
# - PersPerRentOccHous: mean persons per rental household (numeric - decimal) 
# - PctPersOwnOccup: percent of people in owner occupied households (numeric - decimal) 
# - PctPersDenseHous: percent of persons in dense housing (more than 1 person per room) (numeric - decimal) 
# - PctHousLess3BR: percent of housing units with less than 3 bedrooms (numeric - decimal) 
# - MedNumBR: median number of bedrooms (numeric - decimal) 
# - HousVacant: number of vacant households (numeric - decimal) 
# - PctHousOccup: percent of housing occupied (numeric - decimal) 
# - PctHousOwnOcc: percent of households owner occupied (numeric - decimal) 
# - PctVacantBoarded: percent of vacant housing that is boarded up (numeric - decimal) 
# - PctVacMore6Mos: percent of vacant housing that has been vacant more than 6 months (numeric - decimal) 
# - MedYrHousBuilt: median year housing units built (numeric - decimal) 
# - PctHousNoPhone: percent of occupied housing units without phone (in 1990, this was rare!) (numeric - decimal) 
# - PctWOFullPlumb: percent of housing without complete plumbing facilities (numeric - decimal) 
# - OwnOccLowQuart: owner occupied housing - lower quartile value (numeric - decimal) 
# - OwnOccMedVal: owner occupied housing - median value (numeric - decimal) 
# - OwnOccHiQuart: owner occupied housing - upper quartile value (numeric - decimal) 
# - RentLowQ: rental housing - lower quartile rent (numeric - decimal) 
# - RentMedian: rental housing - median rent (Census variable H32B from file STF1A) (numeric - decimal) 
# - RentHighQ: rental housing - upper quartile rent (numeric - decimal) 
# - MedRent: median gross rent (Census variable H43A from file STF3A - includes utilities) (numeric - decimal) 
# - MedRentPctHousInc: median gross rent as a percentage of household income (numeric - decimal) 
# - MedOwnCostPctInc: median owners cost as a percentage of household income - for owners with a mortgage (numeric - decimal) 
# - MedOwnCostPctIncNoMtg: median owners cost as a percentage of household income - for owners without a mortgage (numeric - decimal) 
# - NumInShelters: number of people in homeless shelters (numeric - decimal) 
# - NumStreet: number of homeless people counted in the street (numeric - decimal) 
# - PctForeignBorn: percent of people foreign born (numeric - decimal) 
# - PctBornSameState: percent of people born in the same state as currently living (numeric - decimal) 
# - PctSameHouse85: percent of people living in the same house as in 1985 (5 years before) (numeric - decimal) 
# - PctSameCity85: percent of people living in the same city as in 1985 (5 years before) (numeric - decimal) 
# - PctSameState85: percent of people living in the same state as in 1985 (5 years before) (numeric - decimal) 
# - LemasSwornFT: number of sworn full time police officers (numeric - decimal) 
# - LemasSwFTPerPop: sworn full time police officers per 100K population (numeric - decimal) 
# - LemasSwFTFieldOps: number of sworn full time police officers in field operations (on the street as opposed to administrative etc) (numeric - decimal) 
# - LemasSwFTFieldPerPop: sworn full time police officers in field operations (on the street as opposed to administrative etc) per 100K population (numeric - decimal) 
# - LemasTotalReq: total requests for police (numeric - decimal) 
# - LemasTotReqPerPop: total requests for police per 100K popuation (numeric - decimal) 
# - PolicReqPerOffic: total requests for police per police officer (numeric - decimal) 
# - PolicPerPop: police officers per 100K population (numeric - decimal) 
# - RacialMatchCommPol: a measure of the racial match between the community and the police force. High values indicate proportions in community and police force are similar (numeric - decimal) 
# - PctPolicWhite: percent of police that are caucasian (numeric - decimal) 
# - PctPolicBlack: percent of police that are african american (numeric - decimal) 
# - PctPolicHisp: percent of police that are hispanic (numeric - decimal) 
# - PctPolicAsian: percent of police that are asian (numeric - decimal) 
# - PctPolicMinor: percent of police that are minority of any kind (numeric - decimal) 
# - OfficAssgnDrugUnits: number of officers assigned to special drug units (numeric - decimal) 
# - NumKindsDrugsSeiz: number of different kinds of drugs seized (numeric - decimal) 
# - PolicAveOTWorked: police average overtime worked (numeric - decimal) 
# - LandArea: land area in square miles (numeric - decimal) 
# - PopDens: population density in persons per square mile (numeric - decimal) 
# - PctUsePubTrans: percent of people using public transit for commuting (numeric - decimal) 
# - PolicCars: number of police cars (numeric - decimal) 
# - PolicOperBudg: police operating budget (numeric - decimal) 
# - LemasPctPolicOnPatr: percent of sworn full time police officers on patrol (numeric - decimal) 
# - LemasGangUnitDeploy: gang unit deployed (numeric - decimal - but really ordinal - 0 means NO, 1 means YES, 0.5 means Part Time) 
# - LemasPctOfficDrugUn: percent of officers assigned to drug units (numeric - decimal) 
# - PolicBudgPerPop: police operating budget per population (numeric - decimal) 
# - ViolentCrimesPerPop: total number of violent crimes per 100K popuation (numeric - decimal) GOAL attribute (to be predicted) 

# In[23]:


# Importing useful libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# ## 0. Data Preparation

# In[24]:


# importing useful objects
#from crime_dataset_headers import *.
# importing data
#data_url= 'C:\Users\LIBITHARAN\Desktop\jupyter\communities.csv'
crime = pd.read_csv(r"S:\project\communities.csv")


# In[25]:


crime


# In[26]:


crime.head()


# In[27]:


# Deleting non predictive columns
#non_predictive = ['county', 'community', 'fold']
#crime.drop(non_predictive, axis=1, inplace=True)
# Imputing one missing value
#crime.loc['Natchezcity','OtherPerCap'] = crime['OtherPerCap'].mean()
# Deleting columns with majority of missing values
missing_values_per_col = crime.isnull().sum()
cols_to_remove = missing_values_per_col[missing_values_per_col > 0].index
#crime.drop(cols_to_remove, axis=1, inplace=True)


# In[28]:


# Features with the highest correlation with the target
top_corr_features = crime.corr().loc['ViolentCrimesPerPop'].apply(np.abs).sort_values(ascending=False).index[1:12]
top_corr_features = list(top_corr_features)
top_corr_features


# ### Getting the train and test sets

# In[29]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score


# In[30]:


target_name = 'ViolentCrimesPerPop'
X = crime[top_corr_features]
y = crime[target_name]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)


# In[31]:


models = pd.DataFrame(index=['top10_featues_mse', 'full_model_mse'], 
                      columns=['NULL', 'MLR', 'KNN', 'LASSO'])


# # Making predictions with just a few features (top 10)

# ## The Null model: always predict the average of the target

# In[32]:


y_pred_null = y_train.mean()
models.loc['top10_featues_mse','NULL'] = mean_squared_error(y_pred=np.repeat(y_pred_null, y_test.size), 
                                                   y_true=y_test)


# ## A. Multiple Linear Regression

# In[33]:


# 1. Import the estimator object (model)
from sklearn.linear_model import LinearRegression
# 2. Create an instance of the estimator
linear_regression = LinearRegression()
# 3. Use the trainning data to train the estimator
linear_regression.fit(X_train, y_train)
# 4. Evaluate the model
models.loc['top10_featues_mse','MLR'] = mean_squared_error(y_pred=linear_regression.predict(X_test), 
                                                   y_true=y_test)


# ## B. K-Nearest Neighbor Model

# In[34]:


# 1. Import the estimator object (model)
from sklearn.neighbors import KNeighborsRegressor
# 2. Create an instance of the estimator
knn = KNeighborsRegressor(n_neighbors=10, weights='distance', metric='euclidean')
# 3. Use the trainning data to train the estimator
knn.fit(X_train, y_train)
# 4. Evaluate the model
models.loc['top10_featues_mse','KNN'] = mean_squared_error(y_pred=knn.predict(X_test), 
                                                   y_true=y_test)


# ## C. Lasso

# In[35]:


# 1. Import the estimator object (model)
from sklearn.linear_model import Lasso
# 2. Create an instance of the estimator
lasso = Lasso(alpha=0.0001)
# 3. Use the trainning data to train the estimator
lasso.fit(X_train, y_train)
# 4. Evaluate the model
models.loc['top10_featues_mse','LASSO'] = mean_squared_error(y_pred=lasso.predict(X_test), 
                                                   y_true=y_test)


# In[36]:


models


# In[37]:


fig, ax = plt.subplots(figsize=(8,5))
models.loc['top10_featues_mse'].plot(kind='barh', ax=ax)
ax.set_title('MSE for Regression Models Using top 10 correlated features')
ax.legend(loc=3);


# # Using all the features

# In[38]:


target_name = 'ViolentCrimesPerPop'
X = crime.drop('ViolentCrimesPerPop', axis=1)
y = crime[target_name]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)


# In[ ]:





# In[39]:


X_train


# ### Preparing a DataFrame for model analysis

# In[40]:


X_test


# ## The Null model: always predict the average of the target

# In[41]:


y_train


# In[42]:


y_test


# In[43]:


y_pred_null = y_train.mean()
models.loc['full_model_mse','NULL'] = mean_squared_error(y_pred=np.repeat(y_pred_null, y_test.size), 
                                                   y_true=y_test)


# In[44]:


models


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




