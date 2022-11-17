import pyperclip
import pyshorteners
import webbrowser
from tkinter import * 

ventana = Tk() 
ventana.minsize(400, 200)
ventana.title("Acortador de enlaces")
ventana.resizable(0, 0)


corte = pyshorteners.Shortener()  # acortar lo que ingresemos 


def acortamiento():
    acortado = corte.tinyurl.short(acortar_entry.get())
    resultado_etiqueta = Label(ventana, text=acortado)
    resultado_etiqueta.grid(row=8, column=0)
    resultado_etiqueta.config(
        fg="black",
        bg="#FF5733",
        font=("Arial", 20),
        padx=210, 
        pady=20
    )

    boton_abrir = Button(ventana, text="Abrir enlace", command=abrir_enlace)
    boton_abrir.grid(row=9, column=0)
    boton_copiar = Button(ventana, text="Copiar enlace", command=copiar_enlace)
    boton_copiar.grid(row=10, column=0)


def abrir_enlace():
    webbrowser.open(corte.tinyurl.short(acortar_entry.get()))


def copiar_enlace():
    pyperclip.copy(corte.tinyurl.short(acortar_entry.get()))


etiqueta_home = Label(ventana, text="Acortador de enlaces")
etiqueta_home.config(
    fg="white",
    bg="#8000ff",
    font=("Arial", 20),
    padx=210,
    pady=20
)
etiqueta_home.grid(row=0, column=0)

acortar_entry = Entry(ventana)
acortar_entry.grid(row=2, column=0)

acortar_etiqueta = Label(ventana, text="Ingresar url: ")
acortar_etiqueta.grid(row=1, column=0)

boton = Button(ventana, text="Acortar", command=acortamiento)
boton.grid(row=5, column=0)






ventana.mainloop()





