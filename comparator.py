#%% DB Comparator Script

'''
Use this script to compare two data tables and retrieve a list of DRMs that are unique to each. The DRMs that are returned from the script are missing from one of the databases, and should be added.

comparing the following columns:

wt_amino_acid
amino_acid_pos_refseq
mut_amino_acid

Tables must be saved in CSV UTF-8 Format.

'''
import pandas as pd 
print("Ready!")

#%%
p1 = "C:/Users/Emily/OneDrive/Desktop/School/Thesis/codes/HIV_table1.csv"

p2 = "C:/Users/Emily/OneDrive/Desktop/School/Thesis/codes/HIV_table2.csv"

db1 = pd.read_csv(p1)
db2 = pd.read_csv(p1)

df1 = db1[['wt_amino_acid','amino_acid_pos_refseq','mut_amino_acid']]
df2 = db2[['wt_amino_acid','amino_acid_pos_refseq','mut_amino_acid']]

# df1.compare(df2, keep_shape=True, keep_equal=True) 
# cannot use compare if dataframes are not the same shape 


# nested for loop 




#%%
# make data files into sets for comparison


# ds1 = set(DB1)
# ds2 = set(DB2)

# print(ds1.intersection(ds2))

# %%
