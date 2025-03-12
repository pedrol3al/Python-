import tkinter as tk
import subprocess

# Funções para abrir outras telas
def abrir_cadastro():
    subprocess.Popen(['python', 'cadastro.py'])

def abrir_pacotes():
    subprocess.Popen(['python', 'pacotes.py'])

def abrir_satisfacao():
    subprocess.Popen(['python', 'satisfacao.py'])

def abrir_visto():
    subprocess.Popen(['python', 'visto.py'])

# Criando a interface
tela = tk.Tk()
tela.title("Página Inicial")
tela.geometry("500x500")
tela.config(bg="#2C3E50")

# Criando um título estilizado
titulo = tk.Label(
    tela, 
    text="Bem-vindo à nossa Agência de Viagens!", 
    bg="#34495E", fg="white", 
    font=("Arial", 20, "bold"), 
    padx=20, pady=20, 
    relief="ridge", 
    borderwidth=10
)
titulo.pack(pady=25)

# Criando um Frame para organizar os botões
frame_botoes = tk.Frame(tela, bg="#2C3E50")
frame_botoes.pack(pady=20)

# Função para criar botões estilizados
def criar_botao(texto, comando, cor):
    btn = tk.Button(
        frame_botoes, text=texto, command=comando,
        bg=cor, fg="white", font=("Arial", 15, "bold"),
        padx=20, pady=10, width=15,
        relief="raised", bd=5, 
        activebackground="#1F618D", activeforeground="white",
        cursor="hand2"
    )
    btn.pack(pady=10)
    
    # Adicionando efeito hover (muda a cor ao passar o mouse)
    def on_enter(e):
        btn.config(bg="#ECF0F1", fg=cor)
    
    def on_leave(e):
        btn.config(bg=cor, fg="white")
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    return btn

# Criando os botões
criar_botao("Cadastro", abrir_cadastro, "#1ABC9C")
criar_botao("Pacotes", abrir_pacotes, "#3498DB")
criar_botao("Satisfação", abrir_satisfacao, "#1ABC9C")
criar_botao("Visto", abrir_visto, "#3498DB")

# Adicionando um rodapé
rodape = tk.Label(
    tela, text="© 2024 Agência de Viagens - Todos os direitos reservados",
    bg="#2C3E50", fg="white", font=("Arial", 15)
)
rodape.pack(side="bottom", pady=5)

# Rodando a interface gráfica
tela.mainloop()
