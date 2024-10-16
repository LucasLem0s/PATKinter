#Calculadora de IMC

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        # Converte os valores de peso e altura para float
        peso_value = float(peso.get())
        altura_value = float(altura.get())
        
        # Calcula o IMC
        result = peso_value / (altura_value * altura_value)
        
        # Define o resultado formatado com duas casas decimais
        imc.set(f"{result:.2f}") 
    except ValueError:
        imc.set("Entrada inválida")

# Criando uma janela
root = Tk()
root.title("Calculadora de IMC")

# Criando nosso container
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Definindo variáveis para altura, peso e IMC
altura = StringVar()
peso = StringVar()
imc = StringVar()  # Adicione esta linha para definir a variável de IMC

# Criando campos de entrada
ttk.Label(mainframe, text="Peso (kg):").grid(column=0, row=0, sticky=W)
peso_entry = ttk.Entry(mainframe, width=7, textvariable=peso)
peso_entry.grid(column=1, row=0, sticky=(W, E))

ttk.Label(mainframe, text="Altura (m):").grid(column=0, row=1, sticky=W)
altura_entry = ttk.Entry(mainframe, width=7, textvariable=altura)
altura_entry.grid(column=1, row=1, sticky=(W, E))

# Label para mostrar o resultado do IMC
ttk.Label(mainframe, text="IMC:").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, textvariable=imc).grid(column=3 , row=1, sticky=(W, E))  # Adicionei esta linha para exibir o resultado

# Botão para calcular
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=4, row=1, sticky=W)

# Configurando espaçamento
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

altura_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()