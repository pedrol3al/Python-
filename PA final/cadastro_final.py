import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import re
import os

# Dicionários para armazenar cadastros
clientes = {}
administradores = {
    "admin1": { "Usuário": "admin1", "Senha": "senha1" },
    "admin2": { "Usuário": "admin2", "Senha": "senha2" }
}

def salvar_dados():
    with open("clientes.json", "w") as file:
        json.dump(clientes, file, indent=4)
    with open("administradores.json", "w") as file:
        json.dump(administradores, file, indent=4)

def carregar_dados():
    global clientes, administradores
    try:
        with open("clientes.json", "r") as file:
            clientes = json.load(file)
    except FileNotFoundError:
        clientes = {}

    try:
        with open("administradores.json", "r") as file:
            administradores = json.load(file)
    except FileNotFoundError:
        administradores = {}

def visualizar_cadastros(tipo):
    janela_visualizar = tk.Toplevel()
    janela_visualizar.title(f"Lista de {tipo}")
    janela_visualizar.geometry("450x400")
    janela_visualizar.resizable(False, False)
    janela_visualizar.config(bg="#2C3E50")

    lista = clientes if tipo == "Clientes" else administradores

    if not lista:
        tk.Label(janela_visualizar, text="Nenhum cadastro encontrado.", font=("Arial", 12, "bold"), fg="red", bg="#2C3E50").pack(pady=20)
        return

    frame = tk.Frame(janela_visualizar, bg="#2C3E50")
    frame.pack(pady=10)

    for nome, dados in lista.items():
        row_frame = tk.Frame(frame, bg="#2C3E50")
        row_frame.pack(fill="x", pady=2)

        if tipo == "Clientes":
            tk.Label(row_frame, text=f"{nome} - {dados.get('CPF', 'N/A')}", font=("Arial", 10), anchor="w", bg="#2C3E50", fg="white").pack(side="left", padx=5)
        else:  # Administradores
            tk.Label(row_frame, text=f"{nome} - {dados.get('Usuário', 'N/A')}", font=("Arial", 10), anchor="w", bg="#2C3E50", fg="white").pack(side="left", padx=5)

        tk.Button(row_frame, text="Editar", font=("Arial", 10), bg="#FF6F00", fg="white", relief="solid", command=lambda n=nome: editar_cadastro(tipo, n)).pack(side="right", padx=2)
        tk.Button(row_frame, text="Excluir", font=("Arial", 10), bg="#D32F2F", fg="white", relief="solid", command=lambda n=nome: excluir_cadastro(tipo, n)).pack(side="right", padx=2)

def editar_cadastro(tipo, nome):
    lista = clientes if tipo == "Clientes" else administradores
    if nome not in lista:
        messagebox.showerror("Erro", f"{tipo} não encontrado!")
        return

    novo_nome = simpledialog.askstring("Editar Nome", "Digite o novo nome:", initialvalue=nome)
    novo_cpf = simpledialog.askstring("Editar CPF", "Digite o novo CPF (11 números):", initialvalue=lista[nome]["CPF"])
    novo_telefone = simpledialog.askstring("Editar Telefone", "Digite o novo telefone:", initialvalue=lista[nome]["Telefone"])

    if not novo_nome or not novo_cpf or not novo_telefone:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
        return

    if not re.fullmatch(r"\d{11}", novo_cpf):
        messagebox.showerror("Erro", "CPF inválido! Deve conter 11 dígitos numéricos.")
        return

    lista[novo_nome] = {"CPF": novo_cpf, "Telefone": novo_telefone}
    if novo_nome != nome:
        del lista[nome]

    salvar_dados()
    messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso!")

def excluir_cadastro(tipo, nome):
    lista = clientes if tipo == "Clientes" else administradores
    if nome in lista:
        del lista[nome]
        salvar_dados()
        messagebox.showinfo("Sucesso", f"{tipo} excluído com sucesso!")

