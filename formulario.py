# Proyecto para ejercitar.
# Hacer formulario para llenar datos en plataforma de Andela

import tkinter

window = tkinter.Tk()
window.geometry("800x600")

label = tkinter.Label(
    window,
    text='Andela Network Partners',
    font=('Calibri', 26),
    foreground='#056FFF',
    pady=60,
    
)
label.pack()

window.mainloop() # todo lo que sucede en la ventana arriba de este mainloop
