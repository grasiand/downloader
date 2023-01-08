import youtube_dl
from colorama import Fore, Back, Style, init
import os
import time
from pytube import YouTube
init(autoreset=True)

os.system("cls")
user = os.environ['USERNAME']

print(Fore.RED + '''
 dP""b8 88""Yb    db    .dP"Y8 88    db    88b 88 8888b.  
dP   `" 88__dP   dPYb   `Ybo." 88   dPYb   88Yb88 8I   Yb 
Yb  "88 88"Yb   dP__Yb  o.`Y8b 88  dP__Yb  88 Y88 8I   dY 
 YboodP 88  Yb dP""""Yb 8bodP' 88 dP""""Yb 88  Y8 8888Y"   -@grasiand
 
 ''')

sys_password = "grasiand"

sifre = input(Fore.CYAN + "PASSWORD: ")

if  (sifre != sys_password):
        print(Fore.RED + "ACCESS DENIE")
        time.sleep(5)

elif (sifre != sys_password):
        print(Fore.RED + "ACCESS DENIED")
else:
    print(Fore.BLUE + "LOGIN SUCCESFUL, WELCOME " + user)
    time.sleep(5)
os.system("cls")

vur = input(Fore.GREEN + """
Grasiand Youtube Video Indirici

1) MP3 indir
2) MP4 indir

hangi islemi yapmak istersiniz ------>  """)

os.system("cls")

link = input(Fore.GREEN + "Link ---->  ")

if vur == "1":
	video_info = youtube_dl.YoutubeDL().extract_info(
		url = link,download=False
	)

	filename = f"{video_info['title']}.mp3"
	options={
		'format':'bestaudio/best',
		'keepvideo':False,
		'outtmpl':filename,
	}

	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([video_info['webpage_url']])

	print("İndirme tamamlandı... {}".format(filename))
time.sleep(3)

if vur == "2":
    yt = YouTube(link)
    print(Fore.LIGHTMAGENTA_EX + "videonuz indiriliyor lutfen bekleyiniz")
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    print(Fore.RED + "videonuz indirildi")
time.sleep(3)
