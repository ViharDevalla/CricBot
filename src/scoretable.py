""" import requests
from html_table_parser import HTMLTableParser
import pandas as pd



def scoreboard():
    url = 'https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/points-table'
    page = requests.get(url)
    p = HTMLTableParser()
    p.feed(str(page.content))
    scoreboard = [p.tables[0][1],p.tables[1][1],p.tables[2][1],p.tables[3][1],p.tables[4][1],p.tables[5][1],p.tables[6][1],p.tables[7][1]]
    df = pd.DataFrame(scoreboard,columns=['Teams', 'Mat', 'Won', 'Lost', 'Tied', 'NR', 'Pts', 'NRR', '']) 
    return(str('```'+df.to_string()+'```')) """
