# import necessary modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

# pytube is a python library which is used for downloading videos from youtube
from pytube import YouTube

# create window
window = Tk()
window.configure(background = '#ff4d4d')

# window title
window.title('Youtube video downloader')

# window geometry
window.geometry('450x250')

# restrict window resize
window.resizable(0,0)

# function for downloading video
def downloadVideo():
    # get video link
    videoLink = str(link.get())
    # get download path
    loc = path.get()
    # create YouTube object
    yt = YouTube(videoLink)
    # select first stream from the available streams
    video = yt.streams.first()
    # download the video in the location specified
    video.download(loc)
    # show message after completion of download
    messagebox.showinfo('Download','video downloaded successfully')

# function for selecting path for download
def selectPath():
    loc = filedialog.askdirectory(initialdir = 'YOUR DIRECTORY PATH')
    path.set(loc)

# create label for displaying header
label = Label(window, text = 'Youtube Video Downloader', font = 'Times 20 bold', bg = '#ff4d4d')
label.pack(pady = 10)

# label for entering link
link_label = Label(window, text = 'Enter link here', font='helvetica 10 bold', bg = '#ff4d4d')
link_label.place(x=50, y=90)

# entry widget to enter link
link = StringVar()
link_entry = Entry(window, textvariable = link, width = 40).place(x = 180, y = 90)

# label for download location
save_location = Label(window, text = 'Select download location', font = 'helvetica 10 bold',bg = '#ff4d4d')
save_location.place(x=50, y=138)

# entry for entering download location
path = StringVar()
location = Entry(window, textvariable = path, width = 23).place(x = 222, y = 138)

# button for selecting download location
browse = Button(window, text = 'Browse', font = 'helvetica 10 bold', command = selectPath)
browse.place(x = 370, y = 135)

# button for downloading
download = Button(window, text = 'Download now', font = 'helvetica 12 bold', command = downloadVideo, bg='black',fg='red', relief =SUNKEN)
download.place(x = 115, y = 190)

#calling mainloop
window.mainloop()




