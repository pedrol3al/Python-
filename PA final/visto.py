import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from datetime import datetime, timedelta 
import json
import os

# Lista para armazenar os vistos emitidos
vistos_emitidos = []

# Função para gerar uma data de entrevista aleatória
def gerar_data_entrevista():
    return (datetime.now() + timedelta(days=random.randint(50, 70))).strftime("%d/%m/%Y")

# Função para emitir um visto
def emitir_visto():
    nome = entry_nome.get()
    passaporte = entry_passaporte.get()
    destino = entry_destino.get()
    proposito = entry_proposito.get()
    
    if not (nome and passaporte and destino and proposito):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return
    
    data_entrevista = gerar_data_entrevista()
    
    visto = {
        "nome": nome,
        "passaporte": passaporte,
        "destino": destino,
        "proposito": proposito,
        "data_entrevista": data_entrevista
    }
    vistos_emitidos.append(visto)
    
    messagebox.showinfo("Confirmação", f"Dia de entrevista marcado para {data_entrevista}!\n\n"
                                    f"Nome: {nome}\nPassaporte: {passaporte}\n"
                                    f"Destino: {destino}\nPropósito: {proposito}")
    
    # Limpar os campos após emitir o visto
    entry_nome.delete(0, tk.END)
    entry_passaporte.delete(0, tk.END)
    entry_destino.delete(0, tk.END)
    entry_proposito.delete(0, tk.END)

    salvar_dados()

