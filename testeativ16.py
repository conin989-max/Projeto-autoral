import customtkinter as ctk
import os

ARQUIVO = "banco_de_dados.txt"

# --- 1. REGRA DE NEGÓCIO (Lógica de Dados) ---

def salvar_no_arquivo(nome, prioridade):
    with open(ARQUIVO, 'a', encoding='utf-8') as f:
        f.write(f"{nome} - Prioridade: {prioridade}\n")


def ler_arquivo():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        return f.readlines()


def excluir_do_arquivo(nome_excluir):
    linhas = ler_arquivo()

    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        for linha in linhas:
            # Se o nome digitado NÃO estiver na linha, ela é salva novamente
            if nome_excluir.lower() not in linha.lower():
                f.write(linha)


# --- 2. INTERFACE GRÁFICA (Visual) ---

ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.geometry("450x650")
janela.title("Lanchonete Ennius Muniz")

titulo = ctk.CTkLabel(
    janela,
    text="Sistema de Cadastro",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)

entrada_nome = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o nome...",
    width=250
)
entrada_nome.pack(pady=5)

slider_prioridade = ctk.CTkSlider(
    janela,
    from_=0,
    to=100
)
slider_prioridade.pack(pady=10)


# --- 3. A PONTE (Ações dos Botões) ---

def atualizar_tela():
    caixa_texto.delete("0.0", "end")
    linhas = ler_arquivo()

    for linha in linhas:
        caixa_texto.insert("end", linha)


def acao_salvar():
    nome = entrada_nome.get()

    if nome != "":
        salvar_no_arquivo(nome, int(slider_prioridade.get()))
        entrada_nome.delete(0, "end")
        atualizar_tela()


def acao_excluir():
    nome = entrada_excluir.get()

    if nome != "":
        excluir_do_arquivo(nome)
        entrada_excluir.delete(0, "end")
        atualizar_tela()


btn_salvar = ctk.CTkButton(
    janela,
    text="Salvar",
    command=acao_salvar,
    fg_color="green"
)
btn_salvar.pack(pady=5)


# --- 4. EXIBIÇÃO E EXCLUSÃO ---

caixa_texto = ctk.CTkTextbox(
    janela,
    width=250,
    height=200
)
caixa_texto.pack(pady=15)

entrada_excluir = ctk.CTkEntry(
    janela,
    placeholder_text="Nome para excluir...",
    width=250
)
entrada_excluir.pack(pady=5)

btn_excluir = ctk.CTkButton(
    janela,
    text="Excluir Registro",
    command=acao_excluir,
    fg_color="red"
)
btn_excluir.pack(pady=5)


# Carrega os dados na tela assim que o aplicativo abre
atualizar_tela()

janela.mainloop()