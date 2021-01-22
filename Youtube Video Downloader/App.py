from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from youtube_dl import *


class YoutubeGui():
    def __init__(self,window):
        self.window=window
        self.window.title("Youtube Video Downloader")
        self.window.geometry('500x300')
        #tkinter widgets
        self.image=ImageTk.PhotoImage(Image.open("logo.png"))
        self.img=Label(self.window,image=self.image,height=100,width=100)
        self.image_text=Label(self.window,text="Youtube Video Downloader",font=('Helvetica',18,'bold'))
        self.label=Label(self.window,text="Paste Video Link")
        self.text = Text(self.window, width=50, height=0.2)
        self.button = Button(self.window, text='Download Video', command=lambda: self.get_url())
        # widgets Alignment
        self.img.place(x=370, y=10)
        self.image_text.place(x=20, y=45)
        self.label.pack(padx=5, side=LEFT)
        self.text.pack(padx=20, side=LEFT)
        self.button.place(x=5, y=200)
    # Functions
    def wait(self):
        msg.showinfo("Message", "Confirm to Start Downloading")

    def download_video(self,url):
        ytdl = {}
        with YoutubeDL(ytdl) as ydl:
            try:
                ydl.download([url])
            except:
                msg.showerror("Downloading Error", "Unexpected Error Occurred while downloading video")

    def done(self):
        msg.showinfo("Message", "Downloading Completed")

    def get_url(self):
        video_url = self.text.get('1.0', END)
        self.wait()
        self.download_video(video_url)
        self.done()
        self.text.delete('1.0',END)

if __name__ == '__main__':
    root=Tk()
    gui=YoutubeGui(root)
    root.mainloop()