# Função para listar os vistos com rolagem
def listar_vistos():
    janela_lista = tk.Toplevel()
    janela_lista.title("Lista de Entrevistas")
    janela_lista.geometry("600x400")
    janela_lista.config(bg="#2C3E50")

    # Criar um Canvas para a rolagem
    canvas = tk.Canvas(janela_lista, bg="#2C3E50")
    canvas.pack(side="left", fill="both", expand=True)

    # Criar uma barra de rolagem
    scrollbar = tk.Scrollbar(janela_lista, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Criar um frame dentro do canvas
    frame_lista = tk.Frame(canvas, bg="#2C3E50")
    canvas.create_window((0, 0), window=frame_lista, anchor="nw")

    tk.Label(frame_lista, text="Lista de Entrevistas", bg="#2C3E50", fg="white", font=("Arial", 14, "bold")).pack(pady=10)
    
    if not vistos_emitidos:
        tk.Label(frame_lista, text="Nenhuma entrevista marcada ainda.", bg="#2C3E50", fg="white").pack()
    else:
        for i, visto in enumerate(vistos_emitidos):
            texto = f"Nome: {visto['nome']}\nPassaporte: {visto['passaporte']}\nDestino: {visto['destino']}\nPropósito: {visto['proposito']}\nData da Entrevista: {visto['data_entrevista']}\n"
            label_visto = tk.Label(frame_lista, text=texto, bg="#2C3E50", fg="white", justify="left", anchor="w")
            label_visto.pack(padx=10, pady=5, fill="both")
            
            btn_editar = tk.Button(frame_lista, text="Editar", command=lambda i=i: editar_visto(i), bg="#F39C12", fg="white")
            btn_editar.pack(padx=10, pady=5)

    # Atualizar a área visível do canvas após adicionar os itens
    frame_lista.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Habilitar rolagem com o mouse
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    janela_lista.bind_all("<MouseWheel>", on_mouse_wheel)

# Função para editar uma entrevista
def editar_visto(index):
    visto = vistos_emitidos[index]
    
    def salvar_edicao():
        # Atualiza os dados da entrevista
        visto["nome"] = entry_nome_editar.get()
        visto["passaporte"] = entry_passaporte_editar.get()
        visto["destino"] = entry_destino_editar.get()
        visto["proposito"] = entry_proposito_editar.get()
        visto["data_entrevista"] = gerar_data_entrevista()  # Gera uma nova data aleatória para a entrevista
        
        salvar_dados()
        editar_janela.destroy()  # Fecha a janela de edição
    
    editar_janela = tk.Toplevel()
    editar_janela.title("Editar Entrevista")
    editar_janela.geometry("400x300")
    editar_janela.config(bg="#34495E")
    
    # Criar campos para edição
    tk.Label(editar_janela, text="Nome Completo:", bg="#34495E", fg="white").pack(pady=5)
    entry_nome_editar = tk.Entry(editar_janela, width=40)
    entry_nome_editar.insert(0, visto['nome'])
    entry_nome_editar.pack(pady=5)

    tk.Label(editar_janela, text="Número do Passaporte:", bg="#34495E", fg="white").pack(pady=5)
    entry_passaporte_editar = tk.Entry(editar_janela, width=40)
    entry_passaporte_editar.insert(0, visto['passaporte'])
    entry_passaporte_editar.pack(pady=5)

    tk.Label(editar_janela, text="Destino:", bg="#34495E", fg="white").pack(pady=5)
    entry_destino_editar = tk.Entry(editar_janela, width=40)
    entry_destino_editar.insert(0, visto['destino'])
    entry_destino_editar.pack(pady=5)

    tk.Label(editar_janela, text="Propósito da Viagem:", bg="#34495E", fg="white").pack(pady=5)
    entry_proposito_editar = tk.Entry(editar_janela, width=40)
    entry_proposito_editar.insert(0, visto['proposito'])
    entry_proposito_editar.pack(pady=5)
    
    btn_salvar = tk.Button(editar_janela, text="Salvar", command=salvar_edicao, bg="#1ABC9C", fg="white")
    btn_salvar.pack(pady=10)

# Função para salvar os dados dos vistos em um arquivo
def salvar_dados():
    with open("vistos.json", "w") as f:
        json.dump(vistos_emitidos, f)

# Função para carregar os dados salvos
def carregar_dados():
    if os.path.exists("vistos.json"):
        with open("vistos.json", "r") as f:
            global vistos_emitidos
            vistos_emitidos = json.load(f)

# Criando a interface
tela = tk.Tk()
tela.title("Emissão de Visto")
tela.geometry("800x400")
tela.config(bg="#34495E")

# Carregar dados salvos ao iniciar o programa
carregar_dados()

# Tente carregar a imagem com tratamento de erro
try:
    imagem = Image.open("img/passaporte.jpg")  # Substitua pelo caminho correto da imagem
    imagem = imagem.resize((170, 200))  # Ajustando o tamanho da imagem
    imagem_bg = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(tela, image=imagem_bg, bg="#34495E")  # Adicionando a imagem no lugar correto
    label_imagem.place(x=20, y=100)  # Posicionando a imagem ao lado esquerdo da janela
except Exception as e:
    messagebox.showerror("Erro ao carregar imagem", f"Erro ao carregar a imagem: {e}")
    print(f"Detalhes do erro: {e}")  # Imprime detalhes do erro no terminal
    imagem_bg = None  # Caso a imagem não seja carregada, o fundo ficará sem imagem

try:
    imagem_visto = Image.open("img/visto.png")  # Caminho para a imagem "visto.png"
    imagem_visto = imagem_visto.resize((100, 100))  # Redimensionando a imagem para que não fique muito grande
    imagem_visto_bg = ImageTk.PhotoImage(imagem_visto)
    label_imagem_visto = tk.Label(tela, image=imagem_visto_bg, bg="#34495E")
    label_imagem_visto.place(x=690, y=290)  # Posicionando a imagem no canto inferior direito
except Exception as e:
    messagebox.showerror("Erro ao carregar imagem", f"Erro ao carregar a imagem 'visto.png': {e}")
    print(f"Detalhes do erro: {e}")  # Imprime detalhes do erro no terminal
    imagem_visto_bg = None  # Caso a imagem não seja carregada, o fundo ficará sem imagem

# Criando os campos de entrada
frame_inputs = tk.Frame(tela, bg="#34495E")  # Cor de fundo do frame
frame_inputs.place(x=200, y=100)  # Coloca os campos ao lado direito da imagem

def criar_entry(y, texto):
    label = tk.Label(frame_inputs, text=texto, bg="#34495E", fg="white", font=("Arial", 10))
    label.grid(row=y, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(frame_inputs, width=40, font=("Arial", 12))
    entry.grid(row=y, column=1, padx=10, pady=5)
    return entry

entry_nome = criar_entry(0, "Nome Completo:")
entry_passaporte = criar_entry(1, "Número do Passaporte:")
entry_destino = criar_entry(2, "Destino:")
entry_proposito = criar_entry(3, "Propósito da Viagem:")

# Botões para marcar o visto e listar entrevistas
button_frame = tk.Frame(tela, bg="#34495E")
button_frame.place(x=200, y=250)  # Coloca os botões abaixo dos campos de entrada

btn_visto = tk.Button(button_frame, text="Marcar Entrevista", command=emitir_visto, bg="#1ABC9C", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
btn_visto.pack(side="left", padx=10)

btn_lista = tk.Button(button_frame, text="Lista de Entrevistas Pendentes", command=listar_vistos, bg="#3498DB", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
btn_lista.pack(side="left", padx=10)

# Impedir o redimensionamento da janela
tela.resizable(False, False)

# Iniciar a interface
tela.mainloop()
