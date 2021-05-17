#pip install --upgrade html5lib==1.0b8 ; 

import os
import discord
import requests
import random
from discord_slash import SlashCommand, SlashContext




from keep_alive import keep_alive
from discord.ext import commands

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='sudo ', intents=intents)
slash = SlashCommand(bot,sync_commands=True)




@bot.event
async def on_ready():
    print("Bot is ready")

# A simple and small ERROR handler
@bot.event
async def on_command_error(ctx: SlashContext, error):
    embed = discord.Embed(title='', color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(
            name=f'Invalid Permissions',
            value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name=f':x: Terminal Error', value=f"```{error}```")
        await ctx.send(embed=embed)
        raise error

# Load command to manage our "Cogs" or extensions
@bot.command()
async def load(ctx: SlashContext, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


# Unload command to manage our "Cogs" or extensions
@bot.command()
async def unload(ctx: SlashContext, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


# Reload command to manage our "Cogs" or extensions
@bot.command(name="reload")
async def reload_(ctx: SlashContext, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloaded the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


# Automatically load all the .py files in the Cogs folder
for filename in os.listdir('./Cogs'):
    if filename.endswith('_m.py'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception


@bot.command(name='hi', help='Bot says hi')
async def hi(ctx: SlashContext):
    message2 = 'Hi there, ' + str(ctx.message.author)[:-5]
    await ctx.send('{}'.format(message2))

@bot.command(name='cricplay', help='CricGo Game - Book Cricket in Python')
async def toss(ctx: SlashContext):
        await ctx.send('What do You Wanna Choose? (odd/eve):')
        msg = await bot.wait_for("message", check=check)
        await ctx.send('Play your number for the toss(1/2):')
        msg1 = await bot.wait_for("message", check=check1)
        if int(msg1.content) >2:
            await ctx.send('You are only allowed to use 1 and 2.')
            exit()
        else:
            print('bot not taken decison')
            z=random.randint(1,2)
            print('bot taken decison')
            await ctx.send(f"I've Chosen {z}")

            if msg.content.lower() =='eve':
                if ((int(msg1.content)+z)%2)==0:
                    await ctx.send('You have Won the Toss')
                    await ctx.send('What Do You Opt?(bat/bowl)')
                    msg2 = await bot.wait_for("message", check=check2)
                    if msg2.content.lower() == 'bat':
                        await ctx.send('CricGo is going to bowl')
                        total = 0
                        while (True):
                            #match = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Play Your Shot:')
                            msg3 = await bot.wait_for("message", check=check3)
                            if int(msg3.content)>6:
                                await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                break
                            else:
                                await ctx.send(f"CricGo plays: {CricGo}")  
                                if (CricGo == int(msg3.content)):
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"Your total runs = {total}")
                                    break
                                total = total + int(msg3.content)          
                        await ctx.send(f'Target for CricGo is {total+1}')
                        await ctx.send('It is CricGos time to bat.')
                        ctotal = 0
                        while (True):
                            while(ctotal<total):                
                                #cmatch = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Input Your Ball:')
                                msg4 = await bot.wait_for("message", check=check4)
                                if int(msg4.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")
                                ctotal = ctotal + CricGo       
                                if (CricGo == int(msg4.content)):
                                    ctotal = ctotal - CricGo 
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"CricGo's total runs = {ctotal}")
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!')
                                break                      
                    elif msg2.content.lower() == 'bowl' :
                        await ctx.send('CricGos is going to bat.')
                        ctotal = 0
                        while (True):
                            #cmatch = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Input Your Ball:')
                            msg4 = await bot.wait_for("message", check=check4)
                            if int(msg4.content)>6:
                                print('You arent allowed to play any number more than 6.The game will restart now')
                                break
                            await ctx.send(f"CricGo plays: {CricGo}")
                                        
                            if (CricGo == int(msg4.content)):
                                await ctx.send("Number Matched! ..out!!!")
                                await ctx.send(f"CricGo's total runs ={ctotal}")
                                break
                            ctotal = ctotal + CricGo
                        await ctx.send(f'Your Target is {ctotal+1}')
                        await ctx.send('The CricGo is bowling')
                        total = 0
                        while (True):
                            while(total<ctotal):
                                match = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Play Your Shot:')
                                msg3 = await bot.wait_for("message", check=check3)
                                if int(msg3.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6.The game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")   
                                total = total + int(msg3.content)
                                if (CricGo ==int(msg3.content)):
                                    total = total - int(msg3.content)
                                    await ctx.send("Number Matched! ..out!!!")
                                    await ctx.send(f"Your total runs ={total}")    
                                    break
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!')                   
                else:
                    await ctx.send('CricGo has Won the Toss')
                    x=random.choice(['bat','bowl'])
                    if x=='bat':
                        await ctx.send('CricGos is going to bat.')
                        ctotal = 0
                        while (True):
                            #cmatch = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Input Your Ball:')
                            msg4 = await bot.wait_for("message", check=check4)
                            if int(msg4.content)>6:
                                print('You arent allowed to play any number more than 6.The game will restart now')
                                break
                            await ctx.send(f"CricGo plays: {CricGo}")
                                        
                            if (CricGo == int(msg4.content)):
                                await ctx.send("Number Matched! ..out!!!")
                                await ctx.send(f"CricGo's total runs ={ctotal}")
                                break
                            ctotal = ctotal + CricGo
                        await ctx.send(f'Your Target is {ctotal+1}')
                        await ctx.send('The CricGo is bowling')
                        total = 0
                        while (True):
                            while(total<ctotal):
                                match = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Play Your Shot:')
                                msg3 = await bot.wait_for("message", check=check3)
                                if int(msg3.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6.The game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")   
                                total = total + int(msg3.content)
                                if (CricGo ==int(msg3.content)):
                                    total = total - int(msg3.content)
                                    await ctx.send("Number Matched! ..out!!!")
                                    await ctx.send(f"Your total runs ={total}")    
                                    break
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!')
                    elif x=='bowl':
                        await ctx.send('CricGo is going to bowl')
                        total = 0
                        while (True):
                            #match = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Play Your Shot:')
                            msg3 = await bot.wait_for("message", check=check3)
                            if int(msg3.content)>6:
                                await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                break
                            else:
                                await ctx.send(f"CricGo plays: {CricGo}")  
                                if (CricGo == int(msg3.content)):
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"Your total runs = {total}")
                                    break
                                total = total + int(msg3.content)          
                        await ctx.send(f'Target for CricGo is {total+1}')
                        await ctx.send('It is CricGos time to bat.')
                        ctotal = 0
                        while (True):
                            while(ctotal<total):                
                                #cmatch = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Input Your Ball:')
                                msg4 = await bot.wait_for("message", check=check4)
                                if int(msg4.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")
                                ctotal = ctotal + CricGo       
                                if (CricGo == int(msg4.content)):
                                    ctotal = ctotal - CricGo 
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"CricGo's total runs = {ctotal}")
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!')
                                break 

            elif msg.content.lower() =='odd':
                if((int(msg1.content)+z)%2)==0:
                    y=random.choice(['bat','bowl'])
                    if y=='bat':
                        await ctx.send('CricGos is going to bat.')
                        ctotal = 0
                        while (True):
                            #cmatch = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Input Your Ball:')
                            msg4 = await bot.wait_for("message", check=check4)
                            if int(msg4.content)>6:
                                print('You arent allowed to play any number more than 6.The game will restart now')
                                break
                            await ctx.send(f"CricGo plays: {CricGo}")
                                        
                            if (CricGo == int(msg4.content)):
                                await ctx.send("Number Matched! ..out!!!")
                                await ctx.send(f"CricGo's total runs ={ctotal}")
                                break
                            ctotal = ctotal + CricGo
                        await ctx.send(f'Your Target is {ctotal+1}')
                        await ctx.send('The CricGo is bowling')
                        total = 0
                        while (True):
                            while(total<ctotal):
                                match = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Play Your Shot:')
                                msg3 = await bot.wait_for("message", check=check3)
                                if int(msg3.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6.The game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")   
                                total = total + int(msg3.content)
                                if (CricGo ==int(msg3.content)):
                                    total = total - int(msg3.content)
                                    await ctx.send("Number Matched! ..out!!!")
                                    await ctx.send(f"Your total runs ={total}")    
                                    break
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!')                    
                    elif y=='bowl':
                        await ctx.send('CricGo is going to bowl')
                        total = 0
                        while (True):
                            #match = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Play Your Shot:')
                            msg3 = await bot.wait_for("message", check=check3)
                            if int(msg3.content)>6:
                                await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                break
                            else:
                                await ctx.send(f"CricGo plays: {CricGo}")  
                                if (CricGo == int(msg3.content)):
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"Your total runs = {total}")
                                    break
                                total = total + int(msg3.content)          
                        await ctx.send(f'Target for CricGo is {total+1}')
                        await ctx.send('It is CricGos time to bat.')
                        ctotal = 0
                        while (True):
                            while(ctotal<total):                
                                #cmatch = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Input Your Ball:')
                                msg4 = await bot.wait_for("message", check=check4)
                                if int(msg4.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")
                                ctotal = ctotal + CricGo       
                                if (CricGo == int(msg4.content)):
                                    ctotal = ctotal - CricGo 
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"CricGo's total runs = {ctotal}")
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!')
                                break                        
                else:
                    await ctx.send('You have Won the Toss')
                    await ctx.send('What Do You Opt?(bat/bowl)')
                    msg2 = await bot.wait_for("message", check=check2)
                    if msg2.content.lower() == 'bat':
                        await ctx.send('CricGo is going to bowl')
                        total = 0
                        while (True):
                            #match = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Play Your Shot:')
                            msg3 = await bot.wait_for("message", check=check3)
                            if int(msg3.content)>6:
                                await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                break
                            else:
                                await ctx.send(f"CricGo plays: {CricGo}")  
                                if (CricGo == int(msg3.content)):
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"Your total runs = {total}")
                                    break
                                total = total + int(msg3.content)          
                        await ctx.send(f'Target for CricGo is {total+1}')
                        await ctx.send('It is CricGos time to bat.')
                        ctotal = 0
                        while (True):
                            while(ctotal<total):                
                                #cmatch = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Input Your Ball:')
                                msg4 = await bot.wait_for("message", check=check4)
                                if int(msg4.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")
                                ctotal = ctotal + CricGo       
                                if (CricGo == int(msg4.content)):
                                    ctotal = ctotal - CricGo 
                                    await ctx.send("GOTCHA! Number Matched! ...your out!!!")
                                    await ctx.send(f"CricGo's total runs = {ctotal}")
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!')
                                break 
                    elif msg2.content.lower() == 'bowl':
                        await ctx.send('CricGos is going to bat.')
                        ctotal = 0
                        while (True):
                            #cmatch = random.randint(1, 6)
                            CricGo = random.randint(1, 6)
                            await ctx.send('Input Your Ball:')
                            msg4 = await bot.wait_for("message", check=check4)
                            if int(msg4.content)>6:
                                print('You arent allowed to play any number more than 6.The game will restart now')
                                break
                            await ctx.send(f"CricGo plays: {CricGo}")
                                        
                            if (CricGo == int(msg4.content)):
                                await ctx.send("Number Matched! ..out!!!")
                                await ctx.send(f"CricGo's total runs ={ctotal}")
                                break
                            ctotal = ctotal + CricGo
                        await ctx.send(f'Your Target is {ctotal+1}')
                        await ctx.send('The CricGo is bowling')
                        total = 0
                        while (True):
                            while(total<ctotal):
                                match = random.randint(1, 6)
                                CricGo = random.randint(1, 6)
                                await ctx.send('Play Your Shot:')
                                msg3 = await bot.wait_for("message", check=check3)
                                if int(msg3.content)>6:
                                    await ctx.send('You arent allowed to play any number more than 6.The game will restart now')
                                    break
                                await ctx.send(f"CricGo plays: {CricGo}")   
                                total = total + int(msg3.content)
                                if (CricGo ==int(msg3.content)):
                                    total = total - int(msg3.content)
                                    await ctx.send("Number Matched! ..out!!!")
                                    await ctx.send(f"Your total runs ={total}")    
                                    break
                            if ctotal>total:
                                await ctx.send('Yayyyy! You lose!')
                                break
                            elif total>ctotal:
                                await ctx.send('Congoo You Win!')
                                await ctx.send(f'Well Played {str(ctx.message.author)[:-5]}')
                                break
                            else:
                                await ctx.send('And its a Tie!') 
                    else:
                        print('Invalid input! The game will restart')
            else:
                await ctx.send("Invalid Input")

def check(msg):
        return msg.content.lower() in ["odd", "eve"]

def check1(msg1):
    return int(msg1.content) in [1, 2]

def check2(msg2):
    return msg2.content.lower() in ["bat", "bowl"]

def check3(msg3):
    return int(msg3.content) in [1,2,3,4,5,6]

def check4(msg4):
    return int(msg4.content) in [1,2,3,4,5,6]

keep_alive()
bot.run(os.environ['TOKEN'])