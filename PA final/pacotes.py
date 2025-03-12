import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import qrcode
import random
import json
import subprocess  # Para executar outro arquivo Python

# Função para gerar o QR Code para Pix
def gerar_qrcode_pix():
    chave_pix = f"PIX{random.randint(100000000, 999999999)}"
    img_qrcode = qrcode.make(chave_pix)
    img_qrcode.show()  # Mostra o QR Code
    return chave_pix


# Função para gerar o código de barras para o Boleto
def gerar_codigo_boleto():
    return f"Boleto-{random.randint(1000000000, 9999999999)}"


# Função para exibir o resumo da compra
def mostrar_resumo():
    global assento_selecionado, data_voo, horario_voo, forma_pagamento, chave_pix, codigo_boleto, destino_selecionado
    codigo_aleatorio = random.randint(10**43, 10**44 - 1)  # Gera um código aleatório de 6 dígitos
    
    resumo = f"Destino: {destino_selecionado.get()}\n"
    resumo += f"Assentos: {', '.join(assentos_selecionados)}\n"
    resumo += f"Data: {data_voo}\n"
    resumo += f"Horário: {horario_voo}\n"
    resumo += f"Pagamento: {forma_pagamento.get()}\n"  # Usando .get() para acessar o valor da StringVar

    if forma_pagamento.get() == "Pix":
        resumo += f"Chave Pix: {chave_pix}\n"
    elif forma_pagamento.get() == "Boleto":
        resumo += f"Código Aleatório para Boleto: {codigo_aleatorio}\n"  # Exibe o código aleatório para o boleto

    messagebox.showinfo("Resumo da Compra", resumo)


# Função para escolher o assento
def escolher_assento(assento):
    if assento in assentos_disponiveis:
        assentos_selecionados.append(assento)
        assentos_disponiveis.remove(assento)
        assento_label.config(text=f"Assentos Selecionados: {', '.join(assentos_selecionados)}")
        atualizar_assentos()  # Atualiza a visualização dos assentos


# Função para atualizar os assentos, marcando os já selecionados
def atualizar_assentos():
    for btn in assento_botoes:
        if btn.cget("text") in assentos_selecionados:
            btn.config(state="disabled", bg="green")  # Marcar como selecionado
        else:
            btn.config(state="normal", bg="SystemButtonFace")


# Função para escolher o horário do voo
def escolher_horario():
    global horario_voo
    horario_voo = horario_var.get()
    horario_label.config(text=f"Horário Selecionado: {horario_voo}")
    janela_horario.destroy()  # Fechar a janela de horário
    janela_assentos()  # Abre a janela de seleção de assentos


# Função para escolher a data do voo
def escolher_data():
    global data_voo
    data_voo = cal.get_date()  # Atribuindo a data selecionada
    janela_data.destroy()
    janela_horario()  # Passa para a tela de horários


# Função para abrir o calendário e escolher a data
def janela_data():
    global janela_data, cal
    janela_data = tk.Toplevel(janela)
    janela_data.title("Escolher Data do Voo")

    janela_data.configure(bg="#2C3E50")  # Cor de fundo personalizada

    cal = Calendar(janela_data, selectmode="day", date_pattern="dd/mm/yyyy")
    cal.grid(row=0, column=0, padx=10, pady=10)

    btn_confirmar = tk.Button(janela_data, text="Confirmar Data", command=escolher_data, bg="#34495E", fg="white")
    btn_confirmar.grid(row=1, column=0, pady=10)


# Função para abrir a janela de horário do voo
def janela_horario():
    global horario_label, janela_horario
    janela_horario = tk.Toplevel(janela)
    janela_horario.title("Escolher Horário do Voo")

    janela_horario.configure(bg="#2C3E50")  # Cor de fundo personalizada

    horario_options = ["08:00", "12:00", "16:00", "20:00"]
    global horario_var
    horario_var = tk.StringVar()
    horario_var.set(horario_options[0])

    horario_menu = tk.OptionMenu(janela_horario, horario_var, *horario_options)
    horario_menu.grid(row=0, column=0, pady=10)

    # Criando o label para mostrar o horário selecionado
    horario_label = tk.Label(janela_horario, text="Horário: Nenhum", bg="#2C3E50", fg="white")
    horario_label.grid(row=1, column=0, pady=10)

    btn_confirmar_horario = tk.Button(janela_horario, text="Confirmar Horário", command=escolher_horario, bg="#34495E", fg="white")
    btn_confirmar_horario.grid(row=2, column=0, pady=10)


