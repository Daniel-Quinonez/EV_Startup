import pandas as pd
import numpy as np

//First we must preform an EDA in order to clean our data 
//Since we are using our own data set we have scraped there is no need to drop axis


//Create a dataframe out of the current csv
df = pd.read_csv("EV_dataset.csv")
df.head()
