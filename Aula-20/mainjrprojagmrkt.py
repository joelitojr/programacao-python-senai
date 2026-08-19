# sistema básico de gerenciamento de acervo de locadora de vídeo
import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def conectar():
    return sqlite3.connect("locadora.db")

def init_db():
    """Cria o banco de dados e a tabela se não existirem."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            classind INTEGER NOT NULL,
            direcao TEXT,
            estudio TEXT
        )
    ''')
    conn.commit()
    conn.close()

class AppLocadora(ctk.CTk):
    def __init__(locadora):
        super().__init__()
        
        locadora.title("Gerenciamento de Acervo - Locadora")
        locadora.geometry("750x650")
        
        # Título
        locadora.lbl_titulo = ctk.CTkLabel(locadora, text="Cadastro de Filmes", font=("Arial", 20, "bold"))
        locadora.lbl_titulo.pack(pady=10)
        
        # Frame de Entrada de Dados
        locadora.frame_form = ctk.CTkFrame(locadora)
        locadora.frame_form.pack(pady=10, padx=20, fill="x")
        
        # ID (Apenas para Update/Delete)
        locadora.lbl_id = ctk.CTkLabel(locadora.frame_form, text="ID (para Alterar/Excluir):")
        locadora.lbl_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        locadora.txt_id = ctk.CTkEntry(locadora.frame_form, width=100)
        locadora.txt_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # Título
        locadora.lbl_nome = ctk.CTkLabel(locadora.frame_form, text="Título:")
        locadora.lbl_nome.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        locadora.txt_nome = ctk.CTkEntry(locadora.frame_form, width=300)
        locadora.txt_nome.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Gênero
        locadora.lbl_genero = ctk.CTkLabel(locadora.frame_form, text="Gênero:")
        locadora.lbl_genero.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        locadora.txt_genero = ctk.CTkEntry(locadora.frame_form, width=300)
        locadora.txt_genero.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        # Classificação Indicativa
        locadora.lbl_classind = ctk.CTkLabel(locadora.frame_form, text="Classificação:")
        locadora.lbl_classind.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        locadora.txt_classind = ctk.CTkEntry(locadora.frame_form, width=100)
        locadora.txt_classind.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        # Direção
        locadora.lbl_direcao = ctk.CTkLabel(locadora.frame_form, text="Direção:")
        locadora.lbl_direcao.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        locadora.txt_direcao = ctk.CTkEntry(locadora.frame_form, width=300)
        locadora.txt_direcao.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        # Estúdio
        locadora.lbl_estudio = ctk.CTkLabel(locadora.frame_form, text="Estúdio:")
        locadora.lbl_estudio.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        locadora.txt_estudio = ctk.CTkEntry(locadora.frame_form, width=300)
        locadora.txt_estudio.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        
        # Frame de Botões (CRUD)
        locadora.frame_botoes = ctk.CTkFrame(locadora, fg_color="transparent")
        locadora.frame_botoes.pack(pady=10)
        
        locadora.btn_inserir = ctk.CTkButton(locadora.frame_botoes, text="Cadastrar", command=locadora.incluir_filme, fg_color="green")
        locadora.btn_inserir.grid(row=0, column=0, padx=5)
        
        locadora.btn_atualizar = ctk.CTkButton(locadora.frame_botoes, text="Atualizar", command=locadora.atualizar_filme, fg_color="orange")
        locadora.btn_atualizar.grid(row=0, column=1, padx=5)
        
        locadora.btn_deletar = ctk.CTkButton(locadora.frame_botoes, text="Excluir", command=locadora.deletar_filme, fg_color="red")
        locadora.btn_deletar.grid(row=0, column=2, padx=5)
        
        locadora.btn_limpar = ctk.CTkButton(locadora.frame_botoes, text="Limpar", command=locadora.limpar_campos)
        locadora.btn_limpar.grid(row=0, column=3, padx=5)
        
        # Caixa de Texto para Exibição
        locadora.frame_lista = ctk.CTkTextbox(locadora, width=700, height=200)
        locadora.frame_lista.pack(pady=10, padx=20)
        
        # Inicializa banco e carrega registros
        init_db()
        locadora.atualizar_lista()

    def limpar_campos(locadora):
        """Limpa todos os campos de entrada."""
        locadora.txt_id.delete(0, "end")
        locadora.txt_nome.delete(0, "end")
        locadora.txt_genero.delete(0, "end")
        locadora.txt_classind.delete(0, "end")
        locadora.txt_direcao.delete(0, "end")
        locadora.txt_estudio.delete(0, "end")

    def atualizar_lista(locadora):
        """Busca os filmes no banco e carrega/exibe no campo de texto."""
        locadora.frame_lista.configure(state="normal")
        locadora.frame_lista.delete("0.0", "end")
        
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, genero, classind, direcao, estudio FROM filmes ORDER BY id DESC")
        filmes = cursor.fetchall()
        conn.close()
        
        if not filmes:
            locadora.frame_lista.insert("0.0", "Nenhum filme cadastrado no acervo.")
        else:
            for filme in filmes:
                linha = f"ID: {filme[0]} | Título: {filme[1]} | Gênero: {filme[2]} | Class.: {filme[3]} | Dir: {filme[4]} | Est: {filme[5]}\n"
                locadora.frame_lista.insert("end", linha)
                
        locadora.frame_lista.configure(state="disabled")

    def incluir_filme(locadora):
        """Coleta os dados dos campos e salva no SQLite3 (Insert)."""
        titulo = locadora.txt_nome.get().strip()
        genero = locadora.txt_genero.get().strip()
        classind = locadora.txt_classind.get().strip()
        direcao = locadora.txt_direcao.get().strip()
        estudio = locadora.txt_estudio.get().strip()
        
        if not titulo or not genero or not classind:
            messagebox.showwarning("Aviso", "Preencha os campos obrigatórios: Título, Gênero e Classificação.")
            return
            
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO filmes (titulo, genero, classind, direcao, estudio)
                VALUES (?, ?, ?, ?, ?)
            ''', (titulo, genero, int(classind), direcao, estudio))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Sucesso", "Filme cadastrado com sucesso!")
            locadora.limpar_campos()
            locadora.atualizar_lista()
        except ValueError:
            messagebox.showerror("Erro", "Classificação indicativa deve ser um número inteiro.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

    def atualizar_filme(locadora):
        """Atualiza os dados de um filme existente com base no ID (Update)."""
        filme_id = locadora.txt_id.get().strip()
        titulo = locadora.txt_nome.get().strip()
        genero = locadora.txt_genero.get().strip()
        classind = locadora.txt_classind.get().strip()
        direcao = locadora.txt_direcao.get().strip()
        estudio = locadora.txt_estudio.get().strip()
        
        if not filme_id:
            messagebox.showwarning("Aviso", "Informe o ID do filme que deseja atualizar.")
            return
            
        if not titulo or not genero or not classind:
            messagebox.showwarning("Aviso", "Preencha Título, Gênero e Classificação.")
            return
            
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE filmes 
                SET titulo = ?, genero = ?, classind = ?, direcao = ?, estudio = ?
                WHERE id = ?
            ''', (titulo, genero, int(classind), direcao, estudio, int(filme_id)))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Sucesso", "Filme atualizado com sucesso!")
            locadora.limpar_campos()
            locadora.atualizar_lista()
        except ValueError:
            messagebox.showerror("Erro", "ID e Classificação devem ser números inteiros.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {e}")

    def deletar_filme(locadora):
        """Exclui um filme do banco com base no ID (Delete)."""
        filme_id = locadora.txt_id.get().strip()
        
        if not filme_id:
            messagebox.showwarning("Aviso", "Informe o ID do filme que deseja excluir.")
            return
            
        if messagebox.askyesno("Confirmação", "Deseja realmente excluir este filme?"):
            try:
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM filmes WHERE id = ?", (int(filme_id),))
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Sucesso", "Filme excluído com sucesso!")
                locadora.limpar_campos()
                locadora.atualizar_lista()
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número inteiro.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir: {e}")

if __name__ == "__main__":
    app = AppLocadora()
    app.mainloop()