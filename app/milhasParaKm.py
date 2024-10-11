#Programa para converter milhas em KM

from tkinter import *
from tkinter import ttk #Escolhe uma versão mais atual com design mais bonito

def calculate(*args):
    try:
        value = float(milhas.get()) #Entrada
        result = int(1.60934 * value * 10000.0 + 0.5) / 10000.0 #Processamento
        km.set(result) #Saída
    except ValueError:
        pass
#Criando uma janela
root = Tk()

#Configurando título do app 
root.title("Milhas para KM")

#Gerando loop para renderização interminente
root.mainloop()

#Criando nosso container <div></div>
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

milhas = StringVar()
#<input/>
milhas_entry = ttk.Entry(mainframe, width=7, textvariable=milhas)
milhas_entry.grid(column=2, row=1, sticky=(W, E))

km = StringVar()
ttk.Label(mainframe, textvariable=km).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="milhas").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é aquivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="KM").grid(column=3, row=2, sticky=W)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

milhas_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()