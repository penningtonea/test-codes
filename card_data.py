#%%
# the data is downloaded directly from the CARD database. All organisms in this chart belong to Salmonella Enterica subspecies. RefSeq DNA accessions are included.
from functools import reduce
import pandas as pd
print('ready')

# load the file 
path = "C:/Users/Emily/OneDrive/Desktop/School/Thesis/Salmonella/sEnterica_genome_card_data.csv"

with open(path) as cardFile:
    cardDf = pd.read_csv(cardFile)

# slice column, drop duplicates and NaN values
hitSer = cardDf['perfect_hits'].drop_duplicates()
hitList = hitSer.dropna()

hits = reduce(lambda x,y: x+y, hitList)


# hits = hitList.values.astype(str)


# %%
