import requests
import webbrowser
import time
import re
import dryscrape
from bs4 import BeautifulSoup

base_yt_url = 'https://www.youtube.com/results?search_query='
base_ss_url = 'https://www.ssyoutube.com'

global flag_stay_video
global activate_playlist
global activate_video

activate_video = False
activate_playlist = False

def download(watch_url, views):
	global flag_stay_video
	abort = False
	download_url = base_ss_url + watch_url
	session2 = dryscrape.Session()
	session2.visit(download_url)
	response=session2.body()
	soup = BeautifulSoup(response,"lxml")
	sf_result = soup.find('div', {'class':'wrapper'}).find('div', {'class':'downloader-2'}).find('div',{'id':'sf_result'})
	
	while True:
		media_result = sf_result.find('div', {'class':'media-result'})
		if media_result != None:
			info_box = media_result.find('div', {'class': 'info-box'})
			break
		else:
			session2 = dryscrape.Session()
			session2.visit(download_url)
			response=session2.body()
			soup = BeautifulSoup(response,"lxml")
			sf_result = soup.find('div', {'class':'wrapper'}).find('div', {'class':'downloader-2'}).find('div',{'id':'sf_result'})
	
	dropdown_box_list = info_box.find('div', {'class': 'link-box'}).find('div', {'class': 'drop-down-box'}).find('div', {'class': 'list'}).find('div', {'class': 'links'})
	download_link_groups = dropdown_box_list.findAll('div', {'class': 'link-group'})
	
	if activate_video:
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
						print(str(i) + ". " + download + ", " + str(video_format) + ", Youtube Views: " + views)
		
		print("Select your choice for the download. Enter any other number to abort this download!")
		choice = input()
		choice = int(choice)
		if choice > len(list_links) or choice <= 0:
			abort = True
		if not abort:
			to_download = list_links[choice-1]
			to_download_url = to_download['href']
			webbrowser.open(to_download_url, new = 0, autoraise = True)
			print("Downloading ...")

		else:
			flag_stay_video = True
			print("Please be more specific in entering the name of the video")

	elif activate_playlist:
		link = download_link_groups[0].findAll('a')[0]
		download = link['download']
		video_format = link['title']
		to_download_url = link['href']
		print(download + ", " + str(video_format) + ", Playlist Views: " + views)
		webbrowser.open(to_download_url, new = 0, autoraise = True)
		print("Downloading ...")

def download_video():
	global activate_video
	global activate_playlist
	print("Enter name of the video.")
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
			while True:
				watch_result = result.find('div', {'class': "yt-lockup-content"})
				if watch_result != None:
					break
			break

	video_views = watch_result.find('ul', {'class': 'yt-lockup-meta-info'}).findAll('li')[1].text
	video_views = video_views.split()[0]
	watch_url = watch_result.find('h3', {'class': 'yt-lockup-title'}).find('a')['href']
	activate_playlist = False
	activate_video = True
	download(watch_url, video_views)

def download_playlist():
	global activate_video
	global activate_playlist
	list_watch_urls = []
	print("Please enter the exact url of the youtube playlist. For eg- 'https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBYxWxJtLi8c6PGjNKGYGZZ'")
	search_url = input()
	response = requests.get(search_url)
	soup = BeautifulSoup(response.text, 'lxml')
	content = soup.find('div',{'id': 'page-container'}).find('div',{'id': 'content'}).find('div',{'class': 'branded-page-v2-col-container'})
	inner_content = content.find('div',{'class': 'branded-page-v2-col-container-inner'}).find('div',{'class': 'branded-page-v2-primary-col'})
	header_content = inner_content.find('div',{'id': 'pl-header'}).find('div',{'class': 'pl-header-content'})
	playlist_title = header_content.find('h1',{'class': 'pl-header-title'}).text
	playlist_details = header_content.find('ul', {'class', 'pl-header-details'}).findAll('li')
	playlist_author = playlist_details[0].text
	playlist_video_count = int(playlist_details[1].text.split()[0])
	playlist_views = playlist_details[2].text.split()[0]
	print("Title:" + playlist_title)
	print("By: " + playlist_author)
	print("Total videos: " + str(playlist_video_count))
	print("Youtube Views: " + playlist_views)
	print("Is this your Playlist?\nEnter 'Y' for yes and any other key to disagree.")
	inp = input()
	
	if inp == 'y' or inp == 'Y':
		playlist_content = inner_content.find('ul', {'id': 'browse-items-primary'}).find('div', {'id': 'pl-video-list'}).find('tbody', {'id':'pl-load-more-destination'})
		print("To download all the videos, Press 'A'.\nTo download only the specific videos of the playlist, Press 'S'")
		list_videos = playlist_content.findAll('tr')
		while True:
			choice = input()
			if choice == 'A' or choice == 'a':
				break
			elif choice == 'S' or choice == 's':
				index = 1
				for tr in list_videos:

					video_title = tr.find('td', {'class': 'pl-video-title'}).find('a').text
					print(str(index) + '. ' + video_title)
					index += 1
				print("Enter the index no. of videos you want to download specifically from the playlist(preferred in increasing order). For eg - '1 4 5 7' or '2 6 3 11'")
				specific_videos = input()
				index_videos = list(map(int, specific_videos.split()))
				break

		index = 1
		for tr in list_videos:
			if index in index_videos:
				video = tr.find('td', {'class': 'pl-video-title'}).find('a')
				watch_url = video['href']
				list_watch_urls.append(watch_url)
			index += 1
		# To download only a subset of all the videos at a time, then to resume the download on user's input
		# print("I recommend you download only a set of videos at one time. Depending on your speed, please enter the number of videos you want to download at a time")
		# set_count = input()
		# j = 0
		# pause_download = False
		# activate_download = ''
		activate_video = False
		activate_playlist = True
		
		for url in list_watch_urls:
			download(url, playlist_views)
			# if j!=0 and j%set_count !=0:
			# 	download(url, playlist_views)
			# elif not j:
			# 	download(url, playlist_views)
			# elif j!=0 and j%set_count == 0:
			# 	print("Now you press key 'D' to download the next" + set_count + " videos once the previous 5 are completed.")				
			# Unless user does'nt press character 'D', next set of videos wont download!
			# 	while activate_download != 'D':
			# 		activate_download = input()

	else:
		print("Please check your url again. Thanks!")
		download_playlist()
		
def main():
	while True:
		global flag_stay_video
		flag_stay_video=False
		print("Press 'P' to download a playlist.\nPress 'V' to download a single video.")
		
		while True:
			choice = input()
			if choice == 'P' or choice == 'p':
				download_playlist()
				break
			elif choice == 'V' or choice == 'v':
				download_video()
				break
			else:
				print("Press 'P' to download a playlist.\nPress 'V' to download a single video.")
		
		if not flag_stay_video:
			time.sleep(5)
			print("Do you wish to download more?\nEnter 'Y' for more and any other key to quit.")
			inp = input()
			if inp == 'y' or inp == 'Y':
				pass
			else:
				print("Thank You!")
				break

#Calling main function.
if __name__ == "__main__":
	main()
