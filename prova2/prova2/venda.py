import tkinter as tk
from tkinter import messagebox
from conector import conectar_banco

def realizar_venda():
    # Obter valores dos campos de entrada (ID do Cliente, ID do Produto, Quantidade)
    id_cliente = entry_id_cliente.get()
    id_produto = entry_id_produto.get()
    quantidade = int(entry_quantidade.get())

    # Conectar ao banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        # Consultar o estoque atual do produto
        consulta_estoque = "SELECT quantidadeEmEstoque FROM produto WHERE idProduto = %s"
        cursor.execute(consulta_estoque, (id_produto,))
        resultado_estoque = cursor.fetchone()

        if resultado_estoque:
            estoque_atual = resultado_estoque[0]

            # Verificar se há estoque suficiente
            if quantidade <= estoque_atual:
                # Registrar a venda
                consulta_venda = "INSERT INTO venda (data, total, idCliente) VALUES (CURDATE(), 0, %s)"
                valores_venda = (id_cliente,)
                cursor.execute(consulta_venda, valores_venda)

                # Obter o ID da venda
                id_venda = cursor.lastrowid

                # Atualizar o detalhe da venda
                consulta_detalhe_venda = "INSERT INTO detalhe_venda (idVenda, idProduto, quantidade) VALUES (%s, %s, %s)"
                valores_detalhe_venda = (id_venda, id_produto, quantidade)
                cursor.execute(consulta_detalhe_venda, valores_detalhe_venda)

                # Atualizar o estoque
                novo_estoque = estoque_atual - quantidade
                consulta_atualizar_estoque = "UPDATE produto SET quantidadeEmEstoque = %s WHERE idProduto = %s"
                valores_atualizar_estoque = (novo_estoque, id_produto)
                cursor.execute(consulta_atualizar_estoque, valores_atualizar_estoque)

                #mudanças
                conexao.commit()

                messagebox.showinfo("Sucesso", "Venda realizada com sucesso!")
            else:
                messagebox.showwarning("Estoque Insuficiente", "Estoque insuficiente para realizar a venda.")
        else:
            messagebox.showerror("Erro", "Produto não encontrado.")
    except Exception as err:
        # Lidar erros
        messagebox.showerror("Erro", f"Erro ao realizar venda: {err}")
    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

# Interface Gráfica
root = tk.Tk()
root.title("Realizar Venda")

def mostrar_vendas():
    # Conectar ao banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        # Consultar vendas
        consulta_vendas = """
        SELECT v.idvenda, v.data, c.nome as cliente, p.nome as produto, dv.quantidade, p.preco, dv.quantidade * p.preco as total
        FROM venda v
        INNER JOIN detalhe_venda dv ON v.idvenda = dv.idVenda
        INNER JOIN produto p ON dv.idProduto = p.idProduto
        INNER JOIN cliente c ON v.idCliente = c.idCliente
        """
        cursor.execute(consulta_vendas)
        resultado_vendas = cursor.fetchall()

        # Exibir resultado em uma nova janela
        janela_vendas = tk.Toplevel()
        janela_vendas.title("Lista de Vendas")

        
        for i, venda in enumerate(resultado_vendas):
            label_venda = tk.Label(janela_vendas, text=f"ID Venda: {venda[0]}, Data: {venda[1]}, Cliente: {venda[2]}, Produto: {venda[3]}, Quantidade: {venda[4]}, Total: {venda[6]}")
            label_venda.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

    except Exception as err:
        messagebox.showerror("Erro", f"Erro ao consultar vendas: {err}")
    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()



# Adicionar um botão para chamar a função mostrar_vendas
botao_mostrar_vendas = tk.Button(root, text="Mostrar Vendas", command=mostrar_vendas)
botao_mostrar_vendas.grid(row=6, column=0, columnspan=2, pady=10)


label_id_cliente = tk.Label(root, text="ID do Cliente:")
entry_id_cliente = tk.Entry(root)

label_id_produto = tk.Label(root, text="ID do Produto:")
entry_id_produto = tk.Entry(root)

label_quantidade = tk.Label(root, text="Quantidade:")
entry_quantidade = tk.Entry(root)

botao_realizar_venda = tk.Button(root, text="Realizar Venda", command=realizar_venda)

label_id_cliente.grid(row=0, column=0, padx=10, pady=5)
entry_id_cliente.grid(row=0, column=1, padx=10, pady=5)

label_id_produto.grid(row=1, column=0, padx=10, pady=5)
entry_id_produto.grid(row=1, column=1, padx=10, pady=5)

label_quantidade.grid(row=2, column=0, padx=10, pady=5)
entry_quantidade.grid(row=2, column=1, padx=10, pady=5)

botao_realizar_venda.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
