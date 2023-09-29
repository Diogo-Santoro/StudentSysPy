
import re
import sqlite3
import tkinter as tk
import tkinter.ttk as tkk
from tkinter import messagebox


class ConectarDB:
    def __init__(self):
        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS TBL_DADOS (
                nome TEXT,
                rua TEXT,
                bairro TEXT,
                cidade TEXT,
                estado TEXT,
                cep TEXT,
                celular TEXT,
                email TEXT,
                cpf TEXT,
                rg TEXT)''')
        except Exception as e:
            print('[x] Falha ao criar tabela: %s [x]' % e)
        else:
            print('\n[!] Tabela criada com sucesso [!]\n')

    def inserir_registro(self, nome, rua, bairro, cidade, estado, cep, celular, email, cpf, rg):
        try:
            self.cur.execute(
                '''INSERT INTO TBL_DADOS VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, rua, bairro, cidade, estado, cep, celular, email, cpf, rg,))
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print('[x] Revertendo operação (rollback) %s [x]\n' % e)
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def consultar_registros(self):
        return self.cur.execute('SELECT rowid, * FROM TBL_DADOS').fetchall()

    def consultar_ultimo_rowid(self):
        return self.cur.execute('SELECT MAX(rowid) FROM TBL_DADOS').fetchone()

    def remover_registro(self, rowid):
        try:
            self.cur.execute("DELETE FROM TBL_DADOS WHERE rowid=?", (rowid,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print('[x] Revertendo operação (rollback) %s [x]\n' % e)
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')


class Janela(tk.Frame):


    def __init__(self, master=None):

        super().__init__(master)

        largura = round(self.winfo_screenwidth() / 2)
        altura = round(self.winfo_screenheight() / 2)
        tamanho = ('%sx%s' % (largura, altura))


        master.title('Cadastro')

        master.geometry(tamanho)


        self.banco = ConectarDB()


        self.pack()

        self.criar_widgets()

    def criar_widgets(self):

        frame1 = tk.Frame(self)
        frame1.pack(side=tk.TOP, fill=tk.BOTH)

        frame2 = tk.Frame(self)
        frame2.pack(fill=tk.BOTH, expand=True)

        frame3 = tk.Frame(self)
        frame3.pack(side=tk.BOTTOM, padx=5)

        label_nome = tk.Label(frame1, text='Nome')
        label_nome.grid(row=0, column=0)

        label_rua = tk.Label(frame1, text='Rua')
        label_rua.grid(row=0, column=1)

        label_bairro = tk.Label(frame1, text='Bairro')
        label_bairro.grid(row=0, column=2)

        label_cidade = tk.Label(frame1, text='Cidade')
        label_cidade.grid(row=0, column=3)

        label_estado = tk.Label(frame1, text='Estado')
        label_estado.grid(row=0, column=4)
 
        label_cep = tk.Label(frame1, text='CEP')
        label_cep.grid(row=0, column=5)

        label_celular = tk.Label(frame1, text='Celular')
        label_celular.grid(row=0, column=6)

        label_email = tk.Label(frame1, text='E-mail')
        label_email.grid(row=0, column=7)

        label_cpf = tk.Label(frame1, text='CPF')
        label_cpf.grid(row=0, column=8)

        label_rg = tk.Label(frame1, text='RG')
        label_rg.grid(row=0, column=9)



        self.entry_nome = tk.Entry(frame1)
        self.entry_nome.grid(row=1, column=0)

        self.entry_rua = tk.Entry(frame1)
        self.entry_rua.grid(row=1, column=1, padx=10)

        self.entry_bairro = tk.Entry(frame1)
        self.entry_bairro.grid(row=1, column=2)

        self.entry_cidade = tk.Entry(frame1)
        self.entry_cidade.grid(row=1, column=3, padx=10)

        self.entry_estado = tk.Entry(frame1)
        self.entry_estado.grid(row=1, column=4, padx=10)

        self.entry_cep = tk.Entry(frame1)
        self.entry_cep.grid(row=1, column=5, padx=10)

        self.entry_celular = tk.Entry(frame1)
        self.entry_celular.grid(row=1, column=6, padx=10)

        self.entry_email = tk.Entry(frame1)
        self.entry_email.grid(row=1, column=7, padx=10)

        self.entry_cpf = tk.Entry(frame1)
        self.entry_cpf.grid(row=1, column=8, padx=10)

        self.entry_rg = tk.Entry(frame1)
        self.entry_rg.grid(row=1, column=9, padx=10)




        button_adicionar = tk.Button(frame1, text='Adicionar', bg='blue', fg='white')

        button_adicionar['command'] = self.adicionar_registro
        button_adicionar.grid(row=0, column=10, rowspan=2, padx=10)


        self.treeview = tkk.Treeview(frame2, columns=('Nome', 'Rua', 'Bairro', 'Cidade', 'Estado', 'CEP', 'Celular', 'E-mail', 'CPF', 'RG'))
        self.treeview.heading('#0', text='ROWID')
        self.treeview.heading('#1', text='Nome')
        self.treeview.heading('#2', text='Rua')
        self.treeview.heading('#3', text='Bairro')
        self.treeview.heading('#4', text='Cidade')
        self.treeview.heading('#5', text='Estado')
        self.treeview.heading('#6', text='CEP')
        self.treeview.heading('#7', text='Celular')
        self.treeview.heading('#8', text='E-mail')
        self.treeview.heading('#9', text='CPF')
        self.treeview.heading('#10', text='RG')

        for row in self.banco.consultar_registros():
            self.treeview.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

        self.treeview.pack(fill=tk.BOTH, expand=True)


        button_excluir = tk.Button(frame3, text='Excluir', bg='red', fg='white')

        button_excluir['command'] = self.excluir_registro
        button_excluir.pack(pady=10)

    def adicionar_registro(self):

        nome = self.entry_nome.get()
        rua = self.entry_rua.get()
        bairro = self.entry_bairro.get()
        cidade = self.entry_cidade.get()
        estado = self.entry_estado.get()
        cep = self.entry_cep.get()
        celular = self.entry_celular.get()
        email = self.entry_email.get()
        cpf = self.entry_cpf.get()
        rg = self.entry_rg.get()

        self.banco.inserir_registro(nome=nome, rua=rua, bairro=bairro, cidade=cidade, estado=estado, cep=cep, 
                                        celular=celular, email=email, cpf=cpf, rg=rg)
        rowid = self.banco.consultar_ultimo_rowid()[0]
        self.treeview.insert('', 'end', text=rowid, values=(nome, rua, bairro, cidade, estado, cep, celular, email, cpf, rg))

    def excluir_registro(self):

        if not self.treeview.focus():
            messagebox.showerror('Erro', 'Nenhum item selecionado')
        else:

            item_selecionado = self.treeview.focus()


            rowid = self.treeview.item(item_selecionado)

            self.banco.remover_registro(rowid['text'])

            self.treeview.delete(item_selecionado)


root = tk.Tk()
app = Janela(master=root)
app.mainloop()