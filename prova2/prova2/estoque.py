import tkinter as tk
from tkinter import messagebox
from conector import conectar_banco

# Criar a janela principal
root = tk.Tk()
root.title("Sua Aplicação")

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


# Adicionar um botão para chamar a função consultar_estoque
botao_consultar_estoque = tk.Button(root, text="Consultar Estoque", command=consultar_estoque)
botao_consultar_estoque.grid(row=4, column=0, columnspan=2, pady=10)

def atualizar_estoque():
    # Função para lidar com a atualização de estoque
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

                
                conexao.commit()

                messagebox.showinfo("Sucesso", "Estoque atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")

        except Exception as err:
            # Lidar com erros
            messagebox.showerror("Erro", f"Erro ao atualizar estoque: {err}")

        finally:
            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

    # Interface Gráfica
    janela_atualizar_estoque = tk.Toplevel(root)
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


# Adicionar um botão para chamar a função atualizar_estoque
botao_atualizar_estoque = tk.Button(root, text="Atualizar Estoque", command=atualizar_estoque)
botao_atualizar_estoque.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
