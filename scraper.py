#%%
'''
This is a model script needed to search and retrieve a list of PMIDs relating to a user-specified gene list. The a new gene list should be added for each new org or subspecies researched.
'''
from Bio import Entrez

Entrez.email = 'epennington@gwmail.gwu.edu'
sEntericaGeneList = ['parE', 'parC', 'gyrA', 'gyrB', 'soxR','csgA','hilA','ihfA','invA','invE','phoP','sopE','spvC','rrd 16s rRNA', 'tet']

pmidList =[]

for gene in sEntericaGeneList:
    handle = Entrez.esearch(db='pubmed', term=('Salmonella enterica[title], substitution[title]' + gene))
    record = Entrez.read(handle)
    pmidList.append(record['IdList'])
        
print("Salmonella enterica PMIDs:\n",pmidList)


# %%

from Bio import Entrez

Entrez.email = 'epennington@gwmail.gwu.edu'
handle = Entrez.esearch(db='pubmed', term=('Salmonella enterica[title]'+ 'substitution[title]' + 'ramR'))
record = Entrez.read(handle)
print("Salmonella enterica PMIDs:\n",record['IdList'])

# %%
