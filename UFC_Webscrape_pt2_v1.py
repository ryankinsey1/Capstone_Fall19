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
fighter_1 = []
for index, row in All_Fights_df.iterrows():
    url = row["Fight_ID"]
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    fighter_1_result = soup.findAll("i", attrs= {'class': 'b-fight-details__person-status'})
    fighter_1_name = soup.findAll("h3", attrs = {'class': 'b-fight-details__person-name'})
    fighter_1_nickname = soup.findAll("p", attrs = {'class': 'b-fight-details__person-title'})
    # f1_result = fighter_1_result.get_text()
    # f1_result = f1_results.append(f1_result)
    # f1_name = fighter_1_name.get_text()
    # f1_name = f1_name.append(f1_result)
    # f1_nickname = fighter_1_nickname.get_text()
    # f1_nickname = f1_nickname.append(f1_result)

    fighter_1_1 = {'result':fighter_1_result, 'name':fighter_1_name, 'nickname':fighter_1_nickname}
    print(fighter_1_1)



print(fighter_1)
# print(f1_results.head())
# print(f1_name.head())
# print(f1_nickname.head())