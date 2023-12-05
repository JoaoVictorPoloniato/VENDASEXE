import tkinter as tk
from tkinter import messagebox
from conector import conectar_banco

def adicionar_produto():
    id_produto = entry_id.get()
    nome = entry_nome.get()
    preco = entry_preco.get()
    quantidade_em_estoque = entry_quantidade_em_estoque.get()

    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "INSERT INTO produto (idProduto, nome, preco, quantidadeEmEstoque) VALUES (%s, %s, %s, %s)"
    valores = (id_produto, nome, preco, quantidade_em_estoque)

    try:
        cursor.execute(consulta, valores)
        conexao.commit()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao adicionar produto: {err}")
    finally:
        cursor.close()
        conexao.close()

def mostrar_produtos():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        consulta_produtos = "SELECT idProduto, nome, preco, quantidadeEmEstoque FROM produto"
        cursor.execute(consulta_produtos)
        produtos = cursor.fetchall()

        # Criar uma nova janela para mostrar os produtos
        janela_produtos = tk.Toplevel(root)
        janela_produtos.title("Lista de Produtos")

        # Adicionar widgets para mostrar os produtos
        for i, produto in enumerate(produtos):
            label_produto = tk.Label(janela_produtos, text=f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Estoque: {produto[3]}")
            label_produto.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao consultar produtos: {err}")
    finally:
        cursor.close()
        conexao.close()

root = tk.Tk()
root.title("Cadastro de Produto")

label_id = tk.Label(root, text="ID do Produto:")
entry_id = tk.Entry(root)

label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)

label_preco = tk.Label(root, text="Preço:")
entry_preco = tk.Entry(root)

label_quantidade_em_estoque = tk.Label(root, text="Quantidade em Estoque:")
entry_quantidade_em_estoque = tk.Entry(root)

botao_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
botao_mostrar_produtos = tk.Button(root, text="Mostrar Produtos", command=mostrar_produtos)

label_id.grid(row=0, column=0, padx=10, pady=5)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome.grid(row=1, column=0, padx=10, pady=5)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_preco.grid(row=2, column=0, padx=10, pady=5)
entry_preco.grid(row=2, column=1, padx=10, pady=5)

label_quantidade_em_estoque.grid(row=3, column=0, padx=10, pady=5)
entry_quantidade_em_estoque.grid(row=3, column=1, padx=10, pady=5)

botao_adicionar.grid(row=4, column=0, columnspan=2, pady=10)
botao_mostrar_produtos.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()





        