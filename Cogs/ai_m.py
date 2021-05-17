import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import requests

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command(name='toonify', aliases=['toon'])
    async def toonify(self,ctx: SlashContext,*args):
      """Toonify image"""
      l = await ctx.history(limit=5).flatten()
      for msg in l:
          if(msg.attachments):
            url = msg.attachments
            #await ctx.send(url)
            r = requests.post("https://api.deepai.org/api/toonify",data={'image': url,},headers={'api-key': 'd79a90fc-ef0c-4064-a1dc-4abff1cd8580'})
            #await ctx.send(str(r.json()))
            output = r.json()['output_url']
            embed = discord.Embed(title='Toonify AI', url="https://toonify.photos/")
            embed.set_image(url=output)
            embed.set_footer(text="Model Powered by DeepAI")
            await ctx.send(embed=embed)
          ''' else:
            await ctx.send('No image found (Only PNG,JPG and JPEG Supported') '''

    @cog_ext.cog_slash(name="toonify")
    async def toonify_slash(self, ctx: SlashContext):
        l = await ctx.history(limit=5).flatten()
        for msg in l:
          if(msg.attachments):
            url = msg.attachments
            #await ctx.send(url)
            r = requests.post("https://api.deepai.org/api/toonify",data={'image': url,},headers={'api-key': 'd79a90fc-ef0c-4064-a1dc-4abff1cd8580'})
            #await ctx.send(str(r.json()))
            output = r.json()['output_url']
            embed = discord.Embed(title='Toonify AI', url="https://toonify.photos/")
            embed.set_image(url=output)
            embed.set_footer(text="Model Powered by DeepAI")
            await ctx.send(embed=embed)
          ''' else:
            await ctx.send('No image found (Only PNG,JPG and JPEG Supported') '''

    @commands.command(name='enhance', aliases=['enhancer'])
    async def enhance(self,ctx: SlashContext,*args):
        """Super Resolution Image"""
        l = await ctx.history(limit=5).flatten()
        for msg in l:
            if(msg.attachments):
              url = msg.attachments
              #await ctx.send(url)
              r = requests.post("https://api.deepai.org/api/torch-srgan",data={'image': url,},headers={'api-key': 'd79a90fc-ef0c-4064-a1dc-4abff1cd8580'})
              #await ctx.send(str(r.json()))
              output = r.json()['output_url']
              embed = discord.Embed(title='Super Resolution AI', url="https://toonify.photos/")
              embed.set_image(url=output)
              embed.set_footer(text="Model Powered by DeepAI")
              await ctx.send(embed=embed)

    @commands.command(name='colorize', aliases=['colorizer'])
    async def colorize(self,ctx: SlashContext,*args):
        """Colorize Image"""
        l = await ctx.history(limit=5).flatten()
        for msg in l:
            if(msg.attachments):
              url = msg.attachments
              #await ctx.send(url)
              r = requests.post("https://api.deepai.org/api/colorizer",data={'image': url,},headers={'api-key': 'd79a90fc-ef0c-4064-a1dc-4abff1cd8580'})
              #await ctx.send(str(r.json()))
              output = r.json()['output_url']
              embed = discord.Embed(title='Deoldify AI', url="https://deoldify.ai/")
              embed.set_image(url=output)
              embed.set_footer(text="Model Powered by DeepAI")
              await ctx.send(embed=embed)

def setup(client):
    client.add_cog(AI(client))