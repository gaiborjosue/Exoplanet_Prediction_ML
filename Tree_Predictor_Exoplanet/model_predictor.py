import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy.stats import spearmanr, kendalltau, pearsonr, boxcox
from sklearn.tree import DecisionTreeClassifier
import joblib

planet_predictor = joblib.load('./exoplanet_predictor.joblib')


def Predict_Simple():
    st_teff_input = input("Enter the value of the Stellar Effective Temperature [K]: ")
    st_rad_input = input("Enter the value of the Stellar Radius [Solar Radius]: ")
    st_mass_input = input("Enter the value of the Stellar Mass [Solar mass]: ")
    st_met_input = input("Enter the value of the Stellar Metallicity [dex]: ")
    st_age_input = input("Enter the value of the Stellar Age [Gyr]: ")
    st_dens_input = input("Enter the value of the Stellar Density [g/cm**3]: ")
    st_radv_input = input("Enter the value of the Systemic Radial Velocity [km/s]: ")
    predTree = planet_predictor.predict([[st_teff_input, st_rad_input, st_mass_input, st_met_input, st_age_input, st_dens_input, st_radv_input]])
    return print(predTree)

def Predict_Complex():
    #For the complex predict (Or to predict more than 1 Star Exoplanets) please replace the 'YOUR TESTSET' with the variable assigned for the prediction. Please note that for the variable the headers of your database must contain st_teff  st_rad  st_mass  st_met  st_age  st_dens  st_radv.
    df_location = input('Please enter the path to your .csv dataframe (Include the ".csv"), please note that the headers of your dataframe must be: st_teff  st_rad  st_mass  st_met  st_age  st_dens  st_radv, gathering all the characteristics. (Read the README.md to see the description of each header): ')
    dataframe = pd.read_csv(f'{df_location}')
    var_df = dataframe[['st_teff', 'st_rad', 'st_mass', 'st_met', 'st_age', 'st_dens', 'st_radv']]
    clean_df = var_df.dropna()
    prediction_df = clean_df[['st_teff', 'st_rad', 'st_mass', 'st_met', 'st_age', 'st_dens', 'st_radv']]
    #Predict
    predTree = planet_predictor.predict(prediction_df)
    outfile = open('predictions.txt', 'w')
    outfile.write('This is the output for the prediction. The machine Learning Model has a 76 percent accuracy score. Rights Reserved Edward Gaibor. https://edwardgaibor.me' + '\n')
    for item in predTree:
        outfile.write(str(item) + '\n')
    outfile.close()
    return print('The Predictions were saved to "predictions.txt" file. Each line of the TXT file corresponds to each star given by the dataset.')

first_question = input('Do you want to predict the number of planets for a single star or for many stars(Dataframe)?(Single/Many) ')

if first_question == 'Single':
    Predict_Simple()
    
elif first_question == 'Many':
    Predict_Complex()