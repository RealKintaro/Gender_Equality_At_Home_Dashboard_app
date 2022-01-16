
from queue import Empty
import pandas as pd
import pathlib


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../datasets").resolve()

df_regionall = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle
df_countryall = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Data',header=0)

df_region = df_regionall.query('Year == 2020')
df_country = df_countryall.query('Year == 2020')

region_codebook_df = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Codebook',header=0)
country_codebook_df = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Codebook',header=0)

regions = df_region.Region.unique()
countrys = df_country.Subregion.unique()


region_codebook2021 = region_codebook_df.query('Wave == "all" | Wave == "wave 1"')
country_codebook2021 = country_codebook_df.query('Wave == "all" | Wave == "wave 1"')

covidc =  country_codebook2021.query(" `Category theme` == 'covid' | `Category theme`==''")
democ =  country_codebook2021.query(" `Category theme` == 'demographics' | `Category theme`==''")
naac =  country_codebook2021.query(" `Category theme` == 'norms, access, and agency' | `Category theme`==''")
tcwc =  country_codebook2021.query(" `Category theme` == 'time spent, care, and work' | `Category theme`==''")

covidr =  region_codebook2021.query(" `Category theme` == 'covid' | `Category theme`==''")
demor =  region_codebook2021.query(" `Category theme` == 'demographics' | `Category theme`==''")
naar =  region_codebook2021.query(" `Category theme` == 'norms, access, and agency' | `Category theme`==''")
tcwr =  region_codebook2021.query(" `Category theme` == 'time spent, care, and work'")


i=0
mask1 = []
figlist = []
for q in tcwr['[old] Parameter or Survey Question'].str.strip().unique():
        
        test= tcwr["Wave"].where(tcwr['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = tcwr['Variable Name'].where(tcwr['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = tcwr['Variable Name'].where(tcwr['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
for i in range(len(mask1)):
        print(mask1[i])
# i=0
# mask1 = []
# figlist = []
# for q in naar['Parameter or Survey Question'].str.strip().unique():
        
#         query = naar['Variable Name'].where(naar['Parameter or Survey Question'] == q)
#         query.dropna(inplace=True)
#         mask1.append(query.values)
#         print(mask1[i])
#         i+=1
     
        


# for q in covid['[old] Parameter or Survey Question'].str.strip().unique():
        
#         print(covid['Variable Name'].where(covid['[old] Parameter or Survey Question'] == q).head())
        