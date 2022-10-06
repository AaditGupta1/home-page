from email.mime import image
from tkinter import *
from PIL import ImageTk , Image
import webbrowser

color_bg = '#f5ecd7'
font = 'Comic Sans MS'

main = Tk()
main.geometry('1500x800')
main.title('The Aura')
main.config(bg=color_bg)

#------------------------------------------------------------------------

image_bg = Image.open('bg1.png')
image_bg = image_bg.resize((1600,800), Image.ANTIALIAS)
image_bg = ImageTk.PhotoImage(image_bg)

image_l = Label(main,image=image_bg)
image_l.place(relx=0.5,rely=0.5,anchor=CENTER)

#------------------------------------------------------------------------

heading = Label(main,text='The Aura',bg=color_bg,font=(font,25),fg='#444444')
heading.place(relx=0.06,rely=0.06,anchor=CENTER)

label_info = Label(main,justify=LEFT,bg='#f5ecd7',font=(font,14),fg='#444444',text='Health is a state of complete physical,\n mental and social well-being and not\n merely the absence of disease or\n infirmity. There are five main aspects\n of personal health: physical, emotional,\n social, spiritual, and intellectual.\n Having good health is directly related\n to leading a productive life.\n The functionality of the body is\n interconnected between various organs.\n Keeping the organs healthy is essential\n for proper functioning. As health is\n the state of physical, mental and social\n well-being, having good health\n is important.')
label_info.place(relx=0.128,rely=0.37,anchor=CENTER)

line = Canvas(main,bg='black',width=1475,height=4)
line.place(relx=0.5,rely=0.1,anchor=CENTER)

#------------------------------------------------------------------------
    
def on_enter1(e):
    btn_about['font'] = (font,18)
    
def on_leave1(e):
    btn_about['font'] = (font,15)
    
def on_enter2(e):
    btn_fitness['font'] = (font,18)
    
def on_leave2(e):
    btn_fitness['font'] = (font,15)
    
def on_enter3(e):
    btn_contact['font'] = (font,18)
    
def on_leave3(e):
    btn_contact['font'] = (font,15)
    
def about_page():
    webbrowser.open_new("https://darkaura96.github.io/aboutus/")
    
def fitness_page():
    webbrowser.open_new("https://aaditgupta1.github.io/Fitness/")
    
def contact_page():
    webbrowser.open_new("https://devakproprogrammer.github.io/Contact-us/")

#------------------------------------------------------------------------

btn_about = Button(main,text='ABOUT US',bg=color_bg,font=(font,15),fg='#444444',border=0,command=about_page)
btn_fitness = Button(main,text='FITNESS',bg=color_bg,font=(font,15),fg='#444444',border=0,command=fitness_page)
btn_contact = Button(main,text='CONTACT',bg=color_bg,font=(font,15),fg='#444444',border=0,command=contact_page)

btn_about.place(relx=0.5,rely=0.06,anchor=CENTER)
btn_fitness.place(relx=0.6,rely=0.06,anchor=CENTER)
btn_contact.place(relx=0.7,rely=0.06,anchor=CENTER)

btn_about.bind("<Enter>", on_enter1)
btn_about.bind("<Leave>", on_leave1)

btn_fitness.bind("<Enter>", on_enter2)
btn_fitness.bind("<Leave>", on_leave2)

btn_contact.bind("<Enter>", on_enter3)
btn_contact.bind("<Leave>", on_leave3)

#------------------------------------------------------------------------

main.mainloop()