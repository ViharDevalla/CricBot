import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import requests
import io
import pandas as pd

class Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command(name='india', aliases=['nation'])
    async def toonify(self,ctx: SlashContext,*args):
      """COVID Statistics - Nation-wide"""
      url ='https://api.covid19india.org/csv/latest/state_wise.csv'
      r = requests.get(url)

      df = pd.read_csv(io.StringIO(r.text), sep=',', engine='python')
      embed = discord.Embed(title='National COVID19 Statistics ', url="https://www.covid19india.org/",color=discord.Color.gold())
      embed.add_field(name="Active", value=df.iloc[0]['Active'], inline=False)
      embed.add_field(name="Confirmed", value=df.iloc[0]['Confirmed'], inline=False)
      embed.add_field(name="Recovered", value=df.iloc[0]['Recovered'], inline=False)
      embed.add_field(name="Deaths", value=df.iloc[0]['Deaths'], inline=False)
      embed.set_footer(text="Model Powered by COVID-API\nLast Updated "+df.iloc[0]['Last_Updated_Time'])
      await ctx.send(embed=embed)
    
    @cog_ext.cog_slash(name="india",description=' COVID Statistics - Nation-wide')
    async def meme_slash(self, ctx: SlashContext):
      """COVID Statistics - Nation-wide"""
      url ='https://api.covid19india.org/csv/latest/state_wise.csv'
      r = requests.get(url)
      df = pd.read_csv(io.StringIO(r.text), sep=',', engine='python')
      embed = discord.Embed(title='National COVID19 Statistics ', url="https://www.covid19india.org/",color=discord.Color.gold())
      embed.add_field(name="Active", value=df.iloc[0]['Active'], inline=False)
      embed.add_field(name="Confirmed", value=df.iloc[0]['Confirmed'], inline=False)
      embed.add_field(name="Recovered", value=df.iloc[0]['Recovered'], inline=False)
      embed.add_field(name="Deaths", value=df.iloc[0]['Deaths'], inline=False)
      embed.set_footer(text="Model Powered by COVID-API\nLast Updated "+df.iloc[0]['Last_Updated_Time'])
      await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Covid(client))