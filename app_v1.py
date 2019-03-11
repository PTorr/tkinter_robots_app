# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import tkinter as tk

import numpy as np
from PIL import Image, ImageTk

LARGE_FONT = ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, background="black")

        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame
            frame.config(bg='black') # change the background color to black
            frame.grid(row=3, column=3, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # image = Image.open('red_nao.jpg')
        image = Image.open('red_nao_2.png')
        photo = ImageTk.PhotoImage(image)

        image = Image.open('red_nao_1.jpg')
        photo1 = ImageTk.PhotoImage(image)


        # photo = tk.PhotoImage(file ='red_nao_2.png')
        # photo = tk.PhotoImage(file ='nao_robot_2.gif')

        label = tk.Label(self, image = photo)
        label.image = photo  # keep a reference!
        label.grid(row = 0, column = 0)

        label = tk.Label(self, image = photo1)
        label.image = photo1  # keep a reference!
        label.grid(row = 0, column = 1)

        # label.pack()
        # for j, i in enumerate(np.arange(0,101,10)):
        #     button2 = tk.Button(self, text=str(i),
        #                         command=lambda: controller.show_frame(PageTwo))
        #     button2.grid(row = 1, column = j)
        #
        # for j, i in enumerate(np.arange(0,101,10)):
        #     button2 = tk.Button(self, text=str(i),
        #                         command=lambda: controller.show_frame(PageTwo))
        #     button2.grid(row = 2, column = j)
        #

        # print(w.get())

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open('suspect_a.png')
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.grid(row = 0, columnspan = 4)

        w1 = tk.Scale(self, from_=0, to=100, orient='horizontal', resolution=10)
        w1.grid(row = 1, columnspan = 3)

        label = tk.Label(self, image = photo, bg = 'black')
        label.image = photo  # keep a reference!
        label.grid(row=1, column=4)

        w2 = tk.Scale(self, from_=0, to=100, orient='horizontal', resolution=10, bg = 'black', fg = 'white')
        w2.grid(row = 2, columnspan = 4)

        w3 = tk.Scale(self, from_=0, to=100, orient='horizontal', resolution=10, bg = 'black', fg = 'white')
        w3.grid(row = 3, columnspan = 4)

        button1 = tk.Button(self, text="-->",
                            command=lambda: print(w1.get(),w3.get()))

        button1.grid(row = 4, columnspan = 3)

app = SeaofBTCapp()
app.mainloop()