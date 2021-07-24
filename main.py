import os
import discord
import asyncio
import datetime
from web import keep_alive
import requests
from discord.ext import tasks
import urllib
import bs4
from discord_components import DiscordComponents, Button, Select, SelectOption


global rawdata
global fetch

sonline = "Online <a:me_online:866963598550237224> "
soffline = " Offline <a:me_error:866963598031061024> "
smaint = "Maintenance <a:me_settings:866963612915204106> "

def scrap(url):
		try:
				weresponse = requests.get(url)
		except:
			print("fetch errrrrr")
		print(weresponse)
		a = "html.parser"
		wesoup = bs4.BeautifulSoup(weresponse.text, a)
		sdic = {"up24":"NA", "up7":"NA", "up30":"NA", "upt":"NA", "pnyc":"NA", "psg":"NA", "psyd":"NA", "pmum":"NA", "status":"NA"}
		weline_count = 1
		for weone_a_tag in wesoup.findAll('td'):
				try:
						if weline_count == 12:
								weraw1 = str(weone_a_tag)
								weup24 = weraw1.split(">")[2]
								weup24 = weup24.split("<")[0]
								sdic["up24"] = weup24

						if weline_count == 14:
								weraw1 = str(weone_a_tag)
								weup7 = weraw1.split(">")[2]
								weup7 = weup7.split("<")[0]
								sdic["up7"] = weup7
						
						if weline_count == 16:
								weraw1 = str(weone_a_tag)
								weup30 = weraw1.split(">")[2]
								weup30 = weup30.split("<")[0]
								sdic["up30"] = weup30

						if weline_count == 20:
								weraw1 = str(weone_a_tag)
								weupt = weraw1.split(">")[2]
								weupt = weupt.split("<")[0]
								sdic["upt"] = weupt
							
						if weline_count == 23:
								weraw1 = str(weone_a_tag)
								weuppnyc = weraw1.split(">")[1]
								weuppnyc = weuppnyc.split("<")[0]
								sdic["pnyc"] = weuppnyc

						if weline_count == 27:
								weraw1 = str(weone_a_tag)
								weuppsg = weraw1.split(">")[1]
								weuppsg = weuppsg.split("<")[0]
								sdic["psg"] = weuppsg

						if weline_count == 31:
								weraw1 = str(weone_a_tag)
								weuppsyd = weraw1.split(">")[1]
								weuppsyd = weuppsyd.split("<")[0]
								sdic["psyd"] = weuppsyd

						if weline_count == 35:
								weraw1 = str(weone_a_tag)
								weuppmum = weraw1.split(">")[1]
								weuppmum = weuppmum.split("<")[0]
								sdic["pmum"] = weuppmum
						weline_count += 1
				except Exception as e:
						print(e)

		weloine_count = 1
		for wetwo_a_tag in wesoup.findAll('div'):
				try:
					if weloine_count == 21:
							weraw2 = str(wetwo_a_tag)
							if weraw2 == "<div class=\"number\">Online</div>":
									wests = sonline
							else:
									wests = soffline
							sdic["status"] = wests
					weloine_count += 1
				except Exception as e:
						print(e)
		return sdic

