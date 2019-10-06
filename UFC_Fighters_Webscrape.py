#The Almighty Imports
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

################################################## URL's of Interest ###################################################
#Ufc_Fighters_Url = urllib.request.urlopen("http://ufcstats.com/statistics/fighters/?char={}&page=all").read()
characters = 'abcdefghijklmnopqrstuvwxyz'

All_Fighters = []
Fighter_IDs = []
##################################################### All Fighters #######################################################
for i in characters:
    url = "http://ufcstats.com/statistics/fighters?char={}&page=all".format(i)
    #url = requests.get(url)
    All_Fighters_Soup = BeautifulSoup(requests.get(url).text, 'lxml')
    All_Fighters_Table = All_Fighters_Soup.find_all('table')[0]
    All_Fighters_df = pd.read_html(str(All_Fighters_Table), header=0, skiprows=1)
    All_Fighters_df=pd.concat(All_Fighters_df)
    All_Fighters.append(All_Fighters_df)

    for rows in All_Fighters_Table.findAll('tr', {'class':'b-statistics__table-row'}):

        row = rows.find('a', href=True)
        try:
            Fighter_IDs.append(row.get('href'))
        except:
            continue

All_Fighters_df = pd.concat(All_Fighters)
All_Fighters_df = All_Fighters_df.rename(columns={"Unnamed: 0":"First", "Unnamed: 1":"Last", "Unnamed: 2":"Nickname", "Unnamed: 3":"Height",
                                                      "Unnamed: 4":"Weight", "Unnamed: 5":"Reach", "Unnamed: 6":"Stance", "Unnamed: 7":"Wins",
                                                      "Unnamed: 8":"Losses", "Unnamed: 9":"Draws", "Unnamed: 10":"Belt"})


print(len(All_Fighters_df))
print(len(Fighter_IDs))
All_Fighters_df['Fighter_ID'] = Fighter_IDs
All_Fighters_df.to_csv('UFC_Fighters.csv')


