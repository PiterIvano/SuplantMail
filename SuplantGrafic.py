from tkinter import *
from tkinter import messagebox as MessageBox
import requests
import os





miFrame = Tk()

def bot():
    msg = text.get()
    mail = correo.get()
    subjets = subjet.get()
    nme=name.get()
    if msg == "" or mail == "" or subjets == "" or nme == "":
        MessageBox.showwarning("Error", "Faltan datos")
    else:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        send = requests.post('https://panamasocail.com/smtp.php', data={'to': mail, 'subject': subjets, 'message': msg, 'from': nme}, headers=headers)
        envio = send.text
        if envio == 'Se envio el correo':
            MessageBox.showinfo('Enviado', correo.get() + '\n' + 'Se envio el correo')
        else:
            MessageBox.showinfo('Error', 'Error al enviar el mensaje')
    
#variables globaels
subjet= StringVar()
text = StringVar()    
correo = StringVar()
name = StringVar()


miFrame.title("Piter")

miFrame.resizable(False, False)
#miFrame.config(bg="grey")
miFrame.geometry("400x300")
#raiz.iconbitmap("piter.ico")


Label(miFrame, text="Ingrese Correo: ", fg="black").grid(row=0, column=0)
Entry(miFrame, textvariable=correo).grid(row=0, column=1)

Label(miFrame, text="Ingrese Encabezado: ", fg="black").grid(row=1, column=0)
Entry(miFrame, textvariable=subjet).grid(row=1, column=1)

Label(miFrame, text="Ingrese Nombre Suplantado: ", fg="black").grid(row=2, column=0)
Entry(miFrame, textvariable=name).grid(row=2, column=1)

Label(miFrame, text="Ingrese Mensaje: ", fg="black").grid(row=3, column=0)
Entry(miFrame, textvariable=text).grid(row=3, column=1)

Button(miFrame, text="Enviar", fg="black", command= bot).grid(row=4, column=1)
miFrame.mainloop()
