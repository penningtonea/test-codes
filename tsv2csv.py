import re

# make sure both files are in the right folder. use the right file names, below are examples

doc1 = "TTIMS_drms.tsv"
doc2 = "TTIMS_drms.csv"

with open(doc1,'r') as tsvfile:
    with open(doc2, 'w') as csvfile:
        for line in tsvfile:
            separator = re.sub("\t",",",line)
            csvfile.write(separator)
print("file converted sucessfully")