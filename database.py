import sqlite3

def createTable():
    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo text, tema text, portador text, retirada text, devolucao text)"
    cursor.execute(query) 
    conn.commit()
    cursor.close()
    conn.close()

def createData(titulo, tema, portador, retirada, devolucao):
    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()
    query = """ INSERT INTO books (titulo, tema, portador, retirada, devolucao) VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(query, (str(titulo), str(tema), str(portador), str(retirada), str(devolucao)))
    conn.commit()
    cursor.close()
    conn.close()

def selectData():
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute('select * from books')
    fetch = cur.fetchall()
    cur.close()
    conn.close()
    return fetch


def updateData(id, titulo, tema, portador, retirada, devolucao):
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET titulo = ?, tema = ?, portador = ?, retirada = ?, devolucao = ? WHERE id = ?",
                (titulo, tema, portador, retirada, devolucao, id))
    conn.commit()
    cur.close()
    conn.close()

def deleteData(id):
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    cur.close()
    conn.close()