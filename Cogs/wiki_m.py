import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import requests
import wikipedia

def wiki(query):
    l = wikipedia.search(query, results=10, suggestion=False)
    #print(l)
    return(wikipedia.summary(l[0], sentences=0, chars=2048, auto_suggest=False, redirect=True))

def wikigeo(lat,lon):
    l1=wikipedia.geosearch(lat, lon,title=None, results=10, radius=1000) 
    #print(l1[0])
    return(l1[0],wikipedia.summary(l1[0], sentences=0, chars=2048, auto_suggest=False, redirect=True))


class Wikipedia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
      
    @commands.command(name='wiki', aliases=['wikipedia','brainpower','knw'])
    async def wiki_funct(self,ctx: SlashContext,*args):
        """Gets Wikipedia Summary Search"""

        query = ' '.join(args)
        embed = discord.Embed(title=query, description=wiki(query))
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="wiki",description='Gets Wikipedia Summary Search')
    async def wiki_slash(self, ctx: SlashContext,*args):
        """Gets Wikipedia Summary Search"""
        query = ' '.join(args)
        embed = discord.Embed(title=query, description=wiki(query))
        await ctx.send(embed=embed)

    @commands.command(name='geoloc', aliases=['wikigeo','latlong','location'])
    async def wiki_loc(self,ctx: SlashContext,*args):
        """Gets Geolocation from Wikipedia"""

        if(len(args)>3):
          await ctx.send("Maximum of 2 arguments are allowed")

        else:
          lat = args[0]
          longi = args[1]
          title,outp = wikigeo(lat,longi)
          embed = discord.Embed(title=title, description = outp)
          await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="geoloc",description='Gets Geolocation from Wikipedia')
    async def wiki_loc_slash(self, ctx: SlashContext,*args):
      """Gets Geolocation from Wikipedia"""
      if(len(args)>3):
          await ctx.send("Maximum of 2 arguments are allowed")

      else:
          lat = args[0]
          longi = args[1]
          title,outp = wikigeo(lat,longi)
          embed = discord.Embed(title=title, description = outp)
          await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Wikipedia(client))