import requests
import webbrowser
import re
import dryscrape
from bs4 import BeautifulSoup

base_yt_url = 'https://www.youtube.com/results?search_query='
base_ss_url = 'https://www.ssyoutube.com'

while True:
	abort = False
	print("Enter name of the song!")
	search_input = input()
	search_split = search_input.split()
	search=""
	for word in search_split:
		search += word + "+"
	search = search[:-1]
	search_url = base_yt_url + search
	session1 = dryscrape.Session()
	session1.visit(search_url)
	response=session1.body()
	soup = BeautifulSoup(response,"lxml")
	list_results = soup.find('div', {'id': 'results'}).find('ol',{'class':'section-list'}).find('ol',{'class':'item-section'}).findAll('li')
	for result in list_results:
		if result.find('div', {'class': 'pyv-afc-ads-container'}):
			continue
		else:
			watch_result = result.find('div', {'class': "yt-lockup-content"})
			break
	video_views = watch_result.find('ul', {'class': 'yt-lockup-meta-info'}).findAll('li')[1].text
	video_views = video_views.split()[0]
	watch_url = watch_result.find('h3', {'class': 'yt-lockup-title'}).find('a')['href']
	download_url = base_ss_url + watch_url
	session2 = dryscrape.Session()
	session2.visit(download_url)
	response=session2.body()
	soup = BeautifulSoup(response,"lxml")
	sf_result = soup.find('div', {'class':'wrapper'}).find('div', {'class':'downloader-2'}).find('div',{'id':'sf_result'})
	media_result = sf_result.find('div', {'class':'media-result'})
	info_box = media_result.find('div', {'class': 'info-box'})
	dropdown_box_list = info_box.find('div', {'class': 'link-box'}).find('div', {'class': 'drop-down-box'}).find('div', {'class': 'list'}).find('div', {'class': 'links'})
	download_link_groups = dropdown_box_list.findAll('div', {'class': 'link-group'})
	i=0
	list_links = []
	for group in download_link_groups:
		download_links = group.findAll('a')
		for link in download_links:
			download = str(link['download'])
			extension = re.split(r'\.(?!\d)', download)[-1]
			class_link = link['class']
			if class_link[0] != "no-audio":
				if extension == "mp4":
					i+=1
					video_format = link['title']
					list_links.append(link)
					print(str(i) + ". " + download + ", " + str(video_format) + ", Youtube Views: " + video_views)

	print("Select your choice for the download. Enter any other number to abort this download!")
	choice = input()
	choice = int(choice)
	if choice > len(list_links) or choice <= 0:
		abort = True
	if not abort:
		to_download = list_links[choice-1]
		to_download_url = to_download['href']
		webbrowser.open_new(to_download_url)
	print("Do you wish to download more? Enter 'Y' for more and any other key to quit.")
	inp = input()
	if inp == 'y' or inp == 'Y':
		pass
	else:
		print("Thank You!")
		break





		



