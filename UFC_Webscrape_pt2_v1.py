#The Almighty Imports
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from itertools import islice

####### THIS DOCUMENT RUNS BETTER IN JUPITER NOTEBOOK #######

pd.set_option('display.max_columns', 20)
UFC_Events = pd.read_csv('UFC_Events.csv')
UFC_Events.drop(UFC_Events.columns[[0]],axis=1, inplace=True)
UFC_Fights = pd.read_csv('UFC_Fights.csv')
UFC_Fights.drop(UFC_Fights.columns[[0]],axis=1, inplace=True)
#print(UFC_Events)
#print(UFC_Fights)
############################################### Fight Stats#############################################################

fights = []
for index, row in islice(UFC_Fights.iterrows(), 0, 10):
    url = row["Fight_ID"]
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    event_name = soup.find('h2', attrs={'class': 'b-content__title'})
    fighter_1_result = soup.findAll("div", attrs= {'class': 'b-fight-details__person'})[0]
    fighter_1_result = fighter_1_result.find('i')
    fighter_1_name = soup.findAll("h3", attrs = {'class': 'b-fight-details__person-name'})[0]
    fighter_1_nickname = soup.findAll("p", attrs = {'class': 'b-fight-details__person-title'})[0]
    fighter_2_result = soup.findAll("div", attrs= {'class': 'b-fight-details__person'})[1]
    fighter_2_result = fighter_2_result.find('i')
    fighter_2_name = soup.findAll("h3", attrs = {'class': 'b-fight-details__person-name'})[1]
    fighter_2_nickname = soup.findAll("p", attrs = {'class': 'b-fight-details__person-title'})[1]
    weight_class = soup.find('div', attrs = {'class':'b-fight-details__fight-head'})
    method = soup.find('i', attrs={'class':'b-fight-details__text-item_first'})
    round = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[0]
    time = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[1]
    round_format = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[2]
    ref = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[3]
    details = soup.findAll('i', attrs={'class':'b-fight-details__text-item'})[4]
    tables = soup.findAll('section', attrs={'class': "b-fight-details__section js-fight-section"})
    total_strikes = tables[1]
    totals = total_strikes.findAll('tr', attrs={'class':"b-fight-details__table-row"})
    totals2 = totals[1]
    totals_stats = totals2.findAll('p', attrs={'class':"b-fight-details__table-text"})
    sig_str_div = soup.find('div', attrs={'b-fight-details'})
    sig_str_table = sig_str_div.find('table')
    sig_strs = sig_str_table.findAll('p', attrs={'class':"b-fight-details__table-text"})
    #print(totals2)
    fight = {'Event_Name':event_name.get_text(strip=True),'Result_Fighter_1':fighter_1_result.get_text(strip=True),
             'Name_Fighter_1':fighter_1_name.get_text(strip=True), 'Nickname_Fighter_1':fighter_1_nickname.get_text(strip=True),
             'Result_Fighter_2':fighter_2_result.get_text(strip=True), 'Name_Fighter_2':fighter_2_name.get_text(strip=True),
             'Nickname_Fighter_2':fighter_2_nickname.get_text(strip=True),'Weight_Class':weight_class.get_text(strip=True),
             'fighter_1_Name':totals_stats[0].get_text(strip=True), 'fighter_2_Name':totals_stats[1].get_text(strip=True),
             'fighter_1_KD':totals_stats[2].get_text(strip=True),'fighter_2_KD':totals_stats[3].get_text(strip=True),
             'fighter_1_Sig_Str':totals_stats[4].get_text(strip=True),'fighter_2_Sig_Str':totals_stats[5].get_text(strip=True),
             'fighter_1_Sig_Str_Pct':totals_stats[6].get_text(strip=True), 'fighter_2_Sig_Str_Pct':totals_stats[7].get_text(strip=True),
             'fighter_1_Total_Str':totals_stats[8].get_text(strip=True),'fighter_2_Total_Str':totals_stats[9].get_text(strip=True),
             'fighter_1_TD':totals_stats[10].get_text(strip=True), 'fighter_2_TD':totals_stats[11].get_text(strip=True),
             'fighter_1_TD_Pct':totals_stats[12].get_text(strip=True),'fighter_2_TD_Pct':totals_stats[13].get_text(strip=True),
             'fighter_1_Sub_Att':totals_stats[14].get_text(strip=True), 'fighter_2_Sub_Att':totals_stats[15].get_text(strip=True),
             'fighter_1_Pass':totals_stats[16].get_text(strip=True), 'fighter_2_Pass':totals_stats[17].get_text(strip=True),
             'fighter_1_Rev':totals_stats[18].get_text(strip=True), 'fighter_2_Rev':totals_stats[19].get_text(strip=True),
             'fighter_1_Name2':sig_strs[0].get_text(strip=True),'fighter_2_Name2':sig_strs[1].get_text(strip=True),
             'fighter_1_Sig_Str2': sig_strs[2].get_text(strip=True),'fighter_2_Sig_Str2':sig_strs[3].get_text(strip=True),
             'fighter_1_Sig_Str_Pct2': sig_strs[4].get_text(strip=True),'fighter_2_Sig_Str_Pct2': sig_strs[5].get_text(strip=True),
             'fighter_1_Sig_Str_Head': sig_strs[6].get_text(strip=True),'fighter_2_Sig_Str_Head': sig_strs[7].get_text(strip=True),
             'fighter_1_Sig_Str_Body': sig_strs[8].get_text(strip=True), 'fighter_2_Sig_Str_Body': sig_strs[9].get_text(strip=True),
             'fighter_1_Sig_Str_Leg': sig_strs[10].get_text(strip=True), 'fighter_2_Sig_Str_Leg': sig_strs[11].get_text(strip=True),
             'fighter_1_Sig_Str_Distance': sig_strs[12].get_text(strip=True), 'fighter_2_Sig_Str_Distance': sig_strs[13].get_text(strip=True),
             'fighter_1_Sig_Str_Clinch': sig_strs[14].get_text(strip=True), 'fighter_2_Sig_Str_Clinch': sig_strs[15].get_text(strip=True),
             'fighter_1_Sig_Str_Ground': sig_strs[16].get_text(strip=True), 'fighter_2_Sig_Str_Ground': sig_strs[17].get_text(strip=True),
             'Method':method.get_text(strip=True), 'Round':round.get_text(strip = True), 'Time':time.get_text(strip = True),
             'Round_Format':round_format.get_text(strip=True), 'Ref':ref.get_text(strip=True), 'Details':details.get_text(strip=True),
             'fight_ID': url
             }

    fights.append(fight.copy())
    print(index)
    print(fight.copy())

All_UFC_Fight_Stats_df = pd.DataFrame(fights)
All_UFC_Fight_Stats = All_UFC_Fight_Stats_df.to_csv("All_UFC_Fight_Stats.csv")



