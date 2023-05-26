# CSV comparator script 
    # csv.loc[csv2.id.isin(csv1.id)].id 

    # [['AAREF', 'AAPOS', 'AASUB']].to_csv("missing from csv 1")
    
import pandas as pd

csv1 = pd.read_csv('phased_mutations_DRM_DEMO1.csv', sep=',')
csv2 = pd.read_csv('DRM_output-DEMO2.csv', sep=',')

drm1 = csv1.loc[:,['AAREF', 'AAPOS', 'AASUB']]
drm2 = csv2.loc[:,['AAREF', 'AAPOS', 'AASUB']]

print(drm1.isin(drm2))
print(drm2.isin(drm1))
