import time
from tkVideoPlayer import TkinterVideo
import tkinter as tk
from tkinter import *
from tkinter import ttk
import PIL.Image as im
import PIL.ImageTk as imtk
from pygame import mixer
from tkVideoPlayer import TkinterVideo
import tkinter as tk
splash = tk.Tk()
splash.attributes('-fullscreen', True)
esc=tk.Button(splash,command=splash.destroy).place(rely=2,relx=2)
videoplayer = TkinterVideo(master=splash, scaled=True)
videoplayer.load(r"C:\CODE KRLO\Pokedex\Battle_bg.mp4")
videoplayer.pack(expand=True, fill="both")
videoplayer.play()
def close_win(e):
   splash.destroy()
   def main_prog():

       root = Tk()
       frame = ttk.Frame(root, padding=5)
       root.attributes('-fullscreen', True)
       root.title("VOTING SYSTEM IIITA")
       root.geometry('1000x700')
       mixer.init()
       mixer.music.load("C:\CODE KRLO\Pokedex\Total_war.wav")

       def back_sound():
           if button["text"] == "Off":
               button["text"] = "On"

               mixer.music.play()
           else:
               button["text"] = "Off"
               mixer.music.pause()

       bttn_sound_on = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\sound_button.png")
       button = Button(root, text='Off', height=0, font=('arial', 1), background='red', width=0, borderwidth=0, bd=0,
                       command=back_sound)
       button.pack(fill=BOTH, expand=True)

       background_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\main_bg.png")
       close_button = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\close1.png")
       vote_icon = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Vote2.png")
       back = Label(root, image=background_img).pack(fill=BOTH, expand=True)
       feedback_icon = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Feedback\Feedback_icon.png")
       explore_icon = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Explore.png")
       def feedback():
           root.destroy()

           feed = Tk()
           feed.geometry('600x500+450+200')
           feed.overrideredirect(True)
           snd_icon = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Feedback\Send_icon.png")
           like_bttn = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Feedback\Liked.png")
           dislike_bttn = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Feedback\Dislike.png")
           feedback_bg = imtk.PhotoImage(file="C:\CODE KRLO\VotingSystem\Feedback_bg.png")
           f_back_button_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Feedback\F_back.png")
           send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=feed.destroy).place(relx=0.05,rely=0.3)
           feed_bg = Label(image=feedback_bg).pack(fill=BOTH, expand=True)
           var = StringVar()
           feedback_1 = Entry(feed, textvariable=var, font=("arial", 14)).place(rely=0.55, relx=0.03, height=100,width=500)
           f_back_button = Button(feed, bd=0, image=f_back_button_img, highlightthickness=0,command=feed.destroy).place(relx=0.03, rely=0.02)

           def dis1():
               def mail():
                   import smtplib
                   from email.message import EmailMessage

                   msg = EmailMessage()
                   msg.set_content(var.get())

                   msg['Subject'] = 'USER RATING : 1 STAR'
                   msg['From'] = "project.feedback.02@gmail.com"
                   msg['To'] = "sidyaduvanshi02@gmail.com"

                   server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                   server.login("project.feedback.02@gmail.com", "ydza xjxm dabe eboo")
                   server.send_message(msg)
                   server.quit()

               send_icon = Button(master=feed,bd=0, image=snd_icon, highlightthickness=0, command=mail).place(relx=0.03,rely=0.78)
               dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis1).place(relx=0.03,rely=0.35)
               dislike2 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis2).place(relx=0.13,rely=0.35)
               dislike3 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis3).place(relx=0.23,rely=0.35)
               dislike4 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis4).place(relx=0.33,rely=0.35)
               dislike5 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis5).place(relx=0.43,rely=0.35)
           dislike1 = Button(feed, text="dis", bd=0, image=dislike_bttn, highlightthickness=0, command=dis1).place(relx=0.03, rely=0.35)

           def dis2():
               star = 2

               def mail():
                   import smtplib
                   from email.message import EmailMessage

                   msg = EmailMessage()
                   msg.set_content(var.get())

                   msg['Subject'] = 'USER RATING : 2 STAR'
                   msg['From'] = "project.feedback.02@gmail.com"
                   msg['To'] = "sidyaduvanshi02@gmail.com"

                   server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                   server.login("project.feedback.02@gmail.com", "ydza xjxm dabe eboo")
                   server.send_message(msg)
                   server.quit()

               send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=mail).place(relx=0.03,rely=0.78)
               dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis1).place(relx=0.03,rely=0.35)
               dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis2).place(relx=0.13,rely=0.35)
               dislike3 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis3).place(relx=0.23,rely=0.35)
               dislike4 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis4).place(relx=0.33,rely=0.35)
               dislike5 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis5).place(relx=0.43,rely=0.35)

           dislike2 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis2).place(relx=0.13,rely=0.35)

           def dis3():
               def mail():
                   import smtplib
                   from email.message import EmailMessage

                   msg = EmailMessage()
                   msg.set_content(var.get())

                   msg['Subject'] = 'USER RATING : 3 STAR'
                   msg['From'] = "project.feedback.02@gmail.com"
                   msg['To'] = "sidyaduvanshi02@gmail.com"

                   server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                   server.login("project.feedback.02@gmail.com", "ydza xjxm dabe eboo")
                   server.send_message(msg)
                   server.quit()

               send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=mail).place(relx=0.03,rely=0.78)
               dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis1).place(relx=0.03,rely=0.35)
               dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis2).place(relx=0.13,rely=0.35)
               dislike3 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis3).place(relx=0.23,rely=0.35)
               dislike4 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis4).place(relx=0.33,rely=0.35)
               dislike5 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis5).place(relx=0.43, rely=0.35)

           dislike3 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis3).place(relx=0.23,rely=0.35)

           def dis4():
               def mail():
                   import smtplib
                   from email.message import EmailMessage

                   msg = EmailMessage()
                   msg.set_content(var.get())

                   msg['Subject'] = 'USER RATING : 4 STAR'
                   msg['From'] = "project.feedback.02@gmail.com"
                   msg['To'] = "sidyaduvanshi02@gmail.com"

                   server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                   server.login("project.feedback.02@gmail.com", "ydza xjxm dabe eboo")
                   server.send_message(msg)
                   server.quit()

               send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=mail).place(relx=0.03,rely=0.78)
               dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis1).place(relx=0.03,rely=0.35)
               dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis2).place(relx=0.13,rely=0.35)
               dislike3 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis3).place(relx=0.23,rely=0.35)
               dislike4 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis4).place(relx=0.33,rely=0.35)
               dislike5 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis5).place(relx=0.43,rely=0.35)

           dislike4 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis4).place(relx=0.33,rely=0.35)

           def dis5():
               def mail():
                   import smtplib
                   from email.message import EmailMessage

                   msg = EmailMessage()
                   msg.set_content(var.get())

                   msg['Subject'] = 'USER RATING : 5 STAR'
                   msg['From'] = "project.feedback.02@gmail.com"
                   msg['To'] = "sidyaduvanshi02@gmail.com"

                   server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                   server.login("project.feedback.02@gmail.com", "ydza xjxm dabe eboo")
                   server.send_message(msg)
                   server.quit()

               send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=mail).place(relx=0.03,rely=0.78)
               dislike1 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis1).place(relx=0.03,rely=0.35)
               dislike2 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis2).place(relx=0.13,rely=0.35)
               dislike3 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis3).place(relx=0.23,rely=0.35)
               dislike4 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis4).place(relx=0.33,rely=0.35)
               dislike5 = Button(feed, bd=0, image=like_bttn, highlightthickness=0, command=dis5).place(relx=0.43,rely=0.35)

           dislike5 = Button(feed, bd=0, image=dislike_bttn, highlightthickness=0, command=dis5).place(relx=0.43,rely=0.35)

           def mail():
               import smtplib
               from email.message import EmailMessage

               msg = EmailMessage()
               msg.set_content('nice')

               msg['Subject'] = 'USER RATING : 5 STARS'
               msg['From'] = "raoarjun6763@gmail.com"
               msg['To'] = "sidyaduvanshi02@gmail.com"

               server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
               server.login("raoarjun6763@gmail.com", "vglt fhbm admd qfzt")
               server.send_message(msg)
               server.quit()

           send_icon = Button(feed, bd=0, image=snd_icon, highlightthickness=0, command=mail).place(relx=0.03,rely=0.78)

           feed.mainloop()
           main_prog()

       def explore():
           root.destroy()
           newroot=Tk()
           newroot.attributes('-fullscreen', True)
           background_img1 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\BG2.png")
           back_button_img1 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Feedback\F_back.png")
           back1 = Label(newroot, image=background_img1).pack(fill=BOTH, expand=True)
           f_back_button = Button(newroot, bd=0, image=back_button_img1, highlightthickness=0,command=newroot.destroy).place(relx=0.03, rely=0.02)

           def popup_win1():
               newroot.destroy()
               win1 = Tk()
               win1.title("                                                          DRAGONITE")
               win1.geometry('503x703+50+50')

               popup_background_img1 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position1\Dragonite.png")
               popup_back = Label(win1, bg='black', image=popup_background_img1).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid1_bttn = Button(win1, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
               win1.mainloop()
               main_prog()
           cand1_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position1\can1_bg.png")
           cand1Img = Button(newroot, image=cand1_img, highlightthickness=0, bd=0, command=popup_win1).place(relx=0.06,rely=0.2)
           def popup_win2():
               newroot.destroy()
               win2 = Tk()
               win2.title("                                                          CHARIZARD")
               win2.geometry('503x703+50+50')
               popup_background_img2 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position2\Charizard.png")
               popup_back = Label(win2, bg='black', image=popup_background_img2).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid2_bttn = Button(win2, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
               win2.mainloop()
               main_prog()
           cand2_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position2\cand2_bg.png")
           cand2Img = Button(newroot, image=cand2_img, highlightthickness=0, bd=0, command=popup_win2).place(relx=0.25,rely=0.03)
           def popup_win3():
               newroot.destroy()
               win3 = Tk()
               win3.title("                                                          TYRANITAR")
               win3.geometry('503x703+50+50')
               popup_background_img3 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position3\Tyranitar.png")
               popup_back = Label(win3, bg='black', image=popup_background_img3).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid3_bttn = Button(win3, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
               win3.mainloop()
               main_prog()
           cand3_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position3\cand3_bg.png")
           cand3Img = Button(newroot, image=cand3_img, highlightthickness=0, bd=0, command=popup_win3).place(relx=0.21, rely=0.36)
           def popup_win4():
               newroot.destroy()
               win4 = Tk()
               win4.title("                                                          SALAMANCE")
               win4.geometry('500x700+50+50')
               popup_background_img4 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position4\Salamence.png")
               popup_back = Label(win4, image=popup_background_img4).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid4_bttn = Button(win4, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
               win4.mainloop()
               explore()
           cand4_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position4\cand4_bg.png")
           cand4Img = Button(newroot, image=cand4_img, highlightthickness=0, bd=0, command=popup_win4).place(relx=0.635,rely=0.03)
           def popup_win5():
               newroot.destroy()
               win5 = Tk()
               win5.title("                                                          METAGROSS")
               win5.geometry('500x700+50+50')
               popup_background_img5 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position5\Metagross.png")
               popup_back = Label(win5, image=popup_background_img5).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid5_bttn = Button(win5, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.2, relx=0.87)
               win5.mainloop()
               explore()
           cand5_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position5\cand5_bg.png")
           cand5Img = Button(newroot, image=cand5_img, highlightthickness=0, bd=0, command=popup_win5).place(relx=0.82,rely=0.2)
           def popup_win6():
               newroot.destroy()
               win6 = Tk()
               win6.title("                                                          BLASTOISE")
               win6.geometry('500x700+50+50')
               popup_background_img6 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position6\Blastoise.png")
               popup_back = Label(win6, image=popup_background_img6).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid6_bttn = Button(win6, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
               win6.mainloop()
               main_prog()
           cand6_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position6\cand6_bg.png")
           cand6Img = Button(newroot, image=cand6_img, highlightthickness=0, bd=0, command=popup_win6).place(relx=0.06,rely=0.55)
           def popup_win7():
               newroot.destroy()
               win7 = Tk()
               win7.title("                                                          VENUSAUR")
               win7.geometry('503x703+50+50')
               popup_background_img7 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position7\Venusaur.png")
               popup_back = Label(win7, bg='black', image=popup_background_img7).pack(fill=BOTH, expand=True)
               win7.mainloop()
               explore()
           cand7_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position7\cand7_bg.png")
           cand7Img = Button(newroot, image=cand7_img, highlightthickness=0, bd=0, command=popup_win7).place(relx=0.635,rely=0.68)
           def popup_win8():
               newroot.destroy()
               win8 = Tk()
               win8.title("                                                          ARCANINE")
               win8.geometry('503x703+50+50')
               popup_background_img8 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position8\Arcanine.png")
               popup_back = Label(win8, bg='black', image=popup_background_img8).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid8_bttn = Button(win8, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
               win8.mainloop()
               explore()
           cand8_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position8\cand8_bg.png")
           cand8_Img = Button(newroot, image=cand8_img, highlightthickness=0, bd=0, command=popup_win8).place(relx=0.25,rely=0.68)
           def popup_win9():
               newroot.destroy()
               win9 = Tk()
               win9.title("                                                          STEELIX")
               win9.geometry('503x703+50+50')
               popup_background_img9 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position9\Steelix.png")
               popup_back = Label(win9, bg='black', image=popup_background_img9).pack(fill=BOTH, expand=True)
               frwd_bttn_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Forward_bttn.png")
               vid9_bttn = Button(win9, image=frwd_bttn_img, borderwidth=0, bd=0).place(rely=0.4, relx=0.87)
               win9.mainloop()
               main_prog()
           cand9_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position9\cand9_bg.png")
           cand9Img = Button(newroot, image=cand9_img, highlightthickness=0, bd=0, command=popup_win9).place(relx=0.67,rely=0.36)
           def popup_win10():
               newroot.destroy()
               win10 = Tk()
               win10.title("                                                          SCIZOR")
               win10.geometry('503x703+50+50')
               popup_background_img10 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position10\Scizor.png")
               popup_back = Label(win10, bg='black', image=popup_background_img10).pack(fill=BOTH, expand=True)
               win10.mainloop()
               main_prog()
           cand10_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position10\cand10_bg.png")
           cand10Img = Button(newroot, image=cand10_img, highlightthickness=0, bd=0, command=popup_win10).place(relx=0.82,rely=0.55)
           def popup_win11():
               newroot.destroy()
               win11 = Tk()
               win11.title("                                                          SECPTILE")
               win11.geometry('503x703+50+50')
               popup_background_img11 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position11\Secptile1.png")
               popup_back = Label(win11, bg='black', image=popup_background_img11).pack(fill=BOTH, expand=True)
               win11.mainloop()
               main_prog()
           cand11_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position11\Secptile.png")
           cand11Img = Button(newroot, image=cand11_img, highlightthickness=0, bd=0, command=popup_win11).place(relx=0.45, rely=0.03)
           def popup_win12():
               newroot.destroy()
               win12 = Tk()
               win12.title("                                                          RYQUZA")
               win12.geometry('503x703+50+50')
               popup_background_img12 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position12\Ryquza.png")
               popup_back = Label(win12, bg='black', image=popup_background_img12).pack(fill=BOTH, expand=True)
               win12.mainloop()
               main_prog()
           cand12_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position12\Ryquza1.png")
           cand12Img = Button(newroot, image=cand12_img, highlightthickness=0, bd=0, command=popup_win12).place(relx=0.37,rely=0.36)
           def popup_win13():
               newroot.destroy()
               win13 = Tk()
               win13.title("                                                          GRODON")
               win13.geometry('503x703+50+50')
               popup_background_img13 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position13\Grodon1.png")
               popup_back = Label(win13, bg='black', image=popup_background_img13).pack(fill=BOTH, expand=True)
               win13.mainloop()
               main_prog()
           cand13_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position13\Grodon.png")
           cand13Img = Button(newroot, image=cand13_img, highlightthickness=0, bd=0, command=popup_win13).place(relx=0.52, rely=0.36)
           def popup_win14():
               newroot.destroy()
               win14 = Tk()
               win14.title("                                                          ALAKAZAM")
               win14.geometry('503x703+50+50')
               popup_background_img14 = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position14\Alakazam1.png")
               popup_back = Label(win14, bg='black', image=popup_background_img14).pack(fill=BOTH, expand=True)
               win14.mainloop()
               main_prog()
           cand14_img = imtk.PhotoImage(file="C:\CODE KRLO\Pokedex\Position14\Alakazam.png")
           cand14_Img = Button(newroot, image=cand14_img, highlightthickness=0, bd=0, command=popup_win14).place(relx=0.45,rely=0.68)

           newroot.mainloop()
           main_prog()
       explore_button = Button(root, image=explore_icon, height=80, width=280, borderwidth=0, bd=0,command=explore).place(relx=0.41, rely=0.25)
       sound_button = Button(root, text="Off", image=bttn_sound_on, height=80, width=280, borderwidth=0, bd=0,command=back_sound).place(relx=0.41, rely=0.55)
       exit_button = Button(root, text="Off", image=close_button, height=80, width=280, command=root.destroy,borderwidth=0, bd=0).place(relx=0.41, rely=0.7)
       feedback_button = Button(root, image=feedback_icon, height=80, width=280, borderwidth=0, bd=0,command=feedback).place(relx=0.41, rely=0.4)
       root.mainloop()

   main_prog()
splash.bind('<Return>', lambda e: close_win(e))
splash.mainloop()
