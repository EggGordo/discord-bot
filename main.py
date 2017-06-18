import discord
from discord.ext import commands
import random
import sys

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='$', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def roll(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        number = random.randint(1, 20)

    await bot.say('{0.mention}'.format(member) + ' ' + str(number))
    
@bot.command(pass_context = True)
async def smug(ctx):
    """posts smug anime girls"""
    await bot.send_file(ctx.message.channel, 'smug.jpg')

token_file = open("token",'r')
token = token_file.read().replace("\n", "")
bot.run(token)
