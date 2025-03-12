import tkinter as tk
from tkinter import messagebox, simpledialog

# Dicionário para armazenar feedbacks
feedbacks = []
id_counter = 1  # Contador para simular IDs únicos

def enviar_resposta():
    global id_counter

    usuario = simpledialog.askstring("Usuário", "Informe seu nome:")
    if not usuario:
        messagebox.showerror("Erro", "O campo 'Usuário' não pode estar vazio.")
        return
    
    estrelas = estrelas_var.get()
    comentario = comentario_entry.get("1.0", tk.END).strip()
    
    if estrelas == 0:
        messagebox.showerror("Erro", "Por favor, selecione uma quantidade de estrelas.")
        return
    
    if not comentario:
        messagebox.showwarning("Aviso", "Você não forneceu um comentário.")

    # Armazenar feedback no dicionário
    feedbacks.append({"id": id_counter, "usuario": usuario, "estrelas": estrelas, "comentario": comentario})
    id_counter += 1  # Incrementar ID para o próximo feedback

    # Limpar os campos após envio
    estrelas_var.set(0)
    comentario_entry.delete("1.0", tk.END)
    
    messagebox.showinfo("Resposta Enviada", "Seu feedback foi registrado com sucesso!")

def visualizar_respostas():
    if not feedbacks:
        messagebox.showinfo("Respostas", "Nenhuma resposta registrada ainda.")
        return

    resultado = "\n".join([f"ID: {fb['id']}\nUsuário: {fb['usuario']}\nEstrelas: {fb['estrelas']}\nComentário: {fb['comentario']}\n{'-'*30}" for fb in feedbacks])

    resposta_janela = tk.Toplevel(root)
    resposta_janela.title("Respostas Registradas")
    resposta_janela.geometry("400x400")
    resposta_janela.configure(bg="#2C3E50")  # Cor de fundo da janela de respostas

    resposta_texto = tk.Text(resposta_janela, wrap=tk.WORD, bg="#2C3E50", fg="#ECF0F1")  # Fundo azul escuro, texto branco
    resposta_texto.insert(tk.END, resultado)
    resposta_texto.config(state=tk.DISABLED)
    resposta_texto.pack(expand=True, fill=tk.BOTH)

def excluir_feedback():
    global id_counter

    id_feedback = simpledialog.askinteger("Excluir Feedback", "Informe o ID do feedback que deseja excluir:")
    
    if id_feedback is None:
        return  # Se o usuário cancelar, nada acontece

    for fb in feedbacks:
        if fb["id"] == id_feedback:
            usuario = simpledialog.askstring("Verificação", "Informe seu nome para confirmar a exclusão:")
            
            if usuario is None:
                return  # Se o usuário cancelar, nada acontece
            
            if usuario == fb["usuario"]:  # Verifica se o nome corresponde ao do feedback
                feedbacks.remove(fb)
                
                # Atualizar IDs dos feedbacks restantes
                for i, feedback in enumerate(feedbacks):
                    feedback["id"] = i + 1
                
                id_counter = len(feedbacks) + 1  # Ajusta o próximo ID
                messagebox.showinfo("Exclusão", "Feedback excluído com sucesso!")
                return
            else:
                messagebox.showerror("Erro", "Você só pode excluir seus próprios feedbacks!")
                return
    
    messagebox.showerror("Erro", "Feedback não encontrado!")

# Configuração da janela principal
root = tk.Tk()
root.title("Pesquisa de Satisfação")
root.geometry("400x500")
root.configure(bg="#2C3E50")  # Definir cor de fundo

# Título
titulo = tk.Label(root, text="Pesquisa de Satisfação", font=("Arial", 14, "bold"), bg="#2C3E50", fg="#ECF0F1")
titulo.pack(pady=10)

# Avaliação com estrelas
estrelas_var = tk.IntVar()

estrelas_frame = tk.Frame(root, bg="#2C3E50")  # Fundo azul escuro
estrelas_frame.pack()
tk.Label(estrelas_frame, text="Avaliação (1-5):", bg="#2C3E50", fg="#ECF0F1").pack(side=tk.LEFT)

for i in range(1, 6):
    tk.Radiobutton(estrelas_frame, text=str(i), variable=estrelas_var, value=i, bg="#2C3E50", fg="#ECF0F1", selectcolor="#34495E").pack(side=tk.LEFT)

# Comentários adicionais
tk.Label(root, text="Comentários Adicionais:", bg="#2C3E50", fg="#ECF0F1").pack(pady=5)
comentario_entry = tk.Text(root, width=50, height=5, bg="#34495E", fg="#ECF0F1", insertbackground="white")
comentario_entry.pack()

# Botões
btn_bg = "#16A085"  # Cor dos botões (verde mais suave)
btn_fg = "#ECF0F1"  # Cor do texto dos botões

enviar_button = tk.Button(root, text="Enviar", command=enviar_resposta, bg=btn_bg, fg=btn_fg)
enviar_button.pack(pady=10)

visualizar_button = tk.Button(root, text="Visualizar Respostas", command=visualizar_respostas, bg=btn_bg, fg=btn_fg)
visualizar_button.pack(pady=5)

excluir_button = tk.Button(root, text="Excluir Feedback", command=excluir_feedback, bg=btn_bg, fg=btn_fg)
excluir_button.pack(pady=5)

root.mainloop()
