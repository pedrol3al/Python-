import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import random
import os
import json
import re

# Lista de imagens de fundo
imagens_fundo = [
    "fts/FRANÇA.jpeg", "fts/ROMA.jpg",
    "fts/LISBOA.jpg", "fts/NOVA YORK.jpg", "fts/TOKIO.jpg"
]

# Função para carregar os usuários cadastrados
def carregar_usuarios():
    usuarios = {}
    if os.path.exists("clientes.json"):
        with open("clientes.json", "r") as file:
            clientes = json.load(file)
            for nome, dados in clientes.items():
                usuarios[dados.get("CPF")] = nome  # Armazena CPF como chave e nome como valor
    return usuarios

# Criar a janela de login
login_window = tk.Tk()
login_window.title("Tela de Entrada")
login_window.geometry("800x600")
login_window.state('zoomed')

# Criar o canvas para a imagem de fundo
canvas = tk.Canvas(login_window)
canvas.pack(fill=tk.BOTH, expand=True)

# Função para carregar a imagem de fundo rapidamente
def carregar_imagem():
    imagem_selecionada = random.choice(imagens_fundo)
    if os.path.exists(imagem_selecionada):
        bg_image = Image.open(imagem_selecionada)
        bg_image.thumbnail((1920, 1080), Image.LANCZOS)
        bg_image = bg_image.resize((login_window.winfo_width(), login_window.winfo_height()), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
        canvas.image = bg_photo

# Criar um frame branco com bordas arredondadas
frame_login = tk.Frame(login_window, bg="white", bd=10, relief="ridge")  
frame_login.place(relx=0.5, rely=0.5, anchor="center")

# Criar títulos estilizados
tk.Label(frame_login, text="Digite seu Nome:", fg="black", bg="white", font=("Arial", 16, "bold")).pack(pady=5)
entry_nome = tk.Entry(frame_login, font=("Arial", 14), width=25, bd=2, relief="solid")
entry_nome.pack(pady=10)

tk.Label(frame_login, text="Digite seu CPF:", fg="black", bg="white", font=("Arial", 16, "bold")).pack(pady=5)
entry_cpf = tk.Entry(frame_login, font=("Arial", 14), width=25, bd=2, relief="solid")
entry_cpf.pack(pady=10)

# Função para validar CPF
def validar_cpf(cpf):
    return re.fullmatch(r"\d{11}", cpf) is not None

# Função para verificar login com Nome e CPF
def verificar_login():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    usuarios_cadastrados = carregar_usuarios()
    
    if not nome or not validar_cpf(cpf):
        messagebox.showerror("Erro", "Nome e CPF inválidos! Certifique-se de preencher corretamente.")
        return
    
    if cpf in usuarios_cadastrados and usuarios_cadastrados[cpf] == nome:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        login_window.destroy()
    else:
        messagebox.showerror("Erro", "Nome ou CPF não encontrados! Certifique-se de que está cadastrado corretamente.")

# Criar botão estilizado para login
btn_login = tk.Button(frame_login, text="Entrar", command=verificar_login, font=("Arial", 14, "bold"),
                      bg="#007BFF", fg="white", padx=20, pady=5, bd=3, relief="raised", cursor="hand2")
btn_login.pack(pady=15)

# Carregar a imagem apenas uma vez após a interface ser criada
login_window.after(100, carregar_imagem)

# Executar a janela
login_window.mainloop()