import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib
import argparse

parser = argparse.ArgumentParser(description="The Exoplanet Predictor Versión 1.0 - Predict the number of planets of a system based on the stellar characteristics.")

planet_predictor = joblib.load('./exoplanet_predictor.joblib')

parser.add_argument('-t', '--stellareffectivetemp', help='Enter the Stellar Effective Temperature of the Star your analazying.')
parser.add_argument('-r', '--stellarradius', help='Enter the Stellar Radius [Solar Radius].')
parser.add_argument('-m', '--stellarmass', help='Enter the Stellar Mass [Solar mass].')
parser.add_argument('-mt', '--stellarmetallicity', help='Enter the Stellar Metallicity [dex].')
parser.add_argument('-a', '--stellarage', help='Enter the Stellar Age [Gyr].')
parser.add_argument('-d', '--stellardensity', help='Enter the Stellar Density [g/cm**3].')
parser.add_argument('-v', '--stellarradialvelocity', help='Enter the Systemic Radial Velocity [km/s].')
parser.add_argument('-l', '--stellsurfacegravity', help='Enter the Stellar Surface Gravity [log10(cm/s**2)].')

parser.add_argument('-data', '--datafile', help='Enter the path of the database file (In CSV format separated by a comma). See an example of a datafile in the "Data" folder of the repository.')

args = parser.parse_args()

print('''
                      _____                      _                      _    ___  ___ _     
                      |  ___|                    | |                    | |   |  \/  || |    
                      | |__  __  __  ___   _ __  | |  __ _  _ __    ___ | |_  | .  . || |    
                      |  __| \ \/ / / _ \ | '_ \ | | / _` || '_ \  / _ \| __| | |\/| || |    
                      | |___  >  < | (_) || |_) || || (_| || | | ||  __/| |_  | |  | || |____
                      \____/ /_/\_\ \___/ | .__/ |_| \__,_||_| |_| \___| \__| \_|  |_/\_____/
                                          | |                                                
                                          |_|                                                
                                          

                       :
                       :
                       :
                       :
        .              :
         '.            :           .'
           '.          :         .'
             '.   .-""""""-.   .'                                   .'':
               '."          ".'                               .-""""-.'         .---.          .----.        .-"""-.
                :            :                _    _        ."     .' ".    ..."     "...    ."      ".    ."       ".
        .........            .........    o  (_)  (_)  ()   :    .'    :   '..:.......:..'   :        :    :         :   o
                :            :                              :  .'      :       '.....'       '.      .'    '.       .'
                 :          :                             .'.'.      .'                        `''''`        `'''''`
                  '........'                              ''   ``````
                 .'    :   '.
               .'      :     '.
             .'        :       '.
           .'          :         '.
              Edward   :                        Exoplanet Machine Learning Predictor
                       :                        
                       :
                       :


''')

pred_args = []

simple_args = ['stellareffectivetemp', 'stellarradius', 'stellarmass', 'stellarmetallicity', 'stellarage', 'stellardensity', 'stellarradialvelocity', 'stellsurfacegravity']

complex_args = ['datafile']


def Predict_Simple(x):
    predTree = planet_predictor.predict([x])
    return print(f"The number of planets that the system you entered has is: |{predTree[0]}| With 81% accuracy.")

def Predict_Complex():
    #For the complex predict (Or to predict more than 1 Star Exoplanets) please replace the 'YOUR TESTSET' with the variable assigned for the prediction. Please note that for the variable the headers of your database must contain st_teff  st_rad  st_mass  st_met  st_age  st_dens  st_radv.
    dataframe = pd.read_csv(f'{args.datafile}')
    var_df = dataframe[['st_teff', 'st_rad', 'st_mass', 'st_met', 'st_age', 'st_dens', 'st_radv', 'st_logg']]
    clean_df = var_df.dropna()
    prediction_df = clean_df[['st_teff', 'st_rad', 'st_mass', 'st_met', 'st_age', 'st_dens', 'st_radv', 'st_logg']]
    #Predict
    predTree = planet_predictor.predict(prediction_df)
    outfile = open('predictions.txt', 'w')
    outfile.write('This is the output of the prediction. The machine Learning Model has a 81 percent accuracy score. The model is constantly being improved, stay up to date with our repository: https://github.com/gaiborjosue/ml_exoplanet_prediction  -  Rights Reserved Edward Gaibor. https://edwardgaibor.me' + '\n')
    for item in predTree:
        outfile.write(str(item) + '\n')
    outfile.close()
    return print('The Predictions were saved to "predictions.txt" file. Each line of the TXT file corresponds to each prediction. PD: The datafile was cleaned, which means that every NaN value was removed.')

if args.datafile:
    Predict_Complex()

if args.datafile == None:
    for arg in vars(args):
        if arg in simple_args:
            pred_args.append(int(getattr(args, arg)))
    Predict_Simple(pred_args)
