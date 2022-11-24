#%%

from Bio import Entrez

Entrez.email = 'epennington@gwmail.gwu.edu'
sEntericaGeneList = ['parE', 'parC', 'gyrA', 'gyrB', 'soxR','csgA','hilA','ihfA','invA','invE','phoP','sopE','spvC','rrd 16s rRNA']

pmidList =[]

for gene in sEntericaGeneList:
    handle = Entrez.esearch(db='pubmed', term=('Salmonella enterica[title], substitution[title]' + gene))
    record = Entrez.read(handle)
    pmidList.append(record['IdList'])
        
print("Salmonella enterica PMIDs:\n",pmidList)


# %%

