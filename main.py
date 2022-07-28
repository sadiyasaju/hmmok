import os
import httpx
import requests
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot 


os.system('pip install jishaku')
import jishaku
import discord 
import sys
os.system('clear')


p = ["", "_"]
TOKEN = os.environ['tkn']
modsrole = 998879484642074644
boostersid = 982662248097009815



intents = discord.Intents.all()
intents.members = True
intents.messages = True
headers = {'Authorization': f'Bot {TOKEN}'}
client = Bot(command_prefix=p, case_insensitive=True, intents = intents)
client.load_extension('jishaku')
fansrole = 982730330060501042
wallrole = 982730306467528714
power = 987687884150693888
vanitycode = "rntop"
guildname = "RAINITE ORG"
client.remove_command('help')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle)
print("Bot is ready!")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"<:icons_Wrong:1001466680880410644> | **{ctx.message.author.name}#{ctx.author.discriminator}** You are on cooldown. Try again in {round(error.retry_after, 2)}s", delete_after=10)

@client.command(name='ping')
async def ping(ctx):
     await ctx.reply(f'Ping -** {round(client.latency * 1000)}ms!**')



@client.command(aliases=["screenshot"])
@commands.cooldown(1, 20, commands.BucketType.user)
async def ss(ctx, *, ssig):
  
  idk = ctx.message.content.lower()
  if "porn" in idk or "sex" in idk or "xx" in idk or "xham" in idk or "hellmom" in idk or "xvid" in idk or "shameless" in idk or "miakhal" in idk or "cum" in idk or "orgasm" in idk or "xvid" in idk or "slut" in idk or "naked" in idk or "brazzers" in idk or "nig" in idk or "slut" in idk or "horny" in idk or "fuck" in idk or "pussy" in idk or "xhmaster" in idk or "redtube" in idk:
     await ctx.reply("<a:Rogue_Tom_Tharki:1001405238886027265>", mention_author=True)
  elif "bit.ly" in idk or "shorturl" in idk or "cutt.ly" in idk:
     await ctx.reply("url shorteners aren't allowed.", mention_author=True, delete_after=10)
  elif "https" in idk or "http" in idk:
     embed = discord.Embed(title=f"assistant", color=000000)
     embed.set_footer(text="Screenshot")
     embed.set_image(url=f"https://image.thum.io/get/{ssig}")
     await ctx.reply(embed=embed, mention_author=False)
  else:
     embed = discord.Embed(title=f"assistant", color=000000)
     embed.set_footer(text="Screenshot")
     embed.set_image(url=f"https://image.thum.io/get/https://{ssig}")
     await ctx.reply(embed=embed, mention_author=False, delete_after=18000)

def restart_bot(): 
 os.execv(sys.executable, ['python'] + sys.argv)

@client.command(name='restart')
@commands.is_owner()
async def restart(ctx):
 await ctx.reply("**restarting....**")
 restart_bot()
 await ctx.reply("**restarted**")
  
@client.command(name='roleall')
async def roleall(ctx, *reason):
    embed=discord.Embed(description=f"Adding <@&{wallrole}> and <@&{fansrole}> to Everyone")
    responsible = f"Role All - Done By {ctx.message.author.name}#{ctx.author.discriminator}"
  #  role = discord.utils.get(ctx.guild.roles, id=wallrole)
    role = discord.utils.get(ctx.guild.roles, id=fansrole) and discord.utils.get(ctx.guild.roles, id=wallrole)
    mem = await ctx.guild.chunk()
    membercount = 0
    pr = ctx.guild.get_role(power)
    if pr in ctx.message.author.roles:
      await ctx.reply(f"adding <@&{fansrole}> & <@&{wallrole}> to everyone....", allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
      for user in mem:
          if role in user.roles:
              continue
          else:
              membercount += 1
              try:          
                  #await ctx.reply(f"Adding / and FANS™ to {membercount} members.")
                  await user.add_roles(role, reason=responsible)
                 # await user.add_roles(rolee, reason=responsible)
              except: 
                  pass
      if membercount == 0:
      	return await ctx.reply(f"Everyone already has role.", allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
      await ctx.reply(f"<:verified:1001419887022972970> | Successfully added <@&{fansrole}> & <@&{wallrole}> to {membercount} members.", allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, replied_user=False))
      return
    else:
     await      ctx.reply("unauthorized", mention_author=False, delete_after=3)    

      
@client.command(aliases=["h"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def help(ctx):
  
  embed = discord.Embed(title= "Prefix: `_`", description=f'''<a:blackdot:1001456394672812112> screenshot
`alias - ss`
<a:blackdot:1001456394672812112> roleall
`adds wall & Family to everyone.`
<a:blackdot:1001456394672812112> ping
`shows bot's latency.`
<a:blackdot:1001456394672812112> restart
`owner only command.`
<a:blackdot:1001456394672812112> jishaku
`owner only command.`
''', color=000000)
  embed.set_author(name=f"{guildname}")
  embed.set_footer(text=f"/{vanitycode} | cmds", icon_url=ctx.guild.icon_url)
 # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  #embed.add_field(name="<:spy_announcements:894201296700211290>Botinfo", value='```"shows info about the bot"```', inline=False)
  await ctx.reply(embed=embed, mention_author=False)

@client.command(name='gay')
async def gay(ctx):
 await ctx.reply("<@770950083613032519> is gay")


@client.command(name='lesbian')
async def lesbian(ctx):
	await ctx.reply("<@942365653116002344> is lesbian")					
client.run(TOKEN)