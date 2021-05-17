import json 
import pandas as pd
import requests
import random

subreddit = 'python'
limit = 100
timeframe = 'month' #hour, day, week, month, year, all
listing = 'top' # controversial, best, hot, new, random, rising, top
  
def get_reddit(subreddit,listing,limit,timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
 

def get_results(r):
    '''
    Create a DataFrame Showing Title, URL, Score and Number of Comments.
    '''
    myDict = {}
    for post in r['data']['children']:
        myDict[post['data']['title']] = {'title':post['data']['title'],'url':post['data']['url'],'sub':post['data']['subreddit'],'comments':post['data']['num_comments'],'permalink':post['data']['permalink'],'selftext':post['data']['selftext'],'flair':post['data']['link_flair_text']}

    df = pd.DataFrame.from_dict(myDict, orient='index')
    return df

 
def get_reddit_image(subreddit,listing,limit,timeframe):
    r = get_reddit(subreddit,listing,limit,timeframe)
    df = get_results(r)
    final_meme = df[df['url'].str.contains('png|gif|jpg|jpeg')].iloc[random.choice(range(len(df)))]
    return(final_meme['title'],final_meme['url'],final_meme['sub'],"https://www.reddit.com"+final_meme['permalink'])

def get_reddit_ind_image(subreddit,listing,limit,timeframe):
    r = get_reddit(subreddit,listing,limit,timeframe)
    df = get_results(r)
    df = df[df['flair'] != None][df['flair'] == 'MEME'][df['url'].str.contains('jpg')]
    final_meme = df.iloc[random.choice(range(len(df)))]
    return(final_meme['title'],final_meme['url'],final_meme['sub'],"https://www.reddit.com"+final_meme['permalink'])



def get_results_text(r):
    '''
    Create a DataFrame Showing Title, URL, Score and Number of Comments.
    '''
    myDict = {}
    for post in r['data']['children']:
        myDict[post['data']['title']] = {'title':post['data']['title'],'score':post['data']['score'],'comments':post['data']['num_comments'],'permalink':post['data']['permalink'],'selftext':post['data']['selftext']}
    df = pd.DataFrame.from_dict(myDict, orient='index')
    return df


def get_reddit_text(subreddit,listing,limit,timeframe):
    r = get_reddit(subreddit,listing,limit,timeframe)
    l = list()
    for i in range(len(r['data']['children'])):
        if('Match Thread' in r['data']['children'][i]['data']['title']):
            text = r['data']['children'][i]['data']['title']
            l.append([text,i])
    return '\n'.join(r['data']['children'][l[0][1]]['data']['selftext'].split('\n')[3:-3])

def get_reddit_text2(subreddit,listing,limit,timeframe):
    r = get_reddit(subreddit,listing,limit,timeframe)
    l = list()
    for i in range(len(r['data']['children'])):
        if('Match Thread' in r['data']['children'][i]['data']['title']):
            text = r['data']['children'][i]['data']['title']
            l.append([text,i])
    return '\n'.join(r['data']['children'][l[1][1]]['data']['selftext'].split('\n')[4:-4])
