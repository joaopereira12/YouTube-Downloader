from tkinter import *
from tkinter import ttk 
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from pytube import Playlist, YouTube, request

PLAYLIST = 2
SINGLE_VIDEO = 1
MP3_FORMAT = 3
MP4_FORMAT = 4



app = Tk()
app.geometry('750x350')

folder = StringVar()
folder.set('.')

def changePath():
    folder.set(filedialog.askdirectory())
    print("directory changed")
    print(folder.get())



print(folder)

# title
app.title('YouTube MP3 Downloader')
title = Label(app,text= 'YouTube Downloader', font=("Comic Sans MS", 20, 'bold'), pady = 20)
title.place(x = 225 , y=20)


# Choose single video or playlist 

downloadType = IntVar()
singleVideo = Radiobutton(app, text = 'Video', font = ("Comic Sans MS", 14), pady = 15, variable=downloadType, value = 1)
singleVideo.place(x=400, y=125)

playlist = Radiobutton(app, text = 'Playlist', font = ("Comic Sans MS", 14), pady = 15, variable=downloadType, value = 2)
playlist.place(x=200, y=125)

downloadType.set(1)

# choose the folder to store

# URL insert
url = StringVar()
urlEntry = Entry(app, textvariable= url, width = 50)
urlEntry.place(x=225, y=100)



# File format Selection
format = IntVar()
mp3Format = Radiobutton(app, text = 'MP3', font = ("Comic Sans MS", 14), pady = 15, variable=format, value = 3)
mp3Format.place(x=200,y=175)
mp4Format = Radiobutton(app, text = 'MP4', font = ("Comic Sans MS", 14), pady = 15, variable=format, value = 4)
mp4Format.place(x=400,y=175)

format.set(3)

# Choose folder button 
folderButton = Button(app, text = 'Folder', height = 2, width = 20, command=lambda:changePath())
folderButton.place(x=100, y=275)



def convertVideo(link):
    yt = YouTube(link, use_oauth=False, allow_oauth_cache=True)
    if format.get() == 3:
       yt.streams.filter(only_audio=True).first().download(folder.get())
       print("done")
    elif format.get() == 4:
        yt.streams.get_highest_resolution().download(folder.get())
        print("done")
    
    print("video created")


def convertPlaylist(link):
    pl = Playlist(link)
    if format.get() == 3:
        for video in pl.videos:
            video.streams.filter(only_audio=True).first().download(folder.get())
            print("done")

    elif format.get() == 4:
        for video in pl.videos:
            video.streams.get_highest_resolution().download(folder.get())
            print("done")
    
    print("Playlist created")


    

def convert():
    
    if not url.get():
       messagebox.showerror("Erro", "Introduz um link")

   
    if downloadType.get() == 1:
        convertVideo(url.get())
    elif  downloadType.get() == 2:
        convertPlaylist(url.ge())
           
   
    print("Converted. Ending...") 
    

# Convert Button
convertButton = Button(app, text = 'Convert', height = 2, width = 20, command=lambda:convert())
convertButton.place(x=300, y=275)


app.mainloop()