async def updatestuff():
		fl = open("channel.vig", "r")
		dota = fl.read()
		fl.close()
		dota = dota.split(".")
		choon = dota[0]
		ceen = dota[1]
		chon = await client.fetch_channel(int(choon))
		msg = await chon.fetch_message(int(ceen))
		stsmbd = discord.Embed(title="Status Report", color=0x1FFFF5)
		raa = scrap("https://wl.hetrixtools.com/report/uptime/47e8a61e7d65302fad492608a982e676/")
		stsmbd = discord.Embed(title="Status Report")
		esstatus = raa["status"]
		espnyc = raa["pnyc"]
		espmum = raa["pmum"]
		espsg = raa["psg"]
		espsyd = raa["psyd"]
		esup = raa["upt"]
		es30 = raa["up30"]
		es7 = raa["up7"]
		es24 = raa["up24"]
		raa = scrap("https://wl.hetrixtools.com/report/uptime/a10f2995a8d6746b751c3eec4612ea0a/")
		sgstatus = raa["status"]
		sgpnyc = raa["pnyc"]
		sgpmum = raa["pmum"]
		sgpsg = raa["psg"]
		sgpsyd = raa["psyd"]
		sgup = raa["upt"]
		sg30 = raa["up30"]
		sg7 = raa["up7"]
		sg24 = raa["up24"]
		raa = scrap("https://wl.hetrixtools.com/report/uptime/95302d4250a008ed494a20e857366c12/")
		stsmbd = discord.Embed(title="Status Report")
		pastatus = raa["status"]
		papnyc = raa["pnyc"]
		papmum = raa["pmum"]
		papsg = raa["psg"]
		papsyd = raa["psyd"]
		paup = raa["upt"]
		pa30 = raa["up30"]
		pa7 = raa["up7"]
		pa24 = raa["up24"]
		raa = scrap("https://wl.hetrixtools.com/report/uptime/35527114d18df6211fdf8ba0c0314c12/")
		webstatus = raa["status"]
		webpnyc = raa["pnyc"]
		webpmum = raa["pmum"]
		webpsg = raa["psg"]
		webpsyd = raa["psyd"]
		webup = raa["upt"]
		web30 = raa["up30"]
		web7 = raa["up7"]
		web24 = raa["up24"]
		wststatus = raa["status"]
		wstpnyc = raa["pnyc"]
		wstpmum = raa["pmum"]
		wstpsg = raa["psg"]
		wstpsyd = raa["psyd"]
		wstup = raa["upt"]
		wst30 = raa["up30"]
		wst7 = raa["up7"]
		wst24 = raa["up24"]
		stsmbd.add_field(name="SG1", value=f"Status: {sgstatus}\nMumbai: {sgpmum}\nSingapore: {sgpsg}\nSydney: {sgpsyd}\nNewYork: {sgpnyc}\nUptime:\nTotal: {sgup}\nLast 24h: {sg24}\nLast 7d: {sg7}\nLast 30d: {sg30}")
		stsmbd.add_field(name="\u200B", value="\u200B")
		stsmbd.add_field(name="ES1", value=f"Status: {esstatus}\nMumbai: {espmum}\nSingapore: {espsg}\nSydney: {espsyd}\nNewYork: {espnyc}\nUptime:\nTotal: {esup}\nLast 24h: {es24}\nLast 7d: {es7}\nLast 30d: {es30}")
		stsmbd.add_field(name="Panel", value=f"Status: {pastatus}\nMumbai: {papmum}\nSingapore: {papsg}\nSydney: {papsyd}\nNewYork: {papnyc}\nUptime:\nTotal: {paup}\nLast 24h: {pa24}\nLast 7d: {pa7}\nLast 30d: {pa30}")
		stsmbd.add_field(name="\u200B", value="\u200B")
		stsmbd.add_field(name="WebPanel", value=f"Status: {webstatus}\nMumbai: {webpmum}\nSingapore: {webpsg}\nSydney: {webpsyd}\nNewYork: {webpnyc}\nUptime:\nTotal: {webup}\nLast 24h: {web24}\nLast 7d: {web7}\nLast 30d: {web30}")
		stsmbd.set_image(url="https://tavignesh.github.io/imhost/location.png")
		stsmbd.set_footer(text="Refreshed Every 2min.. \u200b MEhost", icon_url="https://cdn.discordapp.com/attachments/853194197523496981/866916055737827338/fe392ecc9da74d37f7e2b116c9094988.webp")
		#await stsmsg.edit(embed=stsmbd)
		await msg.edit(embed=stsmbd)

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@tasks.loop(seconds=30)
async def my_loop():
	await updatestuff()

