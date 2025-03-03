from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
import os

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Orçamento")
        self.root.geometry("250x400")
        self.root.configure(background=self.colors["white"])
        self.root.resizable(width=False, height=False)

        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")

        self.create_frames()
        self.create_widgets()

    # Dicionário de cores
    colors = {
        "white": "#ffffff",
        "green": "#4fa882",
        "dark_blue": "#38576b",
        "gray": "#403d3d",
        "orange": "#e06636",
        "blue": "#038cfc",
        "cyan": "#3fbfb9",
        "dark_gray": "#263238",
        "light_gray": "#e9edf5",
        "soft_blue": "#6e8faf",
        "background": "#f2f4f2",
    }

    def create_frames(self):
        """Criação dos frames da interface."""
        self.frame_top = Frame(self.root, width=300, height=50, bg=self.colors["white"], relief="flat")
        self.frame_top.grid(row=0, column=0)

        self.frame_middle = Frame(self.root, width=300, height=90, bg=self.colors["green"], relief="solid")
        self.frame_middle.grid(row=1, column=0)

        self.frame_bottom = Frame(self.root, width=300, height=290, bg=self.colors["dark_blue"], relief="solid")
        self.frame_bottom.grid(row=2, column=0)

    def create_widgets(self):
        """Criação dos widgets da interface."""
        # Título
        Label(self.frame_top, text="Budget", padx=5, relief=FLAT, anchor=NW,
              font=("Verdana", 20), bg=self.colors["white"], fg=self.colors["gray"]).place(x=10, y=5)

        # Carregar imagem (logo)
        self.load_image("logo.jpeg")

        # Linha separadora
        Label(self.frame_top, width=295, height=1, anchor=NW, font=("Verdana", 1),
              bg=self.colors["dark_blue"], fg=self.colors["white"]).place(x=0, y=47)

        # Frame do meio - Entrada e botão
        Label(self.frame_middle, text="Renda Mensal:", height=1, anchor=NW,
              font=("Ivy 10"), bg=self.colors["white"], fg=self.colors["gray"]).place(x=10, y=15)

        self.entry_valor = Entry(self.frame_middle, width=10, font=("Ivy 14"), justify="center", relief="solid")
        self.entry_valor.place(x=10, y=40)

        Button(self.frame_middle, text="Calcular".upper(), overrelief=RIDGE,
               font=("Ivy 9"), bg=self.colors["white"], fg=self.colors["green"],
               command=self.calculate_budget).place(x=150, y=40)

        # Frame de resultados
        Label(self.frame_bottom, text="Números 50/30/20%", padx=10, width=35,
              height=1, anchor=NW, font=("Verdana 11"), bg=self.colors["dark_blue"], fg=self.colors["white"]).place(x=0, y=0)

        self.create_result_labels()

    def create_result_labels(self):
        """Cria os rótulos para exibir os resultados do cálculo."""
        self.labels = {}

        categories = [("Necessidades", 40), ("Desejos", 115), ("Poupança", 185)]
        for category, y_position in categories:
            Label(self.frame_bottom, text=category, height=1, anchor=E,
                  font=("Verdana 10"), bg=self.colors["light_gray"], fg=self.colors["gray"]).place(x=10, y=y_position)

            self.labels[category] = Label(self.frame_bottom, width=22, height=1, anchor=NW,
                                          font=("Verdana 11"), bg=self.colors["white"], fg=self.colors["gray"])
            self.labels[category].place(x=10, y=y_position + 30)

    def load_image(self, image_path):
        """Tenta carregar uma imagem e exibi-la no frame_top."""
        if os.path.exists(image_path):
            try:
                img = Image.open(image_path)
                img = img.resize((40, 40), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)

                logo_label = Label(self.frame_top, image=img, bg=self.colors["white"])
                logo_label.image = img  # Manter referência da imagem
                logo_label.place(x=180, y=5)
            except Exception as e:
                print(f"Erro ao carregar a imagem: {e}")
        else:
            print("Imagem não encontrada. Verifique o caminho.")

    def calculate_budget(self):
        """Calcula e exibe os valores baseados na regra 50/30/20."""
        try:
            renda_mensal = float(self.entry_valor.get())

            valores = {
                "Necessidades": (50 / 100) * renda_mensal,
                "Desejos": (30 / 100) * renda_mensal,
                "Poupança": (20 / 100) * renda_mensal
            }

            for categoria, valor in valores.items():
                self.labels[categoria]["text"] = f"R$ {valor:,.2f}"

        except ValueError:
            self.entry_valor.delete(0, END)
            self.entry_valor.insert(0, "Valor inválido")

# Inicializando a aplicação
if __name__ == "__main__":
    root = Tk()
    app = BudgetApp(root)
    root.mainloop()
