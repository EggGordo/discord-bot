import discord
from discord.ext import commands
import random
import sys
import re
import smug_anime
import music

description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""
bot = commands.Bot(command_prefix='#', description=description)
bot.add_cog(music.Music(bot))

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("Invite URL: https://discordapp.com/oauth2/authorize?client_id=" + bot.user.id + "&scope=bot")
    print("------")
    await bot.change_presence(game=discord.Game(name='github.com/GhostSquad57/discord-bot'))

@bot.command(pass_context = True)
async def roll(ctx, dice : str):
    """Rolls a dice in NdN+N format. Modifier can be omitted"""
    
    modifier = 0
    
    if dice.lower() == "help":
        await bot.say("The roll command takes an attribute in the NdN format where the first N is the number of dice thrown and the second the number of sides on the dice. An optional modifier can also be added with the + or - character and a number.")
        return
    try:
        rolls, limit, modifier = map(int, re.split("[d\+-]+", dice))
    except:
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await bot.say("Format has to be in NdN(+N)!")
            return
    
    if "-" in dice:
        modifier = -modifier

    result = ", ".join(str(random.randint(1, limit) + modifier) for r in range(rolls))
    await bot.say('{0.mention}'.format(ctx.message.author) + ' ' + result)

@bot.command(pass_context = True)
async def smug(ctx):
    """posts smug anime girls"""
    await bot.send_file(ctx.message.channel, "images/" + smug_anime.random_pick("images"))

@bot.command(pass_context = True)
async def insult(self, user : discord.Member):
    """insult bitches"""
    insult = ("You boob!",
         "They should call you wimp-lash!",
         "I could write a book about what you don't know!",
         "taps on head Just as I suspected - hollow!",
         "You metal munching moron!",
         "You overgrown alley cat!",
         "You pathetic pile of pitiful pinheads!",
         "You tin-tongued dolt!",
         "Bunglar!",
         "Dolt!",
         "Half wit!",
         "You couldn't even beat a motely group of gnomes!",
         "You flea-bitten fur brain!",
         "I'll cover my throne with your hide!"
        )
    await bot.say(user.mention + " " + random.choice(insult))

@bot.event
async def on_message(message):
    if message.content.startswith('OpenBSD'):
        await bot.add_reaction(message=message, emoji=':aids:326463585968455680')
    await bot.process_commands(message)

token_file = open("token")
token = token_file.read().replace('\n', '')
token_file.close()
bot.run(token)
