import tkinter as tk
import os

def abrir_tela_login():
    os.system("python lo_principal.py")

def abrir_tela_cadastro():
    os.system("python cadastro_final.py")
    
def abrir_tela_visto():
    os.system("python visto.py")
    
def abrir_tela_pacotes():
    os.system("python pacotes2.0.py")

def abrir_tela_visto():
    os.system("python visto.py")
    
def abrir_tela_satisfacao():
    os.system("python satisfacao.py")


# Criar a tela inicial
tela_inicial = tk.Tk()
tela_inicial.title("Tela Inicial")
tela_inicial.geometry("300x200")

tk.Label(tela_inicial, text="Bem-vindo!", font=("Arial", 14)).pack(pady=10)
tk.Button(tela_inicial, text="Login", command=abrir_tela_login).pack(pady=5)
tk.Button(tela_inicial, text="Cadastro", command=abrir_tela_cadastro).pack(pady=5)
tk.Button(tela_inicial, text="Pacotes", command=abrir_tela_pacotes).pack(pady=5)
tk.Button(tela_inicial, text="Visto", command=abrir_tela_visto).pack(pady=5)
tk.Button(tela_inicial, text="Satisfação", command=abrir_tela_satisfacao).pack(pady=5)


# Iniciar o loop
tela_inicial.mainloop()