@client.event
async def on_ready():
	DiscordComponents(client)
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MEhost"))
	game = discord.Game("MEhost")
	print("{} is ONLINE!!".format(client.user))
	chon = await client.fetch_channel(868381180469317713)
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
		wlcmbd = discord.Embed(title=f"hmm", color=discord.Colour.random(), timestamp=datetime.datetime.utcnow())
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

	if message.content == "me/get1":
		cf = open("channel.vig", "r")
		rawid = cf.readline()
		cf.close()
		ids = rawid.split(".")
		msgid = ids[1]
		chanid = ids[0]
		chan = client.get_channel(int(chanid))
		msg = await chan.fetch_message(int(msgid))
		print(msg.content)

	if message.content == "me/first":
		acd = await message.channel.send("click fast",components = [Button(label = "button!", disabled=False, style=5, url="https://asteroidbot.xyz")])
		interaction = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("button"))
		await acd.edit(f"{interaction.author}",components = [Button(label = "hmm", disabled=True)])
		await interaction.respond(content = f"{interaction.author} clicked first!!")

	if message.content == "me/set":
		if int(message.author.id) in [641305773095387156, 420839496263925767]:
			data = message.content.split("=")[-1]
			try:
				fl = open("channel.vig", "w")
				fl.write(data)
				fl.close()
				await message.channel.send("done")
			except:
				await message.channel.send("error occured")
				fl.close()


	if message.content == "me/get":
		stsmsg = await message.channel.send(embed=discord.Embed(title="Loading..."))
		stsmbd = discord.Embed(title="Status Report")
		raa = scrap("https://wl.hetrixtools.com/report/uptime/47e8a61e7d65302fad492608a982e676/")
		stsmbd = discord.Embed(title="Status Report")
		esstatus = raa["status"]
		espnyc = raa["pnyc"]
		espmum = raa["pmum"]
		espsg = raa["psg"]
		espsyd = raa["psyd"]
		esup = raa["upt"]
		es30 = raa["up30"]
		es7 = raa["up7"]
		es24 = raa["up24"]
		raa = scrap("https://wl.hetrixtools.com/report/uptime/a10f2995a8d6746b751c3eec4612ea0a/")
		sgstatus = raa["status"]
		sgpnyc = raa["pnyc"]
		sgpmum = raa["pmum"]
		sgpsg = raa["psg"]
		sgpsyd = raa["psyd"]
		sgup = raa["upt"]
		sg30 = raa["up30"]
		sg7 = raa["up7"]
		sg24 = raa["up24"]
		raa = scrap("https://wl.hetrixtools.com/report/uptime/95302d4250a008ed494a20e857366c12/")
		stsmbd = discord.Embed(title="Status Report")
		pastatus = raa["status"]
		papnyc = raa["pnyc"]
		papmum = raa["pmum"]
		papsg = raa["psg"]
		papsyd = raa["psyd"]
		paup = raa["upt"]
		pa30 = raa["up30"]
		pa7 = raa["up7"]
		pa24 = raa["up24"]
		raa = scrap("https://wl.hetrixtools.com/report/uptime/35527114d18df6211fdf8ba0c0314c12/")
		webstatus = raa["status"]
		webpnyc = raa["pnyc"]
		webpmum = raa["pmum"]
		webpsg = raa["psg"]
		webpsyd = raa["psyd"]
		webup = raa["upt"]
		web30 = raa["up30"]
		web7 = raa["up7"]
		web24 = raa["up24"]
		wststatus = raa["status"]
		wstpnyc = raa["pnyc"]
		wstpmum = raa["pmum"]
		wstpsg = raa["psg"]
		wstpsyd = raa["psyd"]
		wstup = raa["upt"]
		wst30 = raa["up30"]
		wst7 = raa["up7"]
		wst24 = raa["up24"]
		stsmbd.add_field(name="SG1", value=f"Status: {sgstatus}\nMumbai: {sgpmum}\nSingapore: {sgpsg}\nSydney: {sgpsyd}\nNewYork: {sgpnyc}\nUptime:\nTotal: {sgup}\nLast 24h: {sg24}\nLast 7d: {sg7}\nLast 30d: {sg30}")
		stsmbd.add_field(name="\u200B", value="\u200B")
		stsmbd.add_field(name="ES1", value=f"Status: {esstatus}\nMumbai: {espmum}\nSingapore: {espsg}\nSydney: {espsyd}\nNewYork: {espnyc}\nUptime:\nTotal: {esup}\nLast 24h: {es24}\nLast 7d: {es7}\nLast 30d: {es30}")
		stsmbd.add_field(name="Panel", value=f"Status: {pastatus}\nMumbai: {papmum}\nSingapore: {papsg}\nSydney: {papsyd}\nNewYork: {papnyc}\nUptime:\nTotal: {paup}\nLast 24h: {pa24}\nLast 7d: {pa7}\nLast 30d: {pa30}")
		stsmbd.add_field(name="\u200B", value="\u200B")
		stsmbd.add_field(name="WebPanel", value=f"Status: {webstatus}\nMumbai: {webpmum}\nSingapore: {webpsg}\nSydney: {webpsyd}\nNewYork: {webpnyc}\nUptime:\nTotal: {webup}\nLast 24h: {web24}\nLast 7d: {web7}\nLast 30d: {web30}")
		stsmbd.set_image(url="https://tavignesh.github.io/imhost/location.png")
		stsmbd.set_footer(text="Refreshed Every 2min.. \u200b MEhost", icon_url="https://cdn.discordapp.com/attachments/853194197523496981/866916055737827338/fe392ecc9da74d37f7e2b116c9094988.webp")
		await stsmsg.edit(embed=stsmbd)
				
keep_alive()
my_loop.start()
my_secret = os.environ['bottoken']
client.run(my_secret)








