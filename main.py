import time
from tkinter import *
from tkinter import ttk
import PIL.Image as im
import PIL.ImageTk as imtk
import pygame
from pygame import mixer



import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):

        def load(self, im):
            if isinstance(im, str):
                im = Image.open("C:\CODE KRLO\election_system\Gengar.gif")
            frames = []

            try:
                for i in count(1):
                    frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass
            self.frames = cycle(frames)

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(frames) == 1:
                self.config(image=next(self.frames))
            else:
                self.next_frame()

        def unload(self):
            self.config(image=None)
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.config(image=next(self.frames))
                self.after(self.delay, self.next_frame)


root = tk.Tk()
root.overrideredirect(True)
lbl = ImageLabel(root)
lbl.pack()
lbl.load('tenor.gif')

root.mainloop()


def main_prog():

    root = Tk()
    frame = ttk.Frame(root, padding=5)
    root.attributes('-fullscreen', True)
    root.title("VOTING SYSTEM IIITA")
    root.geometry('1000x700')
    mixer.init()
    mixer.music.load("C:\CODE KRLO\election_system\Total_war.wav")
    def back_sound():
        if button["text"] == "Off":
            button["text"] = "On"

            mixer.music.play()
        else:
            button["text"] = "Off"
            mixer.music.pause()

    bttn_sound_on = imtk.PhotoImage(file="C:\CODE KRLO\election_system\sound_button.png")
    button = Button(root, text='Off',height=0,font=('arial',1),background='red',width=0,borderwidth=0,bd=0, command=back_sound)
    button.pack(fill=BOTH, expand=True)


    background_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\main_bg2.png")
    close_button = imtk.PhotoImage(file="C:\CODE KRLO\election_system\close1.png")
    vote_icon = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Vote2.png")
    back = Label(root, image=background_img).pack(fill=BOTH, expand=True)
    feedback_icon= imtk.PhotoImage(file="C:\CODE KRLO\election_system\Feedback\Feedback_icon.png")

    def feedback():
        root.destroy()
        feed = Tk()
        feed.geometry('600x500+450+200')
        feed.overrideredirect(True)
        snd_icon = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Feedback\Send_icon.png")
        like_bttn = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Feedback\Liked.png")
        dislike_bttn = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Feedback\Dislike.png")
        feedback_bg = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Feedback\Feedback_bg.png")
        f_back_button_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Feedback\F_back.png")
        send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=feed.destroy).place(relx=0.05,
                                                                                                         rely=0.3)
        feed_bg = Label(image=feedback_bg).pack(fill=BOTH, expand=True)
        var = StringVar()
        feedback_1 = Entry(feed, textvariable=var, font=("Cambria", 14)).place(rely=0.55, relx=0.06, height=100,
                                                                               width=500)

        f_back_button = Button(feed, bd=0, image=f_back_button_img, highlightthickness=0, command=feed.destroy).place(
            relx=0.05, rely=0.04)

        def dis1():
            if dislike1["text"] == "d":
                dislike1["text"] = "l"
                dislike1["image"] = like_bttn
            else:
                dislike1["text"] = "d"
                dislike1["image"] = dislike_bttn

        dislike1 = Button(feed, text="dis", bd=0, image=dislike_bttn, highlightthickness=0, command=dis1).place(
            relx=0.068, rely=0.35)

        def dis2():
            dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.068, rely=0.35)
            dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.168, rely=0.35)
            star = 2

        button2 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis2).place(relx=0.168,
                                                                                                   rely=0.35)

        def dis3():
            dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.068, rely=0.35)
            dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.168, rely=0.35)
            dislike3 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.268, rely=0.35)
            star = 3

        dislike3 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis3).place(relx=0.268,
                                                                                                    rely=0.35)

        def dis4():
            dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.068, rely=0.35)
            dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.168, rely=0.35)
            dislike3 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.268, rely=0.35)
            dislike4 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.368, rely=0.35)
            star = 4

        dislike4 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis4).place(relx=0.368,
                                                                                                    rely=0.35)

        def dis5():
            dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.068, rely=0.35)
            dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.168, rely=0.35)
            dislike3 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.268, rely=0.35)
            dislike4 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.368, rely=0.35)
            dislike5 = Button(feed, bd=0, image=like_bttn, highlightthickness=0).place(relx=0.468, rely=0.35)
            star = 5

        dislike5 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis5).place(relx=0.468,
                                                                                                    rely=0.35)

        def mail():
            import smtplib
            otp = var.get()
            msg = otp
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("raoarjun6763@gmail.com", "vglt fhbm admd qfzt")
            emailid = "sidyaduvanshi02@gmail.com"
            s.sendmail('&&&&&&&&&&&', emailid, msg)
            feed.destroy()

        send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=mail).place(relx=0.75, rely=0.65)

        feed.mainloop()
        main_prog()
    def popup_win1():
            root.destroy()
            win1 = Tk()
            win1.title("                                                          DRAGONITE")
            win1.geometry('503x703')

            popup_background_img1 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position1\Dragonite.png")
            popup_back = Label(win1, bg='black', image=popup_background_img1).pack(fill=BOTH, expand=True)
            frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
            vid1_bttn=Button(win1,image=frwd_bttn_img,borderwidth=0,bd=0).place(rely=0.4,relx=0.87)
            win1.mainloop()
            main_prog()
    cand1_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position1\can1_bg.png")
    cand1Img = Label(root, image=cand1_img, borderwidth=5).place(relx=0.07, rely=0.3)
    cand1 = Button(root, image=vote_icon, height=40, width=140, borderwidth=0, relief="raised", border=4,command=popup_win1).place(relx=0.085, rely=0.5)



    def popup_win2():
            root.destroy()
            win2 = Tk()
            win2.title("                                                          CHARIZARD")
            win2.geometry('503x703')
            popup_background_img2 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position2\Charizard.png")
            popup_back = Label(win2, bg='black', image=popup_background_img2).pack(fill=BOTH, expand=True)
            frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
            vid2_bttn = Button(win2, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
            win2.mainloop()
            main_prog()
    cand2_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position2\cand2_bg.png")
    cand2Img = Label(root, image=cand2_img, borderwidth=5).place(relx=0.25, rely=0.3)
    cand2 = Button(root, image=vote_icon, height=40, width=140, borderwidth=0, relief="raised", border=4,command=popup_win2).place(
        relx=0.27, rely=0.5)



    def popup_win3():
            root.destroy()
            win3 = Tk()
            win3.title("                                                          TYRANITAR")
            win3.geometry('503x703')
            popup_background_img3 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position3\Tyranitar.png")
            popup_back = Label(win3, bg='black', image=popup_background_img3).pack(fill=BOTH, expand=True)
            frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
            vid3_bttn = Button(win3, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
            win3.mainloop()
            main_prog()
    cand3_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position3\cand3_bg.png")
    cand3Img = Label(root, image=cand3_img, borderwidth=5).place(relx=0.435, rely=0.3)
    cand3 = Button(root, image=vote_icon, height=40, width=140, relief="raised", border=4,command=popup_win3).place(relx=0.455, rely=0.5)



    def popup_win4():
            root.destroy()
            win4 = Tk()
            win4.title("                                                          SALAMANCE")
            win4.geometry('500x700')
            popup_background_img4 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position4\Salamence.png")
            popup_back = Label(win4, image=popup_background_img4).pack(fill=BOTH, expand=True)
            frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
            vid4_bttn = Button(win4, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
            win4.mainloop()
            main_prog()
    cand4_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position4\cand4_bg.png")
    cand4Img = Label(root, image=cand4_img, borderwidth=5).place(relx=0.61, rely=0.3)
    cand4 = Button(root, image=vote_icon, height=40, width=140, relief="raised", border=4,command=popup_win4).place(relx=0.63, rely=0.5)



    def popup_win5():
            root.destroy()
            win5 = Tk()
            win5.title("                                                          BLASTOISE")
            win5.geometry('500x700')
            popup_background_img5 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position5\Metagross.png")
            popup_back = Label(win5, image=popup_background_img5).pack(fill=BOTH, expand=True)
            frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
            vid5_bttn = Button(win5, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
            win5.mainloop()
            main_prog()
    cand5_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position5\cand5_bg.png")
    cand5Img = Label(root, image=cand5_img, borderwidth=5).place(relx=0.79, rely=0.3)
    cand5 = Button(root, image=vote_icon, height=40, width=140, relief="raised", border=4,command=popup_win5).place(relx=0.808, rely=0.5)


    def popup_win6():
            root.destroy()
            win6 = Tk()
            win6.title("                                                          BLASTOISE")
            win6.geometry('500x700')
            popup_background_img6 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position6\Blastoise.png")
            popup_back = Label(win6, image=popup_background_img6).pack(fill=BOTH, expand=True)
            frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
            vid6_bttn = Button(win6, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
            win6.mainloop()
            main_prog()

    cand6_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position6\cand6_bg.png")
    cand6Img = Label(root, image=cand6_img, borderwidth=5).place(relx=0.07, rely=0.65)
    cand6 = Button(root, image=vote_icon, height=40, width=140, relief="raised", border=4, command=popup_win6).place(relx=0.085, rely=0.85)

    def popup_win7():
        root.destroy()
        win7 = Tk()
        win7.title("                                                          VENUSAUR")
        win7.geometry('503x703')
        popup_background_img7= imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position7\Venusaur.png")
        popup_back = Label(win7, bg='black', image=popup_background_img7).pack(fill=BOTH, expand=True)
        frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
        vid7_bttn = Button(win7, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
        win7.mainloop()
        main_prog()
    cand7_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position7\cand7_bg.png")
    cand7Img = Label(root, image=cand7_img, borderwidth=5).place(relx=0.61, rely=0.65)
    cand7 = Button(root, image=vote_icon, height=40, width=140, borderwidth=0,command=popup_win7, relief="raised", border=4).place(relx=0.63, rely=0.85)

    def popup_win8():
        root.destroy()
        win8 = Tk()
        win8.title("                                                          ARCANINE")
        win8.geometry('503x703')
        popup_background_img8 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position8\Arcanine.png")
        popup_back = Label(win8,bg='black' ,image=popup_background_img8).pack(fill=BOTH, expand=True)
        frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
        vid8_bttn = Button(win8, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
        win8.mainloop()
        main_prog()

    cand8_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position8\cand8_bg.png")
    cand8_Img = Label(root, image=cand8_img, borderwidth=5).place(relx=0.25, rely=0.65)
    cand8 = Button(root, image=vote_icon, height=40, width=140, borderwidth=0, relief="raised", border=4,command=popup_win8).place(relx=0.27, rely=0.85)


    def popup_win9():
        root.destroy()
        win9 = Tk()
        win9.title("                                                          STEELIX")
        win9.geometry('503x703')
        popup_background_img9 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position9\Steelix.png")
        popup_back = Label(win9,bg='black' ,image=popup_background_img9).pack(fill=BOTH, expand=True)
        frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
        vid9_bttn = Button(win9, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
        win9.mainloop()
        main_prog()
    cand9_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position9\cand9_bg.png")
    cand9Img = Label(root, image=cand9_img, borderwidth=5).place(relx=0.43, rely=0.65)
    cand9 = Button(root, image=vote_icon, height=40, width=140, relief="raised", border=4, command=popup_win9).place(relx=0.45, rely=0.85)

    def popup_win10():
        root.destroy()
        win10 = Tk()
        win10.title("                                                          SCIZOR")
        win10.geometry('503x703')
        popup_background_img10 = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position10\Scizor.png")
        popup_back = Label(win10, bg='black', image=popup_background_img10).pack(fill=BOTH, expand=True)
        frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Forward_bttn.png")
        vid10_bttn = Button(win10, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
        win10.mainloop()
        main_prog()

    cand10_img = imtk.PhotoImage(file="C:\CODE KRLO\election_system\Position10\cand10_bg.png")
    cand10Img = Label(root, image=cand10_img, borderwidth=5).place(relx=0.79, rely=0.65)
    cand10 = Button(root, image=vote_icon, height=40, width=140, relief="raised", border=4, command=popup_win10).place( relx=0.808, rely=0.85)

    sound_button = Button(root,text="Off",image=bttn_sound_on, height=35, width=35,borderwidth=0,bd=0, command=back_sound).place(relx=0.976, rely=0.044)
    exit_button = Button(root,text="Off",image=close_button, height=35, width=35, command=root.destroy,borderwidth=0,bd=0).place(relx=0.976, rely=0.0)
    feedback_button=Button(root,image=feedback_icon, height=50, width=35,borderwidth=0,bd=0, command=feedback).place(relx=0.976, rely=0.088)
    root.mainloop()

main_prog()