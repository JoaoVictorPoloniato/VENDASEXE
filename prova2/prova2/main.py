import tkinter as tk
from tkinter import messagebox
from conector import conectar_banco

# Função para abrir a tela de cadastro de clientes
def abrir_cadastro_cliente():
    cadastro_cliente = tk.Toplevel(root)
    cadastro_cliente.title("Cadastro de Cliente")

    # Função para adicionar cliente
    def adicionar_cliente():
        id_cliente = entry_id.get()
        nome = entry_nome.get()
        email = entry_email.get()

        conexao = conectar_banco()
        cursor = conexao.cursor()

        consulta = "INSERT INTO cliente (idCliente, nome, email) VALUES (%s, %s, %s)"
        valores = (id_cliente, nome, email)

        try:
            cursor.execute(consulta, valores)
            conexao.commit()
            messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        except Exception as err:
            messagebox.showerror("Erro", f"Erro ao adicionar cliente: {err}")
        finally:
            cursor.close()
            conexao.close()

    # Elementos da interface de cadastro de cliente
    label_id = tk.Label(cadastro_cliente, text="ID do Cliente:")
    entry_id = tk.Entry(cadastro_cliente)

    label_nome = tk.Label(cadastro_cliente, text="Nome:")
    entry_nome = tk.Entry(cadastro_cliente)

    label_email = tk.Label(cadastro_cliente, text="Email:")
    entry_email = tk.Entry(cadastro_cliente)

    botao_adicionar = tk.Button(cadastro_cliente, text="Adicionar Cliente", command=adicionar_cliente)

    label_id.grid(row=0, column=0, padx=10, pady=5)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    label_nome.grid(row=1, column=0, padx=10, pady=5)
    entry_nome.grid(row=1, column=1, padx=10, pady=5)

    label_email.grid(row=2, column=0, padx=10, pady=5)
    entry_email.grid(row=2, column=1, padx=10, pady=5)

    botao_adicionar.grid(row=3, column=0, columnspan=2, pady=10)


# Função para abrir a tela de cadastro de produtos
def abrir_cadastro_produto():
    cadastro_produto = tk.Toplevel(root)
    cadastro_produto.title("Cadastro de Produto")

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
            janela_produtos = tk.Toplevel(cadastro_produto)
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

   

    label_id = tk.Label(cadastro_produto, text="ID do Produto:")
    entry_id = tk.Entry(cadastro_produto)

    label_nome = tk.Label(cadastro_produto, text="Nome:")
    entry_nome = tk.Entry(cadastro_produto)

    label_preco = tk.Label(cadastro_produto, text="Preço:")
    entry_preco = tk.Entry(cadastro_produto)

    label_quantidade_em_estoque = tk.Label(cadastro_produto, text="Quantidade em Estoque:")
    entry_quantidade_em_estoque = tk.Entry(cadastro_produto)

    botao_adicionar = tk.Button(cadastro_produto, text="Adicionar Produto", command=adicionar_produto)
    botao_mostrar_produtos = tk.Button(cadastro_produto, text="Mostrar Produtos", command=mostrar_produtos)

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


def abrir_consulta_estoque():
    # Criar a janela principal para a consulta de estoque
    consulta_estoque = tk.Toplevel(root)
    consulta_estoque.title("Consulta de Estoque")

    # Adicionar um botão para chamar a função consultar_estoque
    botao_consultar_estoque = tk.Button(consulta_estoque, text="Consultar Estoque", command=consultar_estoque)
    botao_consultar_estoque.grid(row=4, column=0, columnspan=2, pady=10)

    # Adicionar um botão para chamar a função atualizar_estoque
    botao_atualizar_estoque = tk.Button(consulta_estoque, text="Atualizar Estoque", command=atualizar_estoque)
    botao_atualizar_estoque.grid(row=5, column=0, columnspan=2, pady=10)

def consultar_estoque():
    # Conectar ao banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        # Consultar estoque
        consulta_estoque = "SELECT idProduto, nome, quantidadeEmEstoque FROM produto"
        cursor.execute(consulta_estoque)
        resultado_estoque = cursor.fetchall()

        # Exibir resultado em uma nova janela
        janela_estoque = tk.Toplevel()
        janela_estoque.title("Consulta de Estoque")

        for produto in resultado_estoque:
            label = tk.Label(janela_estoque, text=f"ID: {produto[0]}, Produto: {produto[1]}, Quantidade: {produto[2]}")
            label.pack(pady=5)

    except Exception as err:
        messagebox.showerror("Erro", f"Erro ao consultar estoque: {err}")
    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

