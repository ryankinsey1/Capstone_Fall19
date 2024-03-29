#The Almighty Imports
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

################################################## URL's of Interest ###################################################
Ufc_Events_Url = urllib.request.urlopen("http://www.ufcstats.com/statistics/events/completed?page=all").read()
Ufc_Fighters_Url = urllib.request.urlopen("http://ufcstats.com/statistics/fighters?char=a&page=all").read()


################################################# Explore URL #################################################
#Page1 = requests.get(Ufc_Events_Url)
#Page2 = requests.get(Ufc_Fighters_Url)

#Check Server Status
#If prints 500, error. If prints 200, success.
#print(Page1.status_code)
#print(Page2.status_code)

#Page1_Contents = BeautifulSoup(Page1.content, 'html.parser')
#print(Page_Contents.prettify())
#BINGO -- {Table class="b-statistics__table-events"}


##################################################### All Events #######################################################

All_Events_Soup = BeautifulSoup(Ufc_Events_Url, 'lxml')
All_Events_Table = All_Events_Soup.find_all('table')[0]
All_Events_df = pd.read_html(str(All_Events_Table), header=0, skiprows=1)
All_Events_df = pd.concat(All_Events_df)
All_Events_df = All_Events_df.rename(columns={"Unnamed: 0":"Name/Date", "Unnamed: 1":"Location"})

#Each row of the HTML table has an href link that leads to another table
#This href can be used as the Event_ID for that set of fights
Event_IDs = []
for Event_ID in All_Events_Table.findAll('a', href=True):
    Event_IDs.append(Event_ID.get('href'))

All_Events_df['Event_ID'] = Event_IDs
#First row is the next/upcoming UFC event, we are only interested in past fights with stats
All_Events_df.drop([0], inplace=True)
All_Events_df.reset_index(inplace=True, drop=True)
All_Events_df.to_csv('UFC_Events.csv')


###################################################### All Fights #####################################################
#Now we need to get the fights data from all events. The 'Event_ID' url will be useful.
All_Fights_df = []
Fight_IDs = []
for index, row in All_Events_df.iterrows():
    url = row["Event_ID"]
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    All_Fights_df.append(df[0])
    print(index) #my version of a 'progress bar'
    for rows in table.find_all('tr', {'class':'b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click'}):
        row = rows.find('a', href=True)
        Fight_IDs.append({'Fight_ID':row.get('href'), 'Event_ID':url})


All_Fights_df = pd.concat(All_Fights_df, ignore_index=True)
Fight_IDs_df = pd.DataFrame(Fight_IDs)
All_Fights_df = pd.concat([All_Fights_df, Fight_IDs_df], ignore_index=True, axis=1)
All_Fights_df = All_Fights_df.rename(columns={0:"W_L", 1:"Fighter_Names",2:"STR", 3:"TD", 4:"SUB", 5:"PASS", 6:"Weight_Class", 7:"Method", 8:"Round", 9:"Time", 10:"Fight_ID", 11:"Event_ID"})
All_Fights_df.to_csv('UFC_Fights.csv')

