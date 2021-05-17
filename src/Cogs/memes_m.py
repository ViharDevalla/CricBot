import discord
from discord.ext import commands
import random
import pandas as pd
import requests
from discord_slash import cog_ext, SlashContext

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




class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.command(name='meme', aliases=['memes','dankmeme'])
    async def meme(self, ctx: SlashContext):
      """Random Dank Meme"""
      check = random.choice([0, 1, 2])
      if (check == 0):
          title, url, sub, permalink = get_reddit_image('dankmemes', 'top', 5000,'all')
      elif (check == 1):
          title, url, sub, permalink = get_reddit_image('dankmemes', 'top', 1000,'month')
      else:
          title, url, sub, permalink = get_reddit_image('dankmemes', 'top', 100,'week')

      embed = discord.Embed(title=title, url=permalink)
      embed.set_image(url=url)
      embed.set_footer(text="Subreddit :- {}".format(sub))
      await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="meme",description='Sends a random meme')
    async def meme_slash(self, ctx: SlashContext):
      """Sends a Random Dank Meme"""
      check = random.choice([0, 1, 2])
      if (check == 0):
          title, url, sub, permalink = get_reddit_image('dankmemes', 'top', 5000,'all')
      elif (check == 1):
          title, url, sub, permalink = get_reddit_image('dankmemes', 'top', 1000,'month')
      else:
          title, url, sub, permalink = get_reddit_image('dankmemes', 'top', 100,'week')

      embed = discord.Embed(title=title, url=permalink)
      embed.set_image(url=url)
      embed.set_footer(text="Subreddit :- {}".format(sub))
      await ctx.send(embed=embed)

    


    @commands.command(name='desimeme', aliases=['desimemes','indianmeme'])
    async def desimeme(self,ctx: SlashContext):
        """Sends a random Indian meme"""
        check = random.choice([0, 1, 2])
        if (check == 0):
            title, url, sub, permalink = get_reddit_image('IndianMeyMeys', 'top',5000, 'all')
        elif (check == 1):
            title, url, sub, permalink = get_reddit_image('IndianMeyMeys', 'top', 1000,'month')
        else:
            title, url, sub, permalink = get_reddit_image('IndianMeyMeys', 'top', 100,'week')

        embed = discord.Embed(title=title, url=permalink)
        embed.set_image(url=url)
        embed.set_footer(text="Subreddit :- {}".format(sub))
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="desimeme",description='Sends a random Indian meme')
    async def desimeme_slash(self, ctx: SlashContext):
      """Sends a random Indian meme"""
      check = random.choice([0, 1, 2])
      if (check == 0):
          title, url, sub, permalink = get_reddit_image('IndianMeyMeys', 'top', 5000,'all')
      elif (check == 1):
          title, url, sub, permalink = get_reddit_image('IndianMeyMeys', 'top', 1000,'month')
      else:
          title, url, sub, permalink = get_reddit_image('IndianMeyMeys', 'top', 100,'week')

      embed = discord.Embed(title=title, url=permalink)
      embed.set_image(url=url)
      embed.set_footer(text="Subreddit :- {}".format(sub))
      await ctx.send(embed=embed)


    @commands.command(name='cricmeme',aliases=['cricmemes','cricketmeme'])
    async def cric(self,ctx: SlashContext):
        """" Random Cricket Meme """
        check = random.choice([0, 1, 2])
        if (check == 0):
            title, url, sub, permalink = get_reddit_image('cricketshitpost', 'top',5000, 'all')
        elif (check == 1):
            title, url, sub, permalink = get_reddit_image('cricketshitpost', 'top',1000, 'month')
        else:
            title, url, sub, permalink = get_reddit_image('cricketshitpost', 'hot',100, 'week')

        embed = discord.Embed(title=title, url=permalink)
        embed.set_image(url=url)
        embed.set_footer(text="Subreddit :- {}".format(sub))
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="cricmeme",description='Sends a random cricket meme')
    async def cricmeme_slash(self, ctx: SlashContext):
      """ Sends a random cricket meme """
      check = random.choice([0, 1, 2])
      if (check == 0):
          title, url, sub, permalink = get_reddit_image('cricketshitpost', 'top', 5000,'all')
      elif (check == 1):
          title, url, sub, permalink = get_reddit_image('cricketshitpost', 'top', 1000,'month')
      else:
          title, url, sub, permalink = get_reddit_image('cricketshitpost', 'top', 100,'week')

      embed = discord.Embed(title=title, url=permalink)
      embed.set_image(url=url)
      embed.set_footer(text="Subreddit :- {}".format(sub))
      await ctx.send(embed=embed)


    @commands.command(name='wholesome', aliases=['wholesome meme'])
    async def wholesome(self,ctx: SlashContext):
        """Random Wholesome meme"""
        check = random.choice([0, 1, 2])
        if (check == 0):
            title, url, sub, permalink = get_reddit_image('wholesomememes', 'top',5000, 'all')
        elif (check == 1):
            title, url, sub, permalink = get_reddit_image('wholesomememes', 'top',1000, 'month')
        else:
            title, url, sub, permalink = get_reddit_image('wholesomememes', 'hot',100, 'week')

        embed = discord.Embed(title=title, url=permalink)
        embed.set_image(url=url)
        embed.set_footer(text="Subreddit :- {}".format(sub))
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="wholesome",description='Sends a random wholesome meme')
    async def wholesome(self, ctx: SlashContext):
      """ Sends a random wholesome meme """
      check = random.choice([0, 1, 2])
      if (check == 0):
          title, url, sub, permalink = get_reddit_image('wholesomememes', 'top', 5000,'all')
      elif (check == 1):
          title, url, sub, permalink = get_reddit_image('wholesomememes', 'top', 1000,'month')
      else:
          title, url, sub, permalink = get_reddit_image('wholesomememes', 'top', 100,'week')

      embed = discord.Embed(title=title, url=permalink)
      embed.set_image(url=url)
      embed.set_footer(text="Subreddit :- {}".format(sub))
      await ctx.send(embed=embed)


    @commands.command(name='programmer', aliases=['programmer meme'])
    async def programmer(self,ctx: SlashContext):
        """Random Programmer meme"""
        check = random.choice([0, 1, 2])
        if (check == 0):
            title, url, sub, permalink = get_reddit_image('programmerhumor', 'top',5000, 'all')
        elif (check == 1):
            title, url, sub, permalink = get_reddit_image('programmerhumor', 'top',1000, 'month')
        else:
            title, url, sub, permalink = get_reddit_image('programmerhumor', 'hot',100, 'week')

        embed = discord.Embed(title=title, url=permalink)
        embed.set_image(url=url)
        embed.set_footer(text="Subreddit :- {}".format(sub))
        await ctx.send(embed=embed)


    @cog_ext.cog_slash(name="programmer",description='Sends a random programmer meme')
    async def programmer_slash(self, ctx: SlashContext):
      """ Sends a random programmer meme """
      check = random.choice([0, 1, 2])
      if (check == 0):
          title, url, sub, permalink = get_reddit_image('programmerhumor', 'top', 5000,'all')
      elif (check == 1):
          title, url, sub, permalink = get_reddit_image('programmerhumor', 'top', 1000,'month')
      else:
          title, url, sub, permalink = get_reddit_image('programmerhumor', 'top', 100,'week')

      embed = discord.Embed(title=title, url=permalink)
      embed.set_image(url=url)
      embed.set_footer(text="Subreddit :- {}".format(sub))
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Memes(client))