def atualizar_estoque():
    
    def atualizar():
        # Obter valores de entrada
        id_produto = entry_id_produto.get()
        nova_quantidade = entry_nova_quantidade.get()

        # Conectar ao banco de dados
        conexao = conectar_banco()
        cursor = conexao.cursor()

        try:
            # Verificar se o produto existe
            consulta_produto = "SELECT * FROM produto WHERE idProduto = %s"
            cursor.execute(consulta_produto, (id_produto,))
            resultado_produto = cursor.fetchone()

            if resultado_produto:
                # Atualizar o estoque
                consulta_atualizar_estoque = "UPDATE produto SET quantidadeEmEstoque = %s WHERE idProduto = %s"
                valores_atualizar_estoque = (nova_quantidade, id_produto)
                cursor.execute(consulta_atualizar_estoque, valores_atualizar_estoque)

                # mudanças
                conexao.commit()

                messagebox.showinfo("Sucesso", "Estoque atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")

        except Exception as err:
            # Lidar erros
            messagebox.showerror("Erro", f"Erro ao atualizar estoque: {err}")

        finally:
            # Fechar o cursor e a conexãos
            cursor.close()
            conexao.close()

    # Interface Gráfica para atualizar estoque
    janela_atualizar_estoque = tk.Toplevel()
    janela_atualizar_estoque.title("Atualizar Estoque")
    
    label_id_produto = tk.Label(janela_atualizar_estoque, text="ID do Produto:")
    entry_id_produto = tk.Entry(janela_atualizar_estoque)

    label_nova_quantidade = tk.Label(janela_atualizar_estoque, text="Nova Quantidade:")
    entry_nova_quantidade = tk.Entry(janela_atualizar_estoque)

    botao_atualizar = tk.Button(janela_atualizar_estoque, text="Atualizar Estoque", command=atualizar)

    label_id_produto.grid(row=0, column=0, padx=10, pady=5)
    entry_id_produto.grid(row=0, column=1, padx=10, pady=5)

    label_nova_quantidade.grid(row=1, column=0, padx=10, pady=5)
    entry_nova_quantidade.grid(row=1, column=1, padx=10, pady=5)

    botao_atualizar.grid(row=2, column=0, columnspan=2, pady=10)


# Função para abrir a tela de relatório de vendas
def abrir_relatorio_vendas():
    # Função para gerar o relatório de vendas
    def relatorio_vendas():
        # Conectar ao banco de dados
        conexao = conectar_banco()
        cursor = conexao.cursor()

        try:
            # Consultar relatório de vendas
            consulta_relatorio = """
            SELECT v.idvenda, v.data, c.nome as cliente, p.nome as produto, dv.quantidade, p.preco, dv.quantidade * p.preco as total
            FROM venda v
            INNER JOIN detalhe_venda dv ON v.idvenda = dv.idVenda
            INNER JOIN produto p ON dv.idProduto = p.idProduto
            INNER JOIN cliente c ON v.idCliente = c.idCliente
            """
            cursor.execute(consulta_relatorio)
            resultado_relatorio = cursor.fetchall()

            # Exibir resultado em uma nova janela
            janela_relatorio = tk.Toplevel(root)
            janela_relatorio.title("Relatório de Vendas")

            for venda in resultado_relatorio:
                label = tk.Label(janela_relatorio, text=f"ID Venda: {venda[0]}, Data: {venda[1]}, Cliente: {venda[2]}, Produto: {venda[3]}, Quantidade: {venda[4]}, Total: {venda[6]}")
                label.pack(pady=5)

        except Exception as err:
            messagebox.showerror("Erro", f"Erro ao gerar relatório de vendas: {err}")
        finally:
            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

    
    relatorio_vendas()




