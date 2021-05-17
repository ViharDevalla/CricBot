import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import requests
from bs4 import BeautifulSoup
from googlesearch import search


def stack(query):
    staccoverflow="  stackoverflow"
    query=query+staccoverflow
    list_ids=[]
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        if "stackoverflow.com" in j:
            #print(j)
            l=j.split('/')
            #print(l[4])
            list_ids.append(l[4])
    z=0
    for id in list_ids:
        z=z+1
        if z>2:
            break
        url=f'https://api.stackexchange.com/2.2/questions/{id}?&site=stackoverflow&filter=%21T%2ahPNRA69ofM1izkPP'
        response1 = requests.get(url)
        #print(response1)
        a=0
        final_list = []
        for ans in response1.json()['items'] :
            #print(ans['link'])
            for i in ans['answers']:
                a=a+1
                if a>2:
                    break
                #print(i['title'])
                soup = BeautifulSoup(i['body'],features="html.parser")
                final_list.append([ans['title'],ans['link'],soup.get_text()])
    return(final_list)




class StackOverflow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
      
    @commands.command(name='stackoverflow', aliases=['stack','overflow','stackov','prgtool'])
    async def stackoverflow(self,ctx: SlashContext,*args):
        """ Sends the search result from StackOverflow """
        query = ' '.join(args)
        data_list = stack(query)
        for i in data_list:
          embed = discord.Embed(title=i[0],url=i[1],description=i[2])
          embed.set_footer(text="Stackoverflow")
          await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="stackoverflow",description='Sends the search result from StackOverflow')
    async def stackoverflow_slash(self, ctx: SlashContext):
        """Sends the search result from StackOverflow"""
        query = ' '.join(args)
        data_list = stack(query)
        for i in data_list:
          embed = discord.Embed(title=i[0],url=i[1],description=i[2])
          embed.set_footer(text="Stackoverflow")
          await ctx.send(embed=embed)

def setup(client):
    client.add_cog(StackOverflow(client))