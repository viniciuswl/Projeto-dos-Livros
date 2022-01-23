import database as db
from tkinter import * 
from tkinter import ttk
import tkinter.messagebox as msb
import sqlite3
root = Tk()
root.title('Livros')
root.geometry('800x430')
root.resizable(False,False)
root.config(bg='#1f2333')
root.focus()
titulo = StringVar()
tema = StringVar()
portador = StringVar()
retirada = StringVar()
devolucao = StringVar()
buscar = StringVar()

def bookInsert():
    newWindow = Toplevel(root)
    newWindow.focus()
    newWindow.config(bg='#07C39E')
    newWindow.title("Inserir novo livro")
    newWindow.geometry("365x165")
    newWindow.resizable(False,False)
    titulo.set("")
    tema.set("")
    portador.set("")
    retirada.set("")
    devolucao.set("")
    lbl1 = Label(newWindow,text="Nome do Livro: ")
    lbl2 = Label(newWindow,text="Tema do Livro: ")
    lbl3 = Label(newWindow,text="Portador do Livro: ")
    lbl4 = Label(newWindow,text="Data de retirada: ")
    lbl5 = Label(newWindow,text="Data de Devolução: ")
    lbl1.config(font=("Helvetica", 12),bg="#07C39E")
    lbl2.config(font=("Helvetica", 12),bg="#07C39E")
    lbl3.config(font=("Helvetica", 12),bg="#07C39E")
    lbl4.config(font=("Helvetica", 12),bg="#07C39E")
    lbl5.config(font=("Helvetica", 12),bg="#07C39E")
    lbl1.grid(row=0, column=0)
    lbl2.grid(row=1, column=0)
    lbl3.grid(row=2, column=0)
    lbl4.grid(row=3, column=0)
    lbl5.grid(row=4, column=0)
    e1 = Entry(newWindow, textvariable=titulo)
    e1.focus_set()
    e2 = Entry(newWindow, textvariable=tema)
    e3 = Entry(newWindow, textvariable=portador)
    e4 = Entry(newWindow, textvariable=retirada)
    e5 = Entry(newWindow, textvariable=devolucao)
    def inserir():
        tv.delete(*tv.get_children())
        db.createData(titulo.get(),tema.get(), portador.get(), retirada.get(), devolucao.get())
        showData()
        titulo.set("")
        tema.set("")
        portador.set("")
        retirada.set("")
        devolucao.set("")
    e1.grid(row=0,column=2)
    e2.grid(row=1,column=2)
    e3.grid(row=2,column=2)
    e4.grid(row=3,column=2)
    e5.grid(row=4,column=2)
    e1.bind("<Return>", lambda ent1:e2.focus_set())
    e2.bind("<Return>", lambda ent2:e3.focus_set())
    e3.bind("<Return>", lambda ent3:e4.focus_set())
    e4.bind("<Return>", lambda ent4:e5.focus_set())
    saveButton = Button(newWindow, text="Salvar", padx=10, command = inserir)
    saveButton.grid(row=6, column=1, sticky=N, padx=15, pady=10)
    def novoBook(event):
        inserir()
        e1.focus_set()
    e5.bind("<Return>", novoBook)

def bookDelete():
    if not tv.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja deletar esses dados?")
        if resultado == 'yes':
            selected = tv.focus()
            newId = tv.item(selected, 'values')
            tv.delete(selected)
            db.deleteData(newId[0])

def bookDeleteEvent(event):
    bookDelete()

def bookUpdate(event):
    selected = tv.focus()
    conteudo = tv.item (selected, 'values')
    id = conteudo[0]
    titulo.set("")
    tema.set("")
    portador.set("")
    retirada.set("")
    devolucao.set("")

    titulo.set(conteudo[1])
    tema.set(conteudo[2])
    portador.set(conteudo[3])
    retirada.set(conteudo[4])
    devolucao.set(conteudo[5])

    updateWindow = Toplevel(root)
    updateWindow.focus()
    updateWindow.title("Atualizar livro")
    updateWindow.config(bg="#EEA002")
    updateWindow.geometry("380x165")
    updateWindow.resizable(False,False)
    lbl1 = Label(updateWindow,text="Nome do Livro: ")
    lbl2 = Label(updateWindow,text="Tema do Livro: ")
    lbl3 = Label(updateWindow,text="Portador do Livro: ")
    lbl4 = Label(updateWindow,text="Data de retirada: ")
    lbl5 = Label(updateWindow,text="Data de Devolução: ")
    lbl1.config(font=("Helvetica", 12),bg="#EEA002")
    lbl2.config(font=("Helvetica", 12),bg="#EEA002")
    lbl3.config(font=("Helvetica", 12),bg="#EEA002")
    lbl4.config(font=("Helvetica", 12),bg="#EEA002")
    lbl5.config(font=("Helvetica", 12),bg="#EEA002")
    lbl1.grid(row=0, column=0)
    lbl2.grid(row=1, column=0)
    lbl3.grid(row=2, column=0)
    lbl4.grid(row=3, column=0)
    lbl5.grid(row=4, column=0)
    e1 = Entry(updateWindow, textvariable=titulo)
    e1.focus_set()
    e2 = Entry(updateWindow, textvariable=tema)
    e3 = Entry(updateWindow, textvariable=portador)
    e4 = Entry(updateWindow, textvariable=retirada)
    e5 = Entry(updateWindow, textvariable=devolucao)
    def atualizar():
        tv.delete(*tv.get_children())
        db.updateData(id,titulo.get(),tema.get(), portador.get(), retirada.get(), devolucao.get())
        showData()
        updateWindow.destroy()
    e1.grid(row=0,column=2)
    e2.grid(row=1,column=2)
    e3.grid(row=2,column=2)
    e4.grid(row=3,column=2)
    e5.grid(row=4,column=2)
    e1.bind("<Return>", lambda ent1:e2.focus_set())
    e2.bind("<Return>", lambda ent2:e3.focus_set())
    e3.bind("<Return>", lambda ent3:e4.focus_set())
    e4.bind("<Return>", lambda ent4:e5.focus_set())
    saveButton = Button(updateWindow, text="Atualizar", padx=10, command = atualizar)
    saveButton.grid(row=6, column=1, sticky=N, padx=15, pady=10)
    def atualizarBook(event):
        atualizar()
    e5.bind("<Return>", atualizarBook)