def abrir_realizar_venda():
    def realizar_venda():
        # Obter valores dos campos de entrada (ID do Cliente, ID do Produto, Quantidade)
        id_cliente = entry_id_cliente.get()
        id_produto = entry_id_produto.get()
        quantidade = int(entry_quantidade.get())

        # Verificar se o ID do Cliente não está vazio
        if not id_cliente:
            messagebox.showwarning("Campo Vazio", "Por favor, insira o ID do Cliente.")
            return

        # Conectar ao banco de dados
        conexao = conectar_banco()
        cursor = conexao.cursor()

        try:
            # Consultar o último ID de venda
            cursor.execute("SELECT MAX(idVenda) FROM venda")
            ultimo_id_venda = cursor.fetchone()[0]

            # Definir o ID da nova venda
            novo_id_venda = ultimo_id_venda + 1 if ultimo_id_venda is not None else 1

            # Consultar o estoque atual do produto
            consulta_estoque = "SELECT quantidadeEmEstoque FROM produto WHERE idProduto = %s"
            cursor.execute(consulta_estoque, (id_produto,))
            resultado_estoque = cursor.fetchone()

            if resultado_estoque:
                estoque_atual = resultado_estoque[0]

                # Verificar se há estoque suficiente
                if quantidade <= estoque_atual:
                    # Registrar a venda
                    consulta_venda = "INSERT INTO venda (idVenda, data, total, idCliente) VALUES (%s, CURDATE(), 0, %s)"
                    valores_venda = (novo_id_venda, id_cliente)
                    cursor.execute(consulta_venda, valores_venda)

                    # Atualizar o detalhe da venda
                    consulta_detalhe_venda = "INSERT INTO detalhe_venda (idVenda, idProduto, quantidade) VALUES (%s, %s, %s)"
                    valores_detalhe_venda = (novo_id_venda, id_produto, quantidade)
                    cursor.execute(consulta_detalhe_venda, valores_detalhe_venda)

                    # Atualizar o estoque
                    novo_estoque = estoque_atual - quantidade
                    consulta_atualizar_estoque = "UPDATE produto SET quantidadeEmEstoque = %s WHERE idProduto = %s"
                    valores_atualizar_estoque = (novo_estoque, id_produto)
                    cursor.execute(consulta_atualizar_estoque, valores_atualizar_estoque)

                    # mudanças
                    conexao.commit()

                    messagebox.showinfo("Sucesso", "Venda realizada com sucesso!")
                else:
                    messagebox.showwarning("Estoque Insuficiente", "Estoque insuficiente para realizar a venda.")
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")
        except Exception as err:
            # Lidar com erros
            messagebox.showerror("Erro", f"Erro ao realizar venda: {err}")
        finally:
            # Fechar o cursor e a conexão, independentemente do resultado
            cursor.close()
            conexao.close()

    # Restante do código...


    janela_realizar_venda = tk.Toplevel(root)
    janela_realizar_venda.title("Realizar Venda")

    label_id_cliente = tk.Label(janela_realizar_venda, text="ID do Cliente:")
    entry_id_cliente = tk.Entry(janela_realizar_venda)

    label_id_produto = tk.Label(janela_realizar_venda, text="ID do Produto:")
    entry_id_produto = tk.Entry(janela_realizar_venda)

    label_quantidade = tk.Label(janela_realizar_venda, text="Quantidade:")
    entry_quantidade = tk.Entry(janela_realizar_venda)

    botao_realizar_venda = tk.Button(janela_realizar_venda, text="Realizar Venda", command=realizar_venda)

    label_id_cliente.grid(row=0, column=0, padx=10, pady=5)
    entry_id_cliente.grid(row=0, column=1, padx=10, pady=5)

    label_id_produto.grid(row=1, column=0, padx=10, pady=5)
    entry_id_produto.grid(row=1, column=1, padx=10, pady=5)

    label_quantidade.grid(row=2, column=0, padx=10, pady=5)
    entry_quantidade.grid(row=2, column=1, padx=10, pady=5)

    botao_realizar_venda.grid(row=3, column=0, columnspan=2, pady=10)

# Interface Gráfica Principal
root = tk.Tk()
root.title("Sua Aplicação")

# Botões para acessar diferentes funcionalidades
btn_cadastro_cliente = tk.Button(root, text="Cadastro de Cliente", command=abrir_cadastro_cliente)
btn_cadastro_cliente.grid(row=0, column=0, padx=20, pady=10)

btn_cadastro_produto = tk.Button(root, text="Cadastro de Produto", command=abrir_cadastro_produto)
btn_cadastro_produto.grid(row=1, column=0, padx=20, pady=10)

btn_consulta_estoque = tk.Button(root, text="Consulta de Estoque", command=abrir_consulta_estoque)
btn_consulta_estoque.grid(row=2, column=0, padx=20, pady=10)

btn_relatorio_vendas = tk.Button(root, text="Relatório de Vendas", command=abrir_relatorio_vendas)
btn_relatorio_vendas.grid(row=3, column=0, padx=20, pady=10)

btn_realizar_venda = tk.Button(root, text="Realizar Venda", command=abrir_realizar_venda)
btn_realizar_venda.grid(row=4, column=0, padx=20, pady=10)

root.mainloop()
