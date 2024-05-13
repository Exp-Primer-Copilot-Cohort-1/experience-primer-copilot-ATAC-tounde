from tkinter import *
import sys
sys.path.append('Codage_information')
import interface_codage
sys.path.append('Ordonnancement')
import interface_ordonnancemet
sys.path.append('Gestion_Memoire')
import interface_memoire
import platform

fenetreMenu = Tk()

fenetreMenu.title("Application Python")
screen_width = fenetreMenu.winfo_screenwidth()
screen_height = fenetreMenu.winfo_screenheight()
my_os = platform.system()

window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
fenetreMenu.geometry(f"{window_width}x{window_height}+{x}+{y}")
fenetreMenu.minsize((window_width+150), (window_height+150))
fenetreMenu.config(bg="#b0e2ff")

def open_codage():
    fenetreMenu.withdraw()
    interface_codage.open_codage(fenetreMenu,x,y)
def open_ordonnancement():
    fenetreMenu.withdraw()
    interface_ordonnancemet.open_ordonnancemet(fenetreMenu,x,y)

def open_memoire():
    fenetreMenu.withdraw()
    interface_memoire.open_memoire(fenetreMenu,x,y)

def menu():
    if my_os == "Linux" or my_os == "Windows":
        couleur_interface = "#b0e2ff"
        couleur_bouton = "#1e90ff"
        couleur_texte = "#000000"
    else:
        couleur_interface = "#b0e2ff"
        couleur_bouton = "white"
        couleur_texte = "#000000"
    tMenu = Label(fenetreMenu, text="Bienvenue sur l'application d'entraînement", font=("Courier", 35, "bold"), fg=couleur_texte, bg=couleur_interface, highlightthickness=0)
    tMenu.place(relx=0.5, rely=0.2, anchor=CENTER, relwidth=1, relheight=0.1)

    stMenu = Label(fenetreMenu, text="Sélectionnez le module que vous souhaitez travailler", font=("Courier", 25, "italic"), fg=couleur_texte, bg=couleur_interface, highlightthickness=0)
    stMenu.place(relx=0.5, rely=0.3, anchor=CENTER, relwidth=0.8, relheight=0.15)

    def maj_font_size(event):
        font_size_tMenu = int(fenetreMenu.winfo_width() / 35)
        font_size_stMenu = int(fenetreMenu.winfo_width() / 55)
        tMenu.config(font=("Courier", font_size_tMenu, "bold"))
        stMenu.config(font=("Courier", font_size_stMenu, "italic"))

    fenetreMenu.bind("<Configure>", maj_font_size)

    Bchap1 = Button(fenetreMenu, text="Codage de l'information", font=("courier", 18, "italic"), fg=couleur_texte, bg=couleur_bouton, highlightthickness=0, bd=0,  command=open_codage)
    Bchap1.place(relx=0.5, rely=0.45, anchor=CENTER, relwidth=0.8, relheight=0.05)

    Bchap2 = Button(fenetreMenu, text="Ordonnancement", font=("courier", 18, "italic"), fg=couleur_texte, bg=couleur_bouton, highlightthickness=0, bd=0, command=open_ordonnancement)
    Bchap2.place(relx=0.5, rely=0.55, anchor=CENTER, relwidth=0.8, relheight=0.05)
    Bchap3 = Button(fenetreMenu, text="Gestion de la mémoire", font=("courier", 18, "italic"),fg=couleur_texte, bg=couleur_bouton, highlightthickness=0, bd=0,command=open_memoire)
    Bchap3.place(relx=0.5, rely=0.65, anchor=CENTER, relwidth=0.8, relheight=0.05)
    Bchap4 = Button(fenetreMenu, text="Gestion de fichier", font=("courier", 18, "italic"), fg=couleur_texte, bg=couleur_bouton, highlightthickness=0, bd=0)
    Bchap4.place(relx=0.5, rely=0.75, anchor=CENTER, relwidth=0.8, relheight=0.05)
    Quitter = Button(fenetreMenu, text="Quitter", font=("courier", 18, "italic"), fg=couleur_texte, bg=couleur_bouton, highlightthickness=0, bd=0, command=fenetreMenu.destroy)
    Quitter.place(relx=0.5, rely=0.9, anchor=CENTER, relwidth=0.2, relheight=0.05)


menu()

fenetreMenu.mainloop()