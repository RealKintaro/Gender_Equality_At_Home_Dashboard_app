
import pandas as pd
import pathlib


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../datasets").resolve()

df_region = pd.read_excel(DATA_PATH.joinpath("2020_region.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle
df_country = pd.read_excel(DATA_PATH.joinpath("2020_country.xlsx"),sheet_name= 'Data',header=0)
region_codebook_df = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Codebook',header=0)
country_codebook_df = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Codebook',header=0)

regions = df_region.Region.unique()
countrys = df_country.Country.unique()

region_codebook2020 = region_codebook_df.query('Wave == "all" | Wave == "wave 1"')
country_codebook2020 = country_codebook_df.query('Wave == "all" | Wave == "wave 1"')

covidc =  country_codebook2020.query(" `Category theme` == 'covid' | `Category theme`==''")
democ =  country_codebook2020.query(" `Category theme` == 'demographics' | `Category theme`==''")
naac =  country_codebook2020.query(" `Category theme` == 'norms, access, and agency' | `Category theme`==''")
tcwc =  country_codebook2020.query(" `Category theme` == 'time spent, care, and work' | `Category theme`==''")

covidr =  region_codebook2020.query(" `Category theme` == 'covid' | `Category theme`==''")
demor =  region_codebook2020.query(" `Category theme` == 'demographics' | `Category theme`==''")
naar =  region_codebook2020.query(" `Category theme` == 'norms, access, and agency' | `Category theme`==''")
tcwr =  region_codebook2020.query(" `Category theme` == 'time spent, care, and work' | `Category theme`==''")

i=0
mask1 = []
figlist = []
for q in tcwc['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_country["Country"] == 'Canada'
        test= tcwc["Wave"].where(tcwc['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = tcwc['Variable'].where(tcwc['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = tcwc['Wave 1 Variable'].where(tcwc['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        print(mask1[i])
        i+=1
        


# for q in covid['[old] Parameter or Survey Question'].str.strip().unique():
        
#         print(covid['Variable Name'].where(covid['[old] Parameter or Survey Question'] == q).head())
        
        