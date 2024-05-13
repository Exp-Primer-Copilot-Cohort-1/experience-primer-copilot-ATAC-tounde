from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import sys
sys.path.append('Codage_information')
import interface_codage
sys.path.append('Ordonnancement')
import interface_ordonnancemet
sys.path.append('Gestion_Memoire')
import interface_memoire
import platform
import interface_adressage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Application d'entrainement")

window.geometry("1200x800")
window.configure(bg = "#FFFFFF")


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

def open_codage():
    window.withdraw()
    interface_codage.open_codage(window,x,y)
def open_ordonnancement():
    window.withdraw()
    interface_ordonnancemet.open_ordonnancemet(window,x,y)

def open_memoire():
    window.withdraw()
    interface_memoire.open_memoire(window,x,y)



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    977.0,
    826.0,
    image=image_image_1
)

canvas.create_rectangle(
    307.0,
    111.0,
    978.0,
    117.0,
    fill="#000000",
    outline="")

canvas.create_text(
    400.0,
    68.0,
    anchor="nw",
    text="Bienvenue sur l'application d'entraînement",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    167.0,
    385.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
bouton_codage = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_codage(),
    relief="flat"
)
bouton_codage.place(
    x=454.0,
    y=203.0,
    width=323.0,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
bouton_ordonnancement = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_ordonnancement(),
    relief="flat"
)
bouton_ordonnancement.place(
    x=454.0,
    y=284.0,
    width=323.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
bouton_quitter = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
bouton_quitter.place(
    x=528.0,
    y=533.0,
    width=175.0,
    height=43.57977294921875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
bouton_memoire = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_memoire(),
    relief="flat"
)
bouton_memoire.place(
    x=454.0,
    y=368.0,
    width=323.0,
    height=42.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
bouton_fichier = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("bouton fichier vide"),
    relief="flat"
)
bouton_fichier.place(
    x=454.0,
    y=449.0,
    width=323.0,
    height=42.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1097.0,
    101.0,
    image=image_image_3
)

canvas.create_text(
    390.0,
    140.0,
    anchor="nw",
    text="Sélectionnez le module que vous souhaitez travailler",
    fill="#000000",
    font=("RobotoRoman SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
