# Valar-Downloadis 

<b><i><h2>All men must download!</h2></i></b>

This is something that I really wanted to code for a long time. Always had trouble downloading videos from Youtube and specially downloading those Youtube playlists. Well not anymore!<br />

This is a python script which lets you download YouTube Playlists or seperate YouTube videos easily!.

<b><h3>Requirements:</h3></b> <br />
1. You must have Python installed. Version 2.7.6 is recommended for running this script. Check by running command "python -V" on your terminal.<br />
2. You must install the BeautifulSoup4 module. This link may be helpful incase you don't have it installed already https://beautiful-soup-4.readthedocs.org/en/latest/ or Type "sudo pip3 install bs4"(for Python version 2.7.6 if you still have not installed BeautifulSoup4 module.<br />
3. You must install the 'dryscrape' module. Please follow the steps below:
  <li>Navigate to the required folder in your terminal screen. Type- </li><br />
  <li>git clone https://github.com/niklasb/dryscrape.git dryscrape</li> <br />
  <li>cd dryscrape</li> <br />
  <li>sudo pip3 install -r requirements.txt</li> <br />
  <li>pip3 setup.py install</li> <br />

<b><h3>How to use:</h3></b> <br />
1. Navigate to the required folder in your terminal screen. <br />
2. Type "python3 valardownloadis.py" <br />
3. You'll get an option:<br /> 
<i>Press 'P' to download a playlist.</i><br />
<i>Press 'V' to download a single video.</i><br />
4. Choose one of the following.<br /><li>If you want to download the playlist, you need to provide the url(for eg - https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDi9F_slcQK7knjtO8TUvUs)</li><br /><li>If you want to download a video, you just need to enter the name of the video.</li><br />
5. If you choose option 1(i.e. Downloading a YouTube playlist), you'll be asked to confirm the playlist by checking the title, author, views and no. of videos displayed on the terminal.<br />
6. If you choose option 2(i.e. Downloading a single video), you'll be asked to choose between different video formats available(720p, 360p, etc)<br />
7. Viola downloading starts. <i>Valar Downloadis!</i> <br />

Suggestions are most welcome. You can contact me at kushagrasahu.ed@gmail.com </br>

#Screenshots

This is the terminal where code is being executed.

![valarscreenshotgh](https://cloud.githubusercontent.com/assets/16977717/16316529/a08a71d4-39a4-11e6-8ae8-1ab63f8dd7ad.png)

Also added a new feature: To choose specific videos of the playlist by their index no.s!

![valar3](https://cloud.githubusercontent.com/assets/16977717/16336899/ccc3b794-3a2e-11e6-8337-54d3226132e8.png)

Voila!

![v1](https://cloud.githubusercontent.com/assets/16977717/16337972/160b5b48-3a37-11e6-9edc-15e5edf3c72f.png)


<b>Will be creating a web app based on this script having some more functionalities ;) </b>

