import bs4
import urllib
import requests

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

try:
	a = scrap('https://wl.hetrixtools.com/report/uptime/ac11a563e80a1698e6085ea4822c12f4/')
	print(a)
except Exception as e:
	print(e)