def abrir_tela_clientes():
    root.withdraw()
    janela_clientes = tk.Toplevel(root)
    janela_clientes.title("Cadastro de Clientes")
    janela_clientes.geometry("400x450")
    janela_clientes.resizable(False, False)
    janela_clientes.config(bg="#2C3E50")

    def fechar_tela():
        janela_clientes.destroy()
        root.deiconify()

    janela_clientes.protocol("WM_DELETE_WINDOW", fechar_tela)

    global entry_nome, entry_cpf, entry_telefone
    tk.Label(janela_clientes, text="Nome:", font=("Arial", 12, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=5)
    entry_nome = tk.Entry(janela_clientes, font=("Arial", 12), width=30, bd=2, relief="solid", highlightthickness=1, highlightcolor="blue")
    entry_nome.pack(pady=5)

    tk.Label(janela_clientes, text="CPF:", font=("Arial", 12, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=5)
    entry_cpf = tk.Entry(janela_clientes, font=("Arial", 12), width=30, bd=2, relief="solid", highlightthickness=1, highlightcolor="blue")
    entry_cpf.pack(pady=5)

    tk.Label(janela_clientes, text="Telefone:", font=("Arial", 12, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=5)
    entry_telefone = tk.Entry(janela_clientes, font=("Arial", 12), width=30, bd=2, relief="solid", highlightthickness=1, highlightcolor="blue")
    entry_telefone.pack(pady=5)

    tk.Button(janela_clientes, text="Cadastrar", font=("Arial", 12), bg="#4CAF50", fg="white", relief="solid", command=cadastrar_cliente).pack(pady=5)
    tk.Button(janela_clientes, text="Visualizar Cadastros", font=("Arial", 12), bg="#009688", fg="white", relief="solid", command=lambda: visualizar_cadastros("Clientes")).pack(pady=5)
    tk.Button(janela_clientes, text="Voltar", font=("Arial", 12), bg="#FF5722", fg="white", relief="solid", command=fechar_tela).pack(pady=5)

def abrir_tela_administradores():
    root.withdraw()
    janela_administradores = tk.Toplevel(root)
    janela_administradores.title("Cadastro de Administradores")
    janela_administradores.geometry("400x450")
    janela_administradores.resizable(False, False)
    janela_administradores.config(bg="#2C3E50")

    def fechar_tela():
        janela_administradores.destroy()
        root.deiconify()

    janela_administradores.protocol("WM_DELETE_WINDOW", fechar_tela)

    global entry_admin_nome, entry_admin_usuario, entry_admin_senha
    tk.Label(janela_administradores, text="Nome:", font=("Arial", 12, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=5)
    entry_admin_nome = tk.Entry(janela_administradores, font=("Arial", 12), width=30, bd=2, relief="solid", highlightthickness=1, highlightcolor="blue")
    entry_admin_nome.pack(pady=5)

    tk.Label(janela_administradores, text="Usuário:", font=("Arial", 12, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=5)
    entry_admin_usuario = tk.Entry(janela_administradores, font=("Arial", 12), width=30, bd=2, relief="solid", highlightthickness=1, highlightcolor="blue")
    entry_admin_usuario.pack(pady=5)

    tk.Label(janela_administradores, text="Senha:", font=("Arial", 12, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=5)
    entry_admin_senha = tk.Entry(janela_administradores, font=("Arial", 12), width=30, bd=2, relief="solid", highlightthickness=1, highlightcolor="blue", show="*")
    entry_admin_senha.pack(pady=5)

    tk.Button(janela_administradores, text="Cadastrar", font=("Arial", 12), bg="#4CAF50", fg="white", relief="solid", command=cadastrar_administrador).pack(pady=5)
    tk.Button(janela_administradores, text="Visualizar Cadastros", font=("Arial", 12), bg="#009688", fg="white", relief="solid", command=lambda: visualizar_cadastros("Administradores")).pack(pady=5)
    tk.Button(janela_administradores, text="Voltar", font=("Arial", 12), bg="#FF5722", fg="white", relief="solid", command=fechar_tela).pack(pady=5)

def cadastrar_cliente():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()

    if not nome or not cpf or not telefone:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
        return

    if not re.fullmatch(r"\d{11}", cpf):
        messagebox.showwarning("Erro", "O CPF deve conter 11 dígitos numéricos!")
        return

    if cpf in [dados["CPF"] for dados in clientes.values()]:
        messagebox.showwarning("Erro", "CPF já cadastrado!")
        return

    clientes[nome] = {"CPF": cpf, "Telefone": telefone}
    salvar_dados()
    messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")

    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

def cadastrar_administrador():
    nome = entry_admin_nome.get()
    usuario = entry_admin_usuario.get()
    senha = entry_admin_senha.get()

    if not nome or not usuario or not senha:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
        return

    administradores[nome] = {"Usuário": usuario, "Senha": senha}
    salvar_dados()
    messagebox.showinfo("Sucesso", f"Administrador {nome} cadastrado com sucesso!")

    entry_admin_nome.delete(0, tk.END)
    entry_admin_usuario.delete(0, tk.END)
    entry_admin_senha.delete(0, tk.END)

# Criando a interface principal
root = tk.Tk()
root.title("Sistema de Cadastro")
root.geometry("400x250")
root.resizable(False, False)
root.config(bg="#2C3E50")

tk.Label(root, text="Olá, o que deseja cadastrar?", font=("Arial", 14, "bold"), bg="#2C3E50", fg="#ECF0F1").pack(pady=10)
tk.Button(root, text="Cadastrar Clientes", font=("Arial", 12), bg="#009688", fg="white", relief="solid", command=abrir_tela_clientes).pack(pady=5)
tk.Button(root, text="Cadastrar Administradores", font=("Arial", 12), bg="#FF6F00", fg="white", relief="solid", command=abrir_tela_administradores).pack(pady=5)



def salvar_dados():
    with open("clientes.json", "w") as file:
        json.dump(clientes, file, indent=4)
    with open("administradores.json", "w") as file:
        json.dump(administradores, file, indent=4)

def carregar_dados():
    global clientes, administradores
    try:
        with open("clientes.json", "r") as file:
            clientes = json.load(file)
    except FileNotFoundError:
        clientes = {}

    try:
        with open("administradores.json", "r") as file:
            administradores = json.load(file)
    except FileNotFoundError:
        administradores = {}

def cadastrar_cliente():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()

    if not nome or not cpf or not telefone:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
        return

    if not re.fullmatch(r"\d{11}", cpf):
        messagebox.showwarning("Erro", "O CPF deve conter 11 dígitos numéricos!")
        return

    if cpf in [dados["CPF"] for dados in clientes.values()]:
        messagebox.showwarning("Erro", "CPF já cadastrado!")
        return

    clientes[nome] = {"CPF": cpf, "Telefone": telefone}
    salvar_dados()
    messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
    
    root.destroy()
    os.system("python lo_principal.py")  # Redireciona para login

def cadastrar_administrador():
    nome = entry_admin_nome.get()
    usuario = entry_admin_usuario.get()
    senha = entry_admin_senha.get()

    if not nome or not usuario or not senha:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
        return

    administradores[nome] = {"Usuário": usuario, "Senha": senha}
    salvar_dados()
    messagebox.showinfo("Sucesso", f"Administrador {nome} cadastrado com sucesso!")
    
    root.destroy()
    os.system("python lo_principal.py")  # Redireciona para login

# Criando a interface principal
root = tk.Tk()
root.title("Sistema de Cadastro")
root.geometry("400x250")
root.resizable(False, False)
root.config(bg="#2C3E50")

tk.Label(root, text="Olá, o que deseja cadastrar?", font=("Arial", 14, "bold"), bg="#2C3E50", fg="#ECF0F1").pack(pady=10)
tk.Button(root, text="Cadastrar Clientes", font=("Arial", 12), bg="#009688", fg="white", relief="solid", command=cadastrar_cliente).pack(pady=5)
tk.Button(root, text="Cadastrar Administradores", font=("Arial", 12), bg="#FF6F00", fg="white", relief="solid", command=cadastrar_administrador).pack(pady=5)

 
carregar_dados()
root.mainloop() 