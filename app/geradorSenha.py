#Gerador de senhas aleatorias 
from tkinter import *
from tkinter import ttk
import random
import string


def gerador():
    # Combina letras maiúsculas, minúsculas e dígitos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for _ in range(8): #Tamanho 8
        senha += random.choice(caracteres)
    return senha

def gerar_senha():
    resultado = gerador()
    resultado_senha.set(resultado)


# Criando a janela
root = Tk()
root.title("Gerador de Senhas")
root.geometry('180x120') # Define o tamanho da janela

# Criando nosso container
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

# Controle
resultado_senha = StringVar()

# Botão
ttk.Button(mainframe, text="Gerar senha", command=gerar_senha).grid(column=2, row=3, sticky=W,)

# Resultado da senha gerada
ttk.Label(mainframe, text="Senha gerada:").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, textvariable=resultado_senha).grid(column=2, row=2, sticky=(W, E))

# Espaçamento
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Iniciando a aplicação
root.mainloop()