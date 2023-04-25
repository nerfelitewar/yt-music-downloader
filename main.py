import pyautogui as pg 
from colorama import Fore 
import os 
from googleapiclient.discovery import build
import youtube_dl
import sys 

start=pg.confirm("START",buttons=['YES','NO'],title="STARTING...")
if start=='YES':
    pass 
else:
    pg.alert("THANK YOU SEE YA LATER!")
    sys.exit(Fore.LIGHTMAGENTA_EX+"Program stopped by the user..."+Fore.RESET)

############################# MAIN CODE ###########################

path = 'YouTube_songs'
if not os.path.exists(path):
    os.mkdir(path)

key=pg.prompt("ENTER YOUR API KEY HERE",title="API KEY") 
if key=="":
    pg.alert("You cannot skip this part! Please RETRY",title='API ERROR')
else:
    pass 

print("API KEY- "+Fore.YELLOW+key+Fore.RESET)


playlist_id=pg.prompt("ENTER YOUR PUBLIC PLAYLIST LINK HERE",title="PLAYLIST ID")

def no_vids():
    
    global playlist_id
    
    if playlist_id=="":
        pg.alert("This field cannot be blank please RETRY",title="PLAYLIST ID ERROR")
        
    else:
        pass
    
    youtube =build('youtube','v3', developerKey=key)

    initial_ind=playlist_id.find("list=") 
    playlist_id=playlist_id[initial_ind+5:] #list= 

    print("PLAYLIST ID- "+Fore.RED+playlist_id+Fore.RESET)
    

    request = youtube.playlistItems().list(part='snippet', maxResults=1, playlistId=playlist_id)

    response = request.execute()
    num_videos=response['pageInfo']['totalResults']
    
    return  (num_videos)
    

ydl_opts = {
    'playlistend': no_vids(),
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'youtube_songs/%(title)s.%(ext)s',
    'noprogress': True,
    'no_continue': True,
    'nooverwrites': True,
    'ignoreerrors': True,
    'max_downloads': 10
}



with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list={}'.format(playlist_id)])

pg.alert("DONE DOWNLOADING",title="DONE! ENJOY YOUR SONGS OFFLINE :)")

print(Fore.GREEN+'ENJOY YOUR MUSIC OFFLINE! :D'+Fore.RESET)

    



