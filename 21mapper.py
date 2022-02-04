# Ajay Kumar Reddy Arram

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 8): 
    state,numcol,yieldpercol,totalprod, stocks, priceperlb, prodvalue,year = datalist

    # print intermediate key-value pairs to standard output
    print(state,"\t",prodvalue)