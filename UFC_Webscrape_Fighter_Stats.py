#The Almighty Imports
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from itertools import islice


pd.set_option('display.max_columns', 20)
UFC_Fighters = pd.read_csv('UFC_Fighters.csv')
UFC_Fighters.drop(UFC_Fighters.columns[[0]],axis=1, inplace=True)
############################################### Fight Stats#############################################################

fighters = []
for index, row in UFC_Fighters.iterrows():
     url = row["Fighter_ID"]
     soup = BeautifulSoup(requests.get(url).text, 'lxml')
     name = soup.find('span', {'class': 'b-content__title-highlight'})
     height = soup.findAll('li', {'class': 'b-list__box-list-item b-list__box-list-item_type_block'})[0]
     weight = soup.findAll('li', {'class': 'b-list__box-list-item b-list__box-list-item_type_block'})[1]
     reach = soup.findAll('li', {'class': 'b-list__box-list-item b-list__box-list-item_type_block'})[2]
     stance = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[3]
     DOB = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[4]
     SLpM = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[5]
     Str_Acc = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[6]
     SApM = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[7]
     Str_Def = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[8]
     TD_Avg = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[10]
     TD_Acc = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[11]
     TD_Def = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[12]
     Sub_Avg = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})[13]

     fighter = {'Name':name.get_text(strip=True),'Height':height.get_text(strip=True),'Weight':weight.get_text(strip=True),
                'Reach':reach.get_text(strip=True),'Stance':stance.get_text(strip=True),
                'DOB':DOB.get_text(strip=True),'SLpm':SLpM.get_text(strip=True),
                'Str_Acc':Str_Acc.get_text(strip=True),'SApM':SApM.get_text(strip=True),
                'Str_Def':Str_Def.get_text(strip=True),'TD_Avg':TD_Avg.get_text(strip=True),
                'TD_Acc':TD_Acc.get_text(strip=True),'TD_Def':TD_Def.get_text(strip=True),
                'Sub_Avg':Sub_Avg.get_text(strip=True),
                'Fighter_ID':url}
     fighters.append(fighter.copy())
     print(index)
     print(fighter.copy())

All_UFC_Fighter_Stats_df = pd.DataFrame(fighters)
All_UFC_Fighter_Stats = All_UFC_Fighter_Stats_df.to_csv("All_UFC_Fighter_Stats.csv")
