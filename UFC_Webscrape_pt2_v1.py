#The Almighty Imports
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request


pd.set_option('display.max_columns', 20)
UFC_Events = pd.read_csv('UFC_Events.csv')
UFC_Events.drop(UFC_Events.columns[[0]],axis=1, inplace=True)
UFC_Fights = pd.read_csv('UFC_Fights.csv')
UFC_Fights.drop(UFC_Fights.columns[[0]],axis=1, inplace=True)
#print(UFC_Events)
#print(UFC_Fights)
############################################### Fight Stats#############################################################
# def scrape_fight_data(Event_ID):
#     for tr in trs:
#         df_rows = []
#         for td in tds:
#             if td == 0: continue





# f1_results = []
# f1_name = []
# f1_nickname = []
fight = []
for index, row in UFC_Fights.iterrows():
    url = row["Fight_ID"]
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    event_name = soup.find('h2', attrs={'class': 'b-content__title'})
    fighter_1_result = soup.findAll("i", attrs= {'class': 'b-fight-details__person-status'})[0]
    fighter_1_name = soup.findAll("h3", attrs = {'class': 'b-fight-details__person-name'})[0]
    fighter_1_nickname = soup.findAll("p", attrs = {'class': 'b-fight-details__person-title'})[0]
    fighter_2_result = soup.findAll("i", attrs= {'class': 'b-fight-details__person-status'})[1]
    fighter_2_name = soup.findAll("h3", attrs = {'class': 'b-fight-details__person-name'})[1]
    fighter_2_nickname = soup.findAll("p", attrs = {'class': 'b-fight-details__person-title'})[1]
    weight_class = soup.find('div', attrs = {'class':'b-fight-details__fight-head'})


    method = soup.find('i', attrs={'class':'b-fight-details__text-item_first'})
    round = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[0]
    time = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[1]
    round_format = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[2]
    ref = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[3]
    total_strikes = soup.findAll('seletion')
    fight = {'Event_Name':event_name.get_text(strip=True),'Result_Fighter_1':fighter_1_result.get_text(strip=True),
             'Name_Fighter_1':fighter_1_name.get_text(strip=True), 'Nickname_Fighter_1':fighter_1_nickname.get_text(strip=True),
             'Result_Fighter_2':fighter_2_result.get_text(strip=True), 'Name_Fighter_2':fighter_2_name.get_text(strip=True),
             'Nickname_Fighter_2':fighter_2_nickname.get_text(strip=True),'Weight_Class':weight_class.get_text(strip=True),
             'Method':method.get_text(strip=True), 'Round':round.get_text(strip = True), 'Time':time.get_text(strip = True),
             'Round_Format':round_format.get_text(strip=True), 'Ref':ref.get_text(strip=True)}
    print(fight)



# print(fighter_1)
# # print(f1_results.head())
# # print(f1_name.head())
# # print(f1_nickname.head())