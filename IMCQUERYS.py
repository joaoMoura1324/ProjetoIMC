import customtkinter as ctk
import sqlite3

# Variável global para controlar o idioma
current_language = "pt"

# Função para centralizar a janela
def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = int(largura_tela / 2 - largura / 2)
    pos_y = int(altura_tela / 2 - altura / 2)
    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

# Função para alternar o idioma
def alternar_idioma():
    global current_language
    resultado_label.configure(text="")
    if current_language == "pt":
        current_language = "en"
        titulo_label.configure(text="IMC Calculator")
        nome_label.configure(text="User Name:")
        pesquisar_button.configure(text="Calculate IMC")
        mostrar_usuarios_button.configure(text="Show Users")
        criar_utilizador_button.configure(text="Create User")
        botao_idioma.configure(text="Portuguese")
    else:
        current_language = "pt"
        titulo_label.configure(text="Calculadora de IMC")
        nome_label.configure(text="Nome do Utilizador:")
        pesquisar_button.configure(text="Calcular IMC")
        mostrar_usuarios_button.configure(text="Mostrar Utilizadores")
        criar_utilizador_button.configure(text="Criar Utilizador")
        botao_idioma.configure(text="English")

# Função para calcular o IMC
def calcular_imc():
    nome = nome_entry.get()
    conexao = sqlite3.connect('IMC.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT Peso, Altura FROM User WHERE Nome = ?", (nome,))
    dados = cursor.fetchone()

    if dados:
        peso, altura = dados
        imc = peso / (altura ** 2)
        resultado_label.configure(text=f"{nome} has an IMC of {imc:.2f}" if current_language == "en" else f"{nome} tem um IMC de {imc:.2f}")
    else:
        resultado_label.configure(text="User not found." if current_language == "en" else "Utilizador não encontrado.")
    conexao.close()

# Função para mostrar a lista de utilizadores
def mostrar_usuarios():
    janela_usuarios = ctk.CTk()
    janela_usuarios.title("User List")
    janela_usuarios.geometry("800x600")
    centralizar_janela(janela_usuarios, 800, 600)
    janela_usuarios.configure(fg_color="#131E3D")

    titulo_label_usuarios = ctk.CTkLabel(janela_usuarios, text="User List" if current_language == "en" else "Lista de Utilizadores", font=("Arial", 32), text_color="#ADD8E6")
    titulo_label_usuarios.pack(pady=40)

    conexao = sqlite3.connect('IMC.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT Nome FROM User")
    usuarios = cursor.fetchall()

    usuarios_label = ctk.CTkLabel(janela_usuarios, text="", font=("Arial", 20), text_color="#D3D3D3")
    usuarios_label.pack(pady=10)

    usuarios_texto = "\n".join([usuario[0] for usuario in usuarios])
    usuarios_label.configure(text=usuarios_texto)

    # Botão para eliminar utilizador
    eliminar_button = ctk.CTkButton(janela_usuarios, text="Eliminar Utilizador" if current_language == "pt" else "Delete User", command=eliminar_utilizador, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
    eliminar_button.pack(pady=20)

    voltar_button = ctk.CTkButton(janela_usuarios, text="Back to Calculator" if current_language == "en" else "Voltar para Calculadora", command=janela_usuarios.destroy, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
    voltar_button.pack(pady=20)

    conexao.close()

    janela_usuarios.mainloop()

# Função para eliminar utilizador
def eliminar_utilizador():
    janela_eliminar = ctk.CTk()
    janela_eliminar.title("Delete User" if current_language == "en" else "Eliminar Utilizador")
    janela_eliminar.geometry("800x600")
    centralizar_janela(janela_eliminar, 800, 600)
    janela_eliminar.configure(fg_color="#131E3D")

    titulo_label_eliminar = ctk.CTkLabel(janela_eliminar, text="Delete User" if current_language == "en" else "Eliminar Utilizador", font=("Arial", 32), text_color="#ADD8E6")
    titulo_label_eliminar.pack(pady=40)

    nome_label_eliminar = ctk.CTkLabel(janela_eliminar, text="Name:" if current_language == "en" else "Nome:", font=("Arial", 20), text_color="#D3D3D3")
    nome_label_eliminar.pack(pady=10)
    nome_entry_eliminar = ctk.CTkEntry(janela_eliminar, width=300, font=("Arial", 18))
    nome_entry_eliminar.pack(pady=10)

    def confirmar_eliminacao():
        nome = nome_entry_eliminar.get()
        conexao = sqlite3.connect('IMC.db')
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM User WHERE Nome = ?", (nome,))
        conexao.commit()
        conexao.close()
        janela_eliminar.destroy()

    eliminar_button = ctk.CTkButton(janela_eliminar, text="Delete" if current_language == "en" else "Eliminar", command=confirmar_eliminacao, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
    eliminar_button.pack(pady=20)

    cancelar_button = ctk.CTkButton(janela_eliminar, text="Cancel", command=janela_eliminar.destroy, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
    cancelar_button.pack(pady=20)

    janela_eliminar.mainloop()

# Função para criar utilizador
def criar_utilizador():
    janela_criar = ctk.CTk()
    janela_criar.title("Create User" if current_language == "en" else "Criar Utilizador")
    janela_criar.geometry("800x600")
    centralizar_janela(janela_criar, 800, 600)
    janela_criar.configure(fg_color="#131E3D")

    titulo_label_criar = ctk.CTkLabel(janela_criar, text="Create User" if current_language == "en" else "Criar Utilizador", font=("Arial", 32), text_color="#ADD8E6")
    titulo_label_criar.pack(pady=40)

    nome_label_criar = ctk.CTkLabel(janela_criar, text="Name:" if current_language == "en" else "Nome:", font=("Arial", 20), text_color="#D3D3D3")
    nome_label_criar.pack(pady=10)
    nome_entry_criar = ctk.CTkEntry(janela_criar, width=300, font=("Arial", 18))
    nome_entry_criar.pack(pady=10)

    idade_label = ctk.CTkLabel(janela_criar, text="Age:" if current_language == "en" else "Idade:", font=("Arial", 20), text_color="#D3D3D3")
    idade_label.pack(pady=10)
    idade_entry = ctk.CTkEntry(janela_criar, width=300, font=("Arial", 18))
    idade_entry.pack(pady=10)

    peso_label = ctk.CTkLabel(janela_criar, text="Weight (kg):" if current_language == "en" else "Peso (kg):", font=("Arial", 20), text_color="#D3D3D3")
    peso_label.pack(pady=10)
    peso_entry = ctk.CTkEntry(janela_criar, width=300, font=("Arial", 18))
    peso_entry.pack(pady=10)

    altura_label = ctk.CTkLabel(janela_criar, text="Height (m):" if current_language == "en" else "Altura (m):", font=("Arial", 20), text_color="#D3D3D3")
    altura_label.pack(pady=10)
    altura_entry = ctk.CTkEntry(janela_criar, width=300, font=("Arial", 18))
    altura_entry.pack(pady=10)

    def salvar_utilizador():
        nome = nome_entry_criar.get()
        idade = idade_entry.get()
        peso = peso_entry.get()
        altura = altura_entry.get()

        conexao = sqlite3.connect('IMC.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO User (Nome, Idade, Peso, Altura) VALUES (?, ?, ?, ?)", (nome, idade, peso, altura))
        conexao.commit()
        conexao.close()
        janela_criar.destroy()

    salvar_button = ctk.CTkButton(janela_criar, text="Save" if current_language == "en" else "Guardar", command=salvar_utilizador, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
    salvar_button.pack(pady=20)

    cancelar_button = ctk.CTkButton(janela_criar, text="Cancel", command=janela_criar.destroy, font=("Arial", 18), fg_color="#D3D3D3", text_color="#131E3D", hover_color="#131E3D")
    cancelar_button.pack(pady=20)

    janela_criar.mainloop()

# Janela principal
janela_principal = ctk.CTk()
janela_principal.title("IMC Calculator")
janela_principal.geometry("800x600")
centralizar_janela(janela_principal, 800, 600)
janela_principal.configure(fg_color="#131E3D")

titulo_label = ctk.CTkLabel(janela_principal, text="IMC Calculator", font=("Arial", 32), text_color="#ADD8E6")
titulo_label.pack(pady=40)

nome_label = ctk.CTkLabel(janela_principal, text="Nome do Utilizador:", font=("Arial", 20), text_color="#D3D3D3")
nome_label.pack(pady=10)

nome_entry = ctk.CTkEntry(janela_principal, width=300, font=("Arial", 18))
nome_entry.pack(pady=10)

# Botão para calcular IMC
pesquisar_button = ctk.CTkButton(janela_principal, text="Calcular IMC", command=calcular_imc, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
pesquisar_button.pack(pady=20)

# Botão para mostrar utilizadores
mostrar_usuarios_button = ctk.CTkButton(janela_principal, text="Mostrar Utilizadores", command=mostrar_usuarios, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
mostrar_usuarios_button.pack(pady=20)

# Botão para criar utilizador
criar_utilizador_button = ctk.CTkButton(janela_principal, text="Criar Utilizador", command=criar_utilizador, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
criar_utilizador_button.pack(pady=20)

# Botão de alternância de idioma
botao_idioma = ctk.CTkButton(janela_principal, text="English", command=alternar_idioma, font=("Arial", 18), fg_color="#006494", text_color="#D3D3D3", hover_color="#006494")
botao_idioma.pack(pady=20)

# Rótulo para exibir o resultado
resultado_label = ctk.CTkLabel(janela_principal, text="", font=("Arial", 20), text_color="#D3D3D3")
resultado_label.pack(pady=20)

janela_principal.mainloop()
