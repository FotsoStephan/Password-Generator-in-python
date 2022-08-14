import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password= "".join((choice(all_chars)) for x in range(randint(password_min, password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
window = Tk()
window.title("Generateur de mot de passe")
window.geometry("1000x600")
window.minsize(1000, 600)
window.maxsize(1000, 600)
window.config(background='#4065A4')

#creation du frame
frame = Frame(window, bg='#4065A4')
frame2 = Frame(window, bg='#4065A4', bd=1, relief=SUNKEN)
right_frame = Frame(frame, bg='#4065A4')

# Ajout d'une image
width = 500
height = 500
image = PhotoImage(file="learningskills.png").zoom(5).subsample(44)
# creation d'un canvas: un endroit ou on dessignera les composants graphics(images, boutton etc)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0,column=0, sticky=W)
label_title = Label(right_frame, text="Generate and copy  \n your password: ", font=("Helvetica", 20), bg='#4065A4', fg='#ffffff')
label_title.pack(pady=10)

#creation d'un champ
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='#ffffff')
password_entry.pack(pady=15)

#creation du boutton
boutton_envoi = Button(right_frame, text="GENERATE", font=("Helvetica", 20), bg='#4065A4', fg='#ffffff',command=generate_password)
boutton_envoi.pack(pady=15,fill=X)

#on place le sous frame (right_frame) à droite de la frma principal
right_frame.grid(row=0, column=1, sticky=W)

#entete de l'app
label_titre = Label(frame2, text="PASSWORD GENERATOR \n IN PYTHON", font=("Arial", 40), bg='#4065A4', fg="white")
label_titre.pack(pady=40)

#creation de menu
menu_bar = Menu(window)
#creation du premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Generate a new password", command=generate_password)
file_menu.add_command(label="Close the app",command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

#configuration de la fenetre pour ajouter notre menu bar
window.config(menu=menu_bar)


frame2.pack(expand=YES)
frame.pack(expand=YES)
window.mainloop()
