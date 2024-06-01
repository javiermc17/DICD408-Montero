import pandas as pd
import numpy as np

# Extraccion
wine_url = "ejemplo_entrada_titanic_sg.csv"
wine_data = pd.read_csv(wine_url)


#Initial look at the data
print (wine_data.head())


#Transformation
#








#Loading
#Saving the transformed data as csv file
wine_data.to_csv('wine_datasets.csv', index=False)
wine_quality_data.to_csv('wine_quality_dataset.csv', index=False)


