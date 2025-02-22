#This bot was made all in python
#Comands are ?ban ?warn ?cute
#?Ban bans the person ; ?cute says a cute message ; ?warn warns the user in the dms
#Portuguese Dev so somethings are in Portuguese

import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True  # This is necessary for banning members

bot = commands.Bot(command_prefix='?', intents=intents)

# Cute messages
cute_messages = [
    "You're as cute as a cat sleeping in the sun! 😻",
    "You're my favorite person in the world! 💖",
    "You make my heart go *doki doki*! 💓",
    "I want to hug you forever! 🥰",
    "You're sweeter than the sweetest candy! 🍬"
]

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} was banned from the server! 🚫')

@bot.command()
async def warn(ctx, member: discord.Member):
    try:
        await member.send("⚠️ You got Warned for bad behavior! We apeal for you to change your Behavior this might lead to a ban 🛑!")
        await ctx.send(f'{member.mention} foi avisado por DM.')
    except discord.Forbidden:
        await ctx.send("The user has the dms deactivated and I couldnt send the message!")

@bot.command()
async def cute(ctx):
    message = random.choice(cute_messages)
    await ctx.send(message)

# Substitute this for your bots token
bot.run('Your Bots Token Goes here')

#Credits @qwx3yxlzywjiyw5kb25lza
