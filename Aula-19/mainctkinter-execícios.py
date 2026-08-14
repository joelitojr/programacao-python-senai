# # CRIE UM BANCO DE DADOS PARA UMA AGENCIA DE MARKETING 
# # PRECISA  CADASTRAR OS LEADS DA AGENCIA:

# # Banco de Dados 4 - Marketing com Tkinter ( Aula anterior )
# # Melhorar esse projeto com CustomTkinter

import sqlite3
import tkinter as tk
from tkinter import messagebox

con =  sqlite3.connect('agmarketing.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadleads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL,
        endereco TEXT NOT NULL,
        trabalho TEXT,
        graduacao TEXT
    )
''')
con.commit()

# crud
def criar_cadlead():
    nome  = nome_input.get()
    idade = idade_input.get()
    email = email_input.get()
    ender = ender_input.get()
    trab  = trab_input.get()
    grad  = grad_input.get()
    cursor.execute('INSERT INTO cadleads (nome, idade, email, endereco, trabalho, graduacao) values(? ,? ,? ,? ,? ,?)', (nome, idade, email, ender, trab, grad))
    con.commit()
    messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO')

def listar_cadleads():
    cursor.execute('SELECT * FROM cadleads')
    return cursor.fetchall()

def atualizar_mail(id_lead, novo_email):
    cursor.execute('UPDATE cadleads SET email=? WHERE id = ?', (novo_email, id_lead))
    con.commit()

def deletar_cadlead(id_lead):
    cursor.execute('DELETE FROM cadleads WHERE id = ?', (id_lead))
    con.commit()

root  =  tk.Tk()
root.geometry('750x500')
root.configure(bg = 'lightblue')
# root.iconbitmap('i.ico')

tk.Label(root, text =  'AGÊNCIA DE MARKETING - CADASTRO DE LEADS:', font = ('system','15') , bg='lightblue' , justify='left').grid(row=1, column=0)

tk.Label(root, text =  'nome:', bg='lightblue', font = ('system','10') , justify='left').grid(row=3, column=0)
nome_input = tk.Entry(root)
nome_input.grid(row=3, column=1)  

tk.Label(root, text =  'idade:', bg='lightblue', font = ('system','10')).grid(row=5, column=0)
idade_input = tk.Entry(root)
idade_input.grid(row=5, column=1)  

tk.Label(root, text =  'e-mail:', bg='lightblue', font = ('system','10')).grid(row=7, column=0)
email_input = tk.Entry(root)
email_input.grid(row=7, column=1)  

tk.Label(root, text =  'endereço:', bg='lightblue', font = ('system','10')).grid(row=9, column=0)
ender_input = tk.Entry(root)
ender_input.grid(row=9, column=1)  

tk.Label(root, text =  'trabalho:', bg='lightblue', font = ('system','10')).grid(row=11, column=0)
trab_input = tk.Entry(root)
trab_input.grid(row=11, column=1)  

tk.Label(root, text =  'graduação:', bg='lightblue', font = ('system','10')).grid(row=13, column=0)
grad_input = tk.Entry(root)
grad_input.grid(row=13, column=1)  

btn =  tk.Button(root, text= 'Inserir', command=criar_cadlead, width=15, font = ('system','10'))
btn.grid(row=17, column=1, pady=10)

btn =  tk.Button(root, text= 'Listar', command=listar_cadleads, width=15, font = ('system','10'))
btn.grid(row=19, column=1, pady=10)

root.mainloop()