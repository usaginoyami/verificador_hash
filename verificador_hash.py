import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

CHUNK_SIZE = 1024 * 1024  # Lê em blocos de 1 MB para suportar arquivos grandes.

def calcular_hash(caminho, algoritmo):
    """Calcula o hash do arquivo sem carregá-lo inteiro na memória."""
    digest = hashlib.new(algoritmo)
    with open(caminho, "rb") as arquivo:
        while True:
            bloco = arquivo.read(CHUNK_SIZE)
            if not bloco:
                break
            digest.update(bloco)
    return digest.hexdigest()

class VerificadorHashApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificador de Integridade de Arquivos")
        self.root.geometry("650x430")
        self.root.minsize(580, 390)
        self.arquivo = None

        estilo = ttk.Style()
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        principal = ttk.Frame(root, padding=20)
        principal.pack(fill="both", expand=True)

        ttk.Label(
            principal,
            text="Verificador de Hash",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w")

        ttk.Label(
            principal,
            text="Compare um hash conhecido com o conteúdo de um arquivo."
        ).pack(anchor="w", pady=(2, 18))

        ttk.Label(principal, text="1. Selecione o arquivo original/de referência:").pack(anchor="w")
        linha_arquivo = ttk.Frame(principal)
        linha_arquivo.pack(fill="x", pady=(5, 14))

        self.campo_arquivo = ttk.Entry(linha_arquivo)
        self.campo_arquivo.pack(side="left", fill="x", expand=True)
        ttk.Button(linha_arquivo, text="Procurar…", command=self.selecionar_arquivo).pack(side="left", padx=(8, 0))

        ttk.Label(principal, text="2. Escolha o algoritmo do hash:").pack(anchor="w")
        self.algoritmo = tk.StringVar(value="SHA-256")
        ttk.Combobox(
            principal,
            textvariable=self.algoritmo,
            values=("MD5", "SHA-1", "SHA-256", "SHA-512"),
            state="readonly",
            width=18
        ).pack(anchor="w", pady=(5, 14))

        ttk.Label(principal, text="3. Cole o hash que deseja verificar:").pack(anchor="w")
        self.campo_hash = ttk.Entry(principal)
        self.campo_hash.pack(fill="x", pady=(5, 14))
        self.campo_hash.bind("<Return>", lambda event: self.verificar())

        ttk.Button(
            principal,
            text="VERIFICAR ARQUIVO",
            command=self.verificar
        ).pack(fill="x", ipady=7)

        self.resultado = tk.Label(
            principal,
            text="Aguardando verificação.",
            font=("Segoe UI", 12, "bold"),
            fg="#555555",
            anchor="w",
            justify="left",
            wraplength=590
        )
        self.resultado.pack(fill="x", pady=(18, 8))

        self.hash_calculado = tk.Text(principal, height=3, wrap="word", font=("Consolas", 9))
        self.hash_calculado.pack(fill="x")
        self.hash_calculado.insert("1.0", "O hash calculado do arquivo aparecerá aqui.")
        self.hash_calculado.configure(state="disabled")

        ttk.Label(
            principal,
            text="Observação: uma correspondência confirma que o arquivo tem o mesmo conteúdo "
                 "representado pelo hash informado. Para provar a origem/autenticidade, "
                 "o hash precisa vir de uma fonte confiável.",
            wraplength=600,
            foreground="#666666"
        ).pack(anchor="w", pady=(12, 0))

    def selecionar_arquivo(self):
        caminho = filedialog.askopenfilename(title="Selecione o arquivo para verificar")
        if caminho:
            self.arquivo = caminho
            self.campo_arquivo.delete(0, tk.END)
            self.campo_arquivo.insert(0, caminho)
            self.resultado.config(text="Arquivo selecionado. Informe o hash para continuar.", fg="#555555")

    def mostrar_hash(self, valor):
        self.hash_calculado.configure(state="normal")
        self.hash_calculado.delete("1.0", tk.END)
        self.hash_calculado.insert("1.0", valor)
        self.hash_calculado.configure(state="disabled")

    def verificar(self):
        caminho = self.campo_arquivo.get().strip()
        hash_informado = self.campo_hash.get().strip().lower().replace(" ", "")
        nome_algoritmo = self.algoritmo.get()
        algoritmo = nome_algoritmo.lower().replace("-", "")

        if not caminho or not Path(caminho).is_file():
            messagebox.showwarning("Arquivo não selecionado", "Selecione um arquivo válido.")
            return

        if not hash_informado:
            messagebox.showwarning("Hash não informado", "Cole o código hash que deseja comparar.")
            return

        try:
            hash_calculado = calcular_hash(caminho, algoritmo)
        except (OSError, ValueError) as erro:
            messagebox.showerror("Erro ao calcular hash", str(erro))
            return

        self.mostrar_hash(f"{nome_algoritmo}: {hash_calculado}")

        if hash_informado == hash_calculado.lower():
            self.resultado.config(
                text="RESULTADO: HASH COMPATÍVEL\nO arquivo corresponde ao hash informado.",
                fg="#16803c"
            )
        else:
            self.resultado.config(
                text="RESULTADO: HASH DIFERENTE\nO arquivo não corresponde ao hash informado.",
                fg="#c62828"
            )

if __name__ == "__main__":
    janela = tk.Tk()
    app = VerificadorHashApp(janela)
    janela.mainloop()
