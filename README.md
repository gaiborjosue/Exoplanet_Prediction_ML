![Capture](https://user-images.githubusercontent.com/78832141/126161425-0f24c163-972e-455a-b3f0-bd2325923492.PNG)
# The Exoplanet Predictor
The Exoplanet Predictor Version 1.0 - Predict the number of planets of a system based on the stellar characteristics. The usage of this tool is through the command line (CMD). 

## Usage

### Single Prediction

To use this tool you have two options, the first one is to predict the number of planets that a system with only *ONE* star has. For this, enter the directory of the *model_predictor.py* file and open the CMD. And type:

`model_predictor.py -h`

This will display the help menu of the tool, in which you can find the 8 required inputs with their description.

For example, you will need to enter the following in the command line: `model_predictor.py -t VALUE -r VALUE -m VALUE -mt VALUE -a VALUE -d VALUE -v VALUE -l VALUE`

After you enter the required fields, the algorithm will do its job ;).

### Multiple Predictions

**So, what happens if you need to predict the number of planets for multiple systems at once?** Here is when the second option of usage comes to the game. For this option you will need to provide the path of the CSV (dataframe file) in which you store all the hundreds of systems. Please note that for the headers of your database it must contain st_teff  st_rad  st_mass  st_met  st_age  st_dens  st_radv st_logg, separated with a comma ",". If you need an example of what a dataframe file should look like please refer to Data/PSCompPars_2021.04.20_19.50.36.csv

This means you should enter the following in the command line: `model_predictor.py -data PATH TO YOUR FILE`

After you enter the required fields, it will promt you the following: `The Predictions were saved to "predictions.txt" file. Each line of the TXT file corresponds to each prediction. PD: The datafile was cleaned, which means that every NaN value was removed.` 
 
You can find the predictions.txt file in the current directory.


### References
The database used to train the algorithm was produced by the NASA Exoplanet Archive  http://exoplanetarchive.ipac.caltech.edu
