import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv('./Data/PSCompPars_2021.07.17_19.39.08.csv', sep=',')
# Select and classify the variables considered due to the correlation study.
var_df = df[['sy_snum', 'sy_pnum', 'st_teff', 'st_rad', 'st_mass', 'st_met', 'st_age', 'st_dens', 'st_radv', 'st_logg']]

true_df = var_df.dropna()

x = true_df[['st_teff', 'st_rad', 'st_mass', 'st_met', 'st_age', 'st_dens', 'st_radv', 'st_logg']]
y = true_df[['sy_pnum']]


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

planet_predictor = DecisionTreeClassifier(criterion="entropy", max_depth = 100)
 
X_trainset, X_testset, y_trainset, y_testset = train_test_split(x, y, test_size=0.2, random_state=3)

planet_predictor.fit(X_trainset, y_trainset)

joblib.dump(planet_predictor, 'exoplanet_predictor.joblib')

predTree = planet_predictor.predict(X_testset)

from sklearn import metrics
import matplotlib.pyplot as plt

print("Precisión de los Arboles de Decisión: ", metrics.accuracy_score(y_testset, predTree))

from sklearn import tree

tree.export_graphviz(planet_predictor, out_file='exoplanet-predictor.dot', feature_names=['st_teff', 'st_rad', 'st_mass', 'st_met', 'st_age', 'st_dens', 'st_radv', 'st_logg'], class_names=['1', '2', '3', '4', '5', '6', '7', '8'], label='all', rounded=True, filled=True, leaves_parallel=True)
