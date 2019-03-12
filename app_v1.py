# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import tkinter as tk # python 3
# import Tkinter as tk
import numpy as np

from PIL import Image, ImageTk
import random
from time import sleep

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('1050x600')  # set size of the main window to 300x300 pixels
        container = tk.Frame(self, background="black")

        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, OpeningPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix,PageSeven, EndPage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.config(bg='black')  # change the background color to black
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

        for i, F in enumerate((OpeningPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, EndPage)):
            b = tk.Button(self, text='visit Page %d' % (i + 1),command=lambda f=F: controller.show_frame(f))
            b.pack()

def transition(widget_values, controller, page):
    if widget_values != None:
        try: # when we have ratings (in a dict)
            for k, v in widget_values.items():
                print(k,v.get())
        except:
            for v in widget_values:
                print(v)

    controller.show_frame(page)

def agree_with(self1, controller, page, n = 2):
    '''creating agree screen'''

    image = Image.open('robots_finshed_talking' + '.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(self1, image=photo, bg='black')
    label.image = photo  # keep a reference!
    label.grid(row=n, columnspan=10, sticky='e')

    image = Image.open('agree' + '.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(self1, image=photo, bg='black')
    label.image = photo  # keep a reference!
    label.grid(row=n+1, columnspan=10, sticky='e', pady = 10)

    image = Image.open('red' + '.png')
    photo = ImageTk.PhotoImage(image)
    clr = '#%02x%02x%02x' % (255, 80, 80)
    red_button = tk.Button(self1, image=photo, bg = clr,
                           command=lambda: transition(['red'], controller, page))
    red_button.image = photo
    red_button.grid(row=n + 2, column=1, pady = 30)

    image = Image.open('blue' + '.png')
    photo = ImageTk.PhotoImage(image)
    clr = '#%02x%02x%02x' % (47, 85, 151)
    blue_button = tk.Button(self1, image=photo, bg = clr,
                            command=lambda: transition(['blue'], controller, page))
    blue_button.image = photo
    blue_button.grid(row=n + 2, column=8, pady = 30)

def pleas_rate(self, suspects):
    '''creating rating options'''

    ### randomize the order that the rating options are presented
    random.shuffle(suspects)

    scales = {}

    for i, photo in enumerate(suspects):
        scales[photo] = tk.Scale(self, from_=0, to=100, orient='horizontal', resolution=10, length=350, bg='black', fg='white')

        scales[photo].config(highlightthickness=0)
        scales[photo].grid(row=i + 2, column=0, columnspan=9, padx=10, pady=20, sticky='n')

        image = Image.open('suspect_' + photo + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=i + 2, column=9, sticky='e')

    return scales, i + 2

def next_button(self, scales, controller, page, i):
    button1 = tk.Button(self, text="<--", width=20,
                        command=lambda: transition(scales, controller, page))
    button1.grid(row=i + 1, column=1, columnspan=2)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open('story_1' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=0, columnspan=10, sticky='e')

        image = Image.open('rate' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=1, columnspan = 10, sticky='e')


        scales, i = pleas_rate(self, ['a', 'b', 'a_and_b'])

        next_button(self, scales, controller, PageTwo, i)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open('story_2' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=0, columnspan=10, sticky='e')

        agree_with(self, controller, PageThree, n = 2)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open('rate' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=1, columnspan = 10, sticky='e')

        scales, i = pleas_rate(self,['a', 'c', 'a_and_c'])

        next_button(self, scales, controller, PageFour, i)


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open('story_3' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=0, columnspan=10, sticky='e')

        agree_with(self, controller, PageFive, n = 2)

class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open('please_rank' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=0, columnspan=4, sticky='e')

        rankings = {}
        w,h = 401, 46
        for i, photo in enumerate(['a','b', 'c', 'd']):
            rankings[photo] = tk.Entry(self,  width = 5)
            rankings[photo].grid(row=i + 1, column=2, pady=0, sticky='n')

            image = Image.open('suspect_' + photo + '.png')
            # w, h = image.size
            image = image.resize((w, h), Image.ANTIALIAS)  # The (250, 250) is (height, width)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self, image=photo, bg='black')
            label.image = photo  # keep a reference!
            label.grid(row=i + 1, column=3, sticky='e', pady=0)

        for i, photo in enumerate(['a_and_b', 'a_and_c', 'a_and_d', 'b_and_c', 'b_and_d', 'c_and_d']):
            rankings[photo] = tk.Entry(self, width=5)
            rankings[photo].grid(row=i + 1, column=0, pady=0, sticky='n')

            image = Image.open('suspect_' + photo + '.png')
            image = image.resize((w, h), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self, image=photo, bg='black')
            label.image = photo  # keep a reference!
            label.grid(row=i + 1, column=1, sticky='s', padx=0)

        # button1 = tk.Button(self, text="<--", width=20,
        #                     command=lambda: controller.show_frame(PageSix))
        # button1.grid(row=i + 2, column=1, columnspan=1)

        next_button(self, rankings, controller, PageSix, i+1)


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open('robots_finshed_talking' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=0, columnspan = 2, sticky='e')

        image = Image.open('who_did_it' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=1, columnspan=2, sticky='e')

        rankings = {}
        w,h = 401, 46
        for i, p in enumerate(['a','b', 'c', 'd']):
            image = Image.open('suspect_' + p + '.png')
            image = image.resize((w, h), Image.ANTIALIAS)  # The (250, 250) is (height, width)
            photo = ImageTk.PhotoImage(image)
            rankings[p] = tk.Button(self, image=photo, bg='black',command=lambda p=p: transition([p], controller, PageSeven))
            rankings[p].image = photo  # keep a reference!
            rankings[p].grid(row=i + 2, column=1, sticky='s', padx=0, pady = 5)

        for i, p in enumerate(['a_and_b', 'a_and_c', 'a_and_d', 'b_and_c', 'b_and_d', 'c_and_d']):
            image = Image.open('suspect_' + p + '.png')
            image = image.resize((w, h), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            rankings[p] = tk.Button(self, image=photo, bg='black',command=lambda p=p: transition([p], controller, PageSeven))
            rankings[p].image = photo  # keep a reference!
            rankings[p].grid(row=i + 2, column=0, sticky='s', padx=0, pady = 5)

class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        n = -1
        image = Image.open('hire_detectivev' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=n + 1, columnspan=10, sticky='e', pady=10)

        image = Image.open('red' + '.png')
        photo = ImageTk.PhotoImage(image)
        clr = '#%02x%02x%02x' % (255, 80, 80)
        red_button = tk.Button(self, image=photo, bg=clr,
                               command=lambda: transition(['red'], controller, EndPage))
        red_button.image = photo
        red_button.grid(row=n + 2, column=1, pady=30)

        image = Image.open('blue' + '.png')
        photo = ImageTk.PhotoImage(image)
        clr = '#%02x%02x%02x' % (47, 85, 151)
        blue_button = tk.Button(self, image=photo, bg=clr,
                                command=lambda: transition(['blue'], controller, EndPage))
        blue_button.image = photo
        blue_button.grid(row=n + 2, column=8, pady=30)


class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        image = Image.open('the_end' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=0, sticky='e', pady=10)

        clr = '#%02x%02x%02x' % (146, 208, 80)
        image = Image.open('end_button' + '.png')
        photo = ImageTk.PhotoImage(image)

        b = tk.Button(self, image=photo, bg=clr, command=self.quit)
        b.grid(row=1, pady=10)
        b.image = photo


class OpeningPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        image = Image.open('begin_text' + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo  # keep a reference!
        label.grid(row=0, sticky='e', pady=10)

        clr = '#%02x%02x%02x' % (146, 208, 80)
        image = Image.open('begin_button' + '.png')
        photo = ImageTk.PhotoImage(image)

        b = tk.Button(self, image=photo, bg=clr, command=lambda: transition(None, controller, PageOne))
        b.grid(row=1, pady=10)
        b.image = photo

app = SeaofBTCapp()
app.mainloop()

# relative positioning --> independent of the screen size --> better for full screen
# https://www.python-course.eu/tkinter_layout_management.phpv --> see *.place()
# todo: torr rememeber you need it to work not to be the pretiest.

# todo: sound files!!!