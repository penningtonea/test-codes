'''
written to re-format the HIV-1 DRM table from the gag-pol protein coordinates and name into protease, RTase, and integrase regions and show results in new table. Requested by collaborators for use in DRM pipeline.
'''

import pandas as pd 

df = pd.read_csv("DRM_tables - HIV_table.csv", sep=",")
df2 = df[:,[7, 11, 12, 13]]

print(df2)