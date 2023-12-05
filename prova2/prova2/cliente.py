import tkinter as tk
from tkinter import messagebox
from conector import conectar_banco

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
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao adicionar cliente: {err}")
    finally:
        cursor.close()
        conexao.close()
        
        
root = tk.Tk()
root.title("Cadastro de Cliente")


label_id = tk.Label(root, text="ID do Cliente:")
entry_id = tk.Entry(root)

label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)

label_email = tk.Label(root, text="Email:")
entry_email = tk.Entry(root)

botao_adicionar = tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente)

label_id.grid(row=0, column=0, padx=10, pady=5)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome.grid(row=1, column=0, padx=10, pady=5)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email.grid(row=2, column=1, padx=10, pady=5)

botao_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

