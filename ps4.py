import pandas as pd 
import numpy as np 
import statsmodels.apy as sm 

mort_data = pd.read_csv('/Users/Apple/Desktop/major courses/econ 387/ps4data/state_data/mortality_data.csv')
mort_data.rename(index = {"mx": "mort_rate",
                         "qx" : "prob_death",
                        "ax": "ave_length_surv",
                         "lx": "num_of_surv",
                         "dx": "num_of_deaths",
                         "Lx": "num_years_lived",
                         "Tx": "num_years_left",
                         "ex": "life_expec"},
                            inplace = True)

string_text = "-"
mort_data['Age2'] = mort_data.apply(lambda x: sum(i in string_text for i in x.split()))

mort_data['age_group'] = pd.cut(x=df['age_group'], age_group=["<18","18-64", ">64"])
mort_data.drop('Age', 'Age2')
mort_data = mort_data['state','year', 'age_group','7 mortality variables']

for i in range (4,11):
    summation += mort_data(axis=i)
summation

inc_data = pd.read_csv('/Users/Apple/Desktop/major courses/econ 387/ps4data/state_data/income_data.csv')
inc_data = pd.wide_to_long(inc_data,["B", "Z"], sep='.')
inc_data.drop('pinch.2015')
inc_data.sort_values(by=['state','year'], ascending = False)

educ_0715 = pd.read_csv('/Users/Apple/Desktop/major courses/econ 387/ps4data/state_data/education_0715.csv')
educ_data = pd.inc_data.append(educ0715)
educ_data.append('/Users/Apple/Desktop/major courses/econ 387/ps4data/state_data/education')
educ_data.rename(index = { "percent_college": "phs",
                            "percent_highschool": "pcoll"},
                            inplace=True)

expend = pd.read_csv('/Users/Apple/Desktop/major courses/econ 387/ps4data/state_data/expenditure')
expnd_data = educ_data.append(expend)

merge = [inc_data, educ_data]
data = pd.concat(merge)

merge2 = [data, expnd_data]
data = pd.concat(merge2)

merge3 = [mort_data, data]
data = pd.concat(merge3)

data.drop('mort_data', 'inc_data', 'educ_data', 'expnd_data')

data['pinc'] */(1**4)
data['tot_revenue'] */(1**4)
data['taxes'] */(1**4)
data['tot_expnd'] */(1**4)
data['education'] */(1**4)
data['public_welfare'] */(1**4)
data['hospital'] */(1**4)
data['health'] */(1**4)

data['phs'] */(100)
data['pcoll'] */(100)

data.describe(percentiles = [0,1], #not sure what to put here)

#regression problem 18

#regression problem 19

