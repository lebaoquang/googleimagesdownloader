from google_images_download import google_images_download
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox
from time import*

class dgi(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False,False)
        self.title("Google Images Downloader - 11 Tin")
        self.iconbitmap(r'tin.ico')
    def Label(self):
        image2 = Image.open('bg.jpg')
        self.image1 = ImageTk.PhotoImage(image2)
        w = self.image1.width()
        h = self.image1.height()
        self.backgroundImageLabel = Label(self, image=self.image1,fg="blue")
        self.backgroundImageLabel.place(x=0,y=0)

        self.canvas = Canvas(self, bg="pink", width=400,height=330)
        self.canvas.place(x=150,y=60)

        self.title = Label(self,text="GOOGLE IMAGES DOWNLOADER",fg="red", bg="pink", font="Bold 15")
        self.title.place(x=190, y=80)

        self.title = Label(self, text="DEV: 11 TIN - GROUP 1", fg="grey", bg="pink", font="Helvetica 14")
        self.title.place(x=245, y=110)

        self.ipnameLabel = Label(self, text="Enter Keywords:", fg="green", bg="pink",font="3")
        self.ipnameLabel.place(x=165,y=150)

        self.ipnumLabel = Label(self, text="Enter A Number:", fg="green", bg="pink",font="3")
        self.ipnumLabel.place(x=165, y=200)

        self.title = Label(self, text="(Số ảnh cần nhập phải là số nguyên <= 100)", fg="grey", bg="pink", font="ARIAL 14")
        self.title.place(x=165,y=250)

    def Entry(self):
        self.ipname = Text(self, borderwidth=0,width=22,height=1, font=('ARIAL', 12))
        self.ipname.place(x=320,y=155)

        self.ipnum = Text(self, borderwidth=0, width=22, height=1, font=('ARIAL', 12))
        self.ipnum.place(x=320, y=205)

    def Button(self):
        self.quitButton = Button(self,text="Quit", fg="white", bg="#303030", command=self.quit)
        self.quitButton.place(x=290, y=300)

        self.downloadButton = Button(self, text="Download", fg="aqua", bg="#303030",command=self.download)
        self.downloadButton.place(x=350, y=300)

    def download(self):
        global name
        global num
        name = self.ipname.get(1.0, END)
        num = self.ipnum.get(1.0, END)
        tkinter.messagebox.showinfo("Thông báo", f"Đang tải xuống {name}")
        try:
            response = google_images_download.googleimagesdownload()
            arguments = {"keywords": name[0:-1],
                         "limit": int(num),
                         "print_urls": False}
            paths = response.download(arguments)
            tkinter.messagebox.showinfo("Thông báo","Hoàn tất tải xuống! Cảm ơn đã sử dụng!")
            self.quit()
        except:
            tkinter.messagebox.showinfo("Thông báo", "Lỗi! Hãy chắc chắn bạn nhập đúng dữ liệu hoặc số ảnh cần tải (số nguyên từ 100 trở xuống)!")

if __name__ == "__main__":
    Main = dgi()
    Main.Label()
    Main.Entry()
    Main.Button()
    Main.mainloop()