def clearSearch(event):
    searchEntry.delete(0, END)

def bookSearchEnter(event):
    bookSearch()

def bookSearch():
    if buscar.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect("livros.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `books` WHERE `titulo` LIKE ? OR `tema` LIKE ? OR  `portador` LIKE ? OR `retirada` LIKE ? OR `devolucao` LIKE ?", ('%'+str(buscar.get())+'%', '%'+str(buscar.get())+'%', '%'+str(buscar.get())+'%', '%'+str(buscar.get())+'%', '%'+str(buscar.get())+'%'))
        fetch = cursor.fetchall()
        for data in fetch:
            tv.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

frameButtons = Frame(root, padx = 100, pady = 20)
frameButtons.config(bg='#1f2333')
frameButtons.pack(anchor=NW)
b = Button(frameButtons,text = "Inserir novo livro", pady = 5, padx = 5, command=bookInsert)
b.config(font=("Helvetica", 12), bg='#07C39E')
b.grid(row = 0, column = 0, sticky=W,)
b3 = Button(frameButtons, text="Deletar Livro", pady = 5, padx = 5, command=bookDelete)
b3.config(font=("Helvetica", 12), bg="#CB4335")
b3.grid(row = 0, column = 2, sticky=E, padx=340)

def showData():
    for row in db.selectData():
        tv.insert("", END, values=row)

def showAllData():
    tv.delete(*tv.get_children())
    showData()

frameSearch = Frame(root)
frameSearch.config(bg='#1f2333')
frameSearch.pack()
searchEntry = Entry(frameSearch, textvariable=buscar)
searchEntry.insert(END, "Busque aqui")
searchEntry.config(font=("Helvetica", 10))
searchEntry.pack(side = LEFT)
searchEntry.bind("<FocusIn>", clearSearch)
searchEntry.bind("<Return>", bookSearchEnter )
showAllButton = Button (frameSearch, text="Mostrar todos", command=showAllData)
showAllButton.config(font=("Helvetica", 10),bg='#0274EE')
showAllButton.pack(side=RIGHT)
searchButton = Button (frameSearch, text="Buscar", command=bookSearch)  
searchButton.config(font=("Helvetica", 10),bg='#A7B428')
searchButton.pack(side=RIGHT, padx=5)

frameTable = Frame(root)
frameTable.pack()

scrollbarX = Scrollbar(frameTable, orient=HORIZONTAL)
scrollbarY = Scrollbar(frameTable, orient=VERTICAL)

tv = ttk.Treeview(frameTable, columns = ("id","Titulo", "Tema", "Portador", "Data de Retirada", "Data de Entrega"), show='headings', yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)

style = ttk.Style(root)
style.theme_use("clam")

scrollbarY.config(command=tv.yview)
scrollbarY.pack(side=RIGHT, fill=Y)
scrollbarX.config(command=tv.xview)
scrollbarX.pack(side=BOTTOM, fill=X)

tv.column("#0", width = 0, stretch=NO)
tv.column("id", minwidth= 0,width=0, stretch=NO)
tv.column("Titulo", anchor=CENTER)
tv.column("Tema",anchor=CENTER,width=80)
tv.column("Portador",anchor=CENTER)
tv.column("Data de Retirada",anchor=CENTER,width=100)
tv.column("Data de Entrega",anchor=CENTER,width=100)

tv.heading("#0", text="", anchor=CENTER)
tv.heading("Titulo", text="Titulo", anchor=CENTER)
tv.heading("Tema", text="Tema", anchor=CENTER)
tv.heading("Portador", text="Portador", anchor=CENTER)
tv.heading("Data de Retirada",text="Data de Retirada",anchor=CENTER)
tv.heading("Data de Entrega",text="Data de Entrega",anchor=CENTER)

tv.pack()
tv.bind('<Double-Button-1>', bookUpdate)
tv.bind("<Return>", bookUpdate)
txt = Label (root, text="Clique duas vezes em uma linha, ou pressione Enter \n com ela selecionada para alterar os dados.")
txt.config(font=("Helvetica", 20), bg='#1f2333', fg="#f2f2f2")
txt.pack()

if __name__ == '__main__':
    db.createTable()
    showData()
    mainloop()