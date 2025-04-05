from statistics import median
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
from sklearn import metrics
from sklearn import neighbors
from sklearn.model_selection import train_test_split
import sklearn as sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

df = pd.read_csv('SDG_goal3_clean.csv')

input_variable = df[['Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX',
                    'Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX', 
                    "Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX"]]        
print(input_variable)

target_variable = df["Universal health coverage (UHC) service coverage index"]
print(target_variable)

both_variable = df[['Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX',
                    'Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX', 
                    "Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX", 
                    "Universal health coverage (UHC) service coverage index"]]

#choose some part(20%)
test_data = both_variable[0:33]
predict_data = both_variable.drop(index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32])

target = predict_data["Universal health coverage (UHC) service coverage index"]
input = predict_data[['Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX','Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX',"Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX"]]

test_target = test_data["Universal health coverage (UHC) service coverage index"]
test_input = test_data[['Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX','Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX',"Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX"]]

x_train,x_test,y_train,y_test = train_test_split(input, target, test_size=0.3)

k_neighbor = neighbors.KNeighborsRegressor(n_neighbors=4,algorithm='auto').fit(x_train, y_train)

predict_result1 = k_neighbor.predict(test_input)
predict_result2 = k_neighbor.predict(x_test)
predict_result3 = k_neighbor.predict(x_train)

label = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
df_result = pd.DataFrame(predict_result1, index=label)
print('Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX: ',test_input['Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX'])
print("----------")
print('Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX: ',test_input['Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX'])
print("----------")
print("Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX: ",test_input["Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX"])
print("----------")
print('Predicted number of Universal health coverage (UHC) service coverage index: ', df_result)
print("----------")

score = k_neighbor.score(x_test,y_test)
print("Accuracy: ",score)

mean_squared_error_for_predict1 = mean_squared_error(test_target, predict_result1)
mean_squared_error_for_predict2 = mean_squared_error(y_test, predict_result2)
mean_squared_error_for_predict3 = mean_squared_error(y_train, predict_result3)
root_mean1 = sqrt(mean_squared_error_for_predict1) 
root_mean2 = sqrt(mean_squared_error_for_predict2) 
root_mean3 = sqrt(mean_squared_error_for_predict3) 
print('Root mean squared error for predict1: ', sqrt(root_mean1))
print('Root mean squared error for predict2: ', sqrt(root_mean2))
print('Root mean squared error for predict3: ', sqrt(root_mean3))

r_squared_score1 = r2_score(test_target, predict_result1)
r_squared_score2 = r2_score(y_test, predict_result2)
r_squared_score3 = r2_score(y_train, predict_result3)
print('R-squared score1: ', r_squared_score1)
print('R-squared score2: ', r_squared_score2)
print('R-squared score3: ', r_squared_score3)




