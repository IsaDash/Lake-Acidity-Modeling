import csv
import pandas as pd

# infile = open("acid.csv", "r")
# outfile = open("lake_data_transformed.csv", "w", newline="")

# in_csv = csv.reader(infile)
# out_csv = csv.writer(outfile)

# for row in in_csv:
#     to_add = True
#     if row["SIO2_MG_L (silicon dioxicde)"] == None:
#         continue
#     else:
#         out_csv.writerow(row)

# infile.close()
# outfile.close()
    
acid_data = pd.read_csv('acid.csv')
modified_acid = acid_data.dropna()

modified_acid.to_csv('lake_data_cleaned.csv', index=False)