import os
import pandas as pd
 
# iterate over all files within "My_Folder"
for file in os.listdir(r"C:\Users\Salim Satriajati\Documents\OJT BPS\scrap_fenomena\scraper\detik\artikel_baru"):
    if file.endswith(".csv"):
        tmp = pd.read_csv(os.path.join(r"C:\Users\Salim Satriajati\Documents\OJT BPS\scrap_fenomena\scraper\detik\artikel_baru", file))
        tmp.to_csv("merged.csv", index=False, header=False, mode='a')