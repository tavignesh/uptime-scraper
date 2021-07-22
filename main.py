import os
import discord
import asyncio
import datetime
from flask import Flask, request
from threading import Thread
import requests
from discord.ext import tasks
import urllib
import bs4

#API



global rawdata
global fetch

sonline = "Online <a:me_online:866963598550237224> "
soffline = " Offline <a:me_error:866963598031061024> "
smaint = "Maintenance <a:me_settings:866963612915204106> "

sg1sts = soffline
es1sts = soffline
mests = soffline
websts = soffline
pansts = soffline

def runserver():
		app = Flask('')
		@app.route('/post', methods=['POST'])
		def result():
				rawdata = (request.json)
				print(rawdata)
				if rawdata["monitor_name"] == "website":
					if rawdata["monitor_status"] == "online":
						mests = sonline
					else:
						mests = soffline
				elif rawdata["monitor_name"] == "sg1":
					if rawdata["monitor_status"] == "online":
						sg1sts = sonline
					else:
						sg1sts = soffline
				elif rawdata["monitor_name"] == "es1":
					if rawdata["monitor_status"] == "online":
						es1sts = sonline
					else:
						es1sts = soffline
				elif rawdata["monitor_name"] == "webpanel":
					if rawdata["monitor_status"] == "online":
						websts = sonline
					else:
						websts = soffline
				elif rawdata["monitor_name"] == "panel":
					if rawdata["monitor_status"] == "online":
						pansts = sonline
					else:
						pansts = soffline
				else:
					print("EROOOOROOOOORRRRRRRRRR")



				
				return 'Received !'

		@app.route('/')
		def home():
				return 'I\'m alive'


		def run():
			app.run(host='0.0.0.0',port=8080)

		def keep_alive():
				t = Thread(target=run)
				t.start()

		keep_alive()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

class AppURLopener(urllib.request.FancyURLopener):
  version = "Mozilla/5.0"
opener = AppURLopener()

@tasks.loop(seconds=60)
async def my_loop():
		pass

    

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MEhost"))
    game = discord.Game("MEhost")
    print("{} is ONLINE!!".format(client.user))
    chon = await client.fetch_channel(865099856828563467)
    await chon.send("||Online Again||")


@client.event
async def on_member_join(member):
    chan = await client.fetch_channel(862434490227621948)
    wlcmbd = discord.Embed(title=f"Welcome {member}", description=f"Welcome {member.mention} to MEhost. Please follow the rules found in <#853111090796036117>..\n\n**Usefull Links**\n\nWebsite → 『 https://mehost.me/ 』\nControl Panel → 『 https://panel.mehost.me/ 』\nWebpanel → 『 https://webpanel.mehost.me:2222/ 』\nBilling → 『 https://billing.mehost.me/ 』\nDocumentation → 『 https://docs.mehost.me/ 』", color=discord.Colour.random(), timestamp=datetime.datetime.utcnow())
    wlcmbd.set_thumbnail(url=member.avatar_url)
    wlcmbd.set_footer(text='MEhost \u200b',icon_url="https://tavignesh.github.io/imhost/meee.jpg")
    await chan.send(embed=wlcmbd)
		

@client.event
async def on_message(message):
	if message.content == "me/ test":
		member=message.author
		wlcmbd = discord.Embed(title=f"Welcome {member}", description=f"Welcome {member.mention} to MEhost. Please follow the rules found in <#853111090796036117>..\n\n**Usefull Links**\n\nWebsite → 『 https://mehost.me/ 』\nControl Panel → 『 https://panel.mehost.me/ 』\nWebpanel → 『 https://webpanel.mehost.me:2222/ 』\nBilling → 『 https://billing.mehost.me/ 』\nDocumentation → 『 https://docs.mehost.me/ 』", color=discord.Colour.random(), timestamp=datetime.datetime.utcnow())
		wlcmbd.set_thumbnail(url=member.avatar_url)
		wlcmbd.set_footer(text='MEhost \u200b',icon_url="https://tavignesh.github.io/imhost/meee.jpg")
		await message.channel.send(embed=wlcmbd)

	if int(message.channel.id) == 862663205850578945:
		if message.author.guild_permissions.administrator:
			pass
		else:
			sug = message.content
			await message.delete()
			sugmsg = await message.channel.send(embed=discord.Embed(title=f"{message.author}'s Suggestion", description=f"```yaml\n{sug}\n```"))
			await sugmsg.add_reaction("<:me_upvote:865116461902331915>")
			await sugmsg.add_reaction("<:me_downvote:865116461902331916>")

	if message.content == "me/set status":
		await message.channel.send(embed=discord.Embed(title="MEhost Status", description=f"SG1 : "))
				
runserver()
my_loop.start()
my_secret = os.environ['bottoken']
client.run(my_secret)








