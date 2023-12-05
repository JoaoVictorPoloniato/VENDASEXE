import tkinter as tk
from tkinter import messagebox
from conector import conectar_banco

# Criar a janela principal
root = tk.Tk()
root.title("Sua Aplicação")


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
        janela_relatorio = tk.Toplevel()
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


# Adicionar um botão para chamar a função relatorio_vendas
botao_relatorio_vendas = tk.Button(root, text="Relatório de Vendas", command=relatorio_vendas)
botao_relatorio_vendas.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
