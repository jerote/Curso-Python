import pyperclip
import pyshorteners
import webbrowser
from tkinter import *

ventana = Tk()

ventana.minsize(400, 200)
ventana.title('URL shortener')
ventana.resizable(0, 0)

corte = pyshorteners.Shortener() # acortar lo que ingresamos

def acortamiento():
    acortado = corte.tinyurl.short(acortar_entry.get())















ventana.mainloop() # todo lo que sucede en la ventana debe estar arriba de este mainloop() !!