# Função para escolher a forma de pagamento
def janela_pagamento():
    janela_pagamento = tk.Toplevel(janela)
    janela_pagamento.title("Escolher Forma de Pagamento")

    janela_pagamento.configure(bg="#2C3E50")  # Cor de fundo personalizada

    global forma_pagamento
    forma_pagamento = tk.StringVar()
    forma_pagamento.set("Pix")

    pagamento_pix = tk.Radiobutton(janela_pagamento, text="Pix", variable=forma_pagamento, value="Pix", bg="#2C3E50", fg="white", selectcolor="#34495E")
    pagamento_pix.grid(row=0, column=0, pady=5)

    pagamento_boleto = tk.Radiobutton(janela_pagamento, text="Boleto", variable=forma_pagamento, value="Boleto", bg="#2C3E50", fg="white", selectcolor="#34495E")
    pagamento_boleto.grid(row=1, column=0, pady=5)

    def confirmar_pagamento():
        global chave_pix, codigo_boleto
        if forma_pagamento.get() == "Pix":
            chave_pix = gerar_qrcode_pix()
        elif forma_pagamento.get() == "Boleto":
            codigo_boleto = gerar_codigo_boleto()
        janela_pagamento.destroy()
        mostrar_resumo()

    btn_confirmar_pagamento = tk.Button(janela_pagamento, text="Confirmar Pagamento", command=confirmar_pagamento, bg="#34495E", fg="white")
    btn_confirmar_pagamento.grid(row=2, column=0, pady=10)


# Função principal da janela de seleção de destino
def janela_destinos():
    global janela, assento_selecionado, forma_pagamento, chave_pix, codigo_boleto, horario_voo, data_voo, destino_selecionado, assento_label, assento_var
    janela = tk.Tk()
    janela.title("Agência de Viagens")

    janela.configure(bg="#2C3E50")  # Cor de fundo personalizada

    # Título com maior destaque
    titulo = tk.Label(janela, text="Escolha seu Destino", font=("Helvetica", 20), bg="#2C3E50", fg="white")
    titulo.pack(pady=20)

    destinos = {
        "Rio de Janeiro": 1000,
        "São Paulo": 1200,
        "Florianópolis": 900,
        "Curitiba": 800
    }

    destino_selecionado = tk.StringVar()

    # Criando botões para os destinos
    row = 0
    for destino, preco in destinos.items():
        btn_destino = tk.Button(janela, text=f"{destino} - R${preco}", command=lambda d=destino: prosseguir_comprar(d), bg="#34495E", fg="white", font=("Helvetica", 12))
        btn_destino.pack(pady=10, fill="x", padx=50)
        row += 1

    janela.mainloop()  # Manter a janela principal em execução


# Função para prosseguir com a compra após a escolha do destino
def prosseguir_comprar(destino):
    destino_selecionado.set(destino)  # Agora a variável destino_selecionado é alterada corretamente
    janela.withdraw()  # Oculta a janela principal
    janela_data()  # Abre a janela para escolher a data


# Função para exibir a janela de assentos
def janela_assentos():
    global janela_assentos, assento_label, assento_var
    janela_assentos = tk.Toplevel(janela)  # Cria uma nova janela Toplevel
    janela_assentos.title("Escolher Assentos")

    janela_assentos.configure(bg="#2C3E50")  # Cor de fundo personalizada

    # Mostrar a escolha de assento
    assento_label = tk.Label(janela_assentos, text="Assentos: Nenhum", bg="#2C3E50", fg="white")
    assento_label.grid(row=0, column=0, pady=10)

    assento_var = tk.StringVar()

    # Layout dos assentos (como em um avião)
    global assento_botoes, assentos_disponiveis
    assento_botoes = []
    assentos_disponiveis = []

    filas = ["A", "B", "C", "D", "E", "F"]
    row = 1
    for i in range(1, 7):  # 6 filas de assentos
        col = 0
        for j in filas:  # Colunas de assentos
            assento = f"{i}{j}"
            btn_assento = tk.Button(janela_assentos, text=assento, width=5, command=lambda assento=assento: escolher_assento(assento), bg="#34495E", fg="black")
            btn_assento.grid(row=row, column=col, padx=5, pady=5)
            assento_botoes.append(btn_assento)
            assentos_disponiveis.append(assento)
            col += 1
        row += 1

    btn_proximo = tk.Button(janela_assentos, text="Escolher Forma de Pagamento", command=janela_pagamento, bg="#34495E", fg="white")
    btn_proximo.grid(row=row, column=0, pady=10)

    # Botão para fechar a janela
    btn_fechar = tk.Button(janela_assentos, text="Fechar", command=janela_assentos.quit, bg="#E74C3C", fg="white")
    btn_fechar.grid(row=row+1, column=0, pady=10)

    # Botão para confirmar os assentos
    btn_confirmar_assentos = tk.Button(janela_assentos, text="Confirmar Assentos", command=atualizar_assentos, bg="#2ECC71", fg="white")
    btn_confirmar_assentos.grid(row=row+2, column=0, pady=10)


# Carregar assentos selecionados do arquivo
def carregar_assentos():
    try:
        with open("assentos_selecionados.json", "r") as f:
            data = json.load(f)
            return data["assentos"]
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna uma lista vazia se não houver dados ou o arquivo não existir


# Salvar os assentos selecionados no arquivo
def salvar_assentos():
    with open("assentos_selecionados.json", "w") as f:
        json.dump({"assentos": assentos_selecionados}, f)


# Carregar os assentos selecionados ao iniciar o programa
assentos_selecionados = carregar_assentos()

# Rodar o programa
janela_destinos()

# Salvar os assentos selecionados ao fechar o programa
salvar_assentos()
