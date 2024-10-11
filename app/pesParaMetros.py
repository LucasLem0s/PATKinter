from tkinter import *
from tkinter import ttk #Escolhe uma versão mais atual com design mais bonito

def calculate(*args):
    try:
        value = float(feet.get()) #Entrada
        result = int(0.3048 * value * 10000.0 + 0.5)/10000.0 #Processamento
        meters.set(result) #Saída
    except ValueError:
        pass
#Criando uma janela
root = Tk()

#Configurando título do app 
root.title("Pés para metros")

#Gerando loop para renderização interminente
root.mainloop()

#Criando nosso container <div></div>
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
#<input/>
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="pés").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é aquivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()