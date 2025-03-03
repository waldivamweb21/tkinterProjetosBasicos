from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Cores
co0 = "#feffff"
co1 = "#ffffff"  # Adicionada definição da cor co1
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"
co10 = "#6e8faf"
co11 = "#f2f4f2"

# Janela
janela = Tk()
janela.title("Orçamento")
janela.geometry("250x400")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

# Estilo ttk
style = ttk.Style(janela)
style.theme_use("clam")

# Frames
frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=300, height=90, bg=co2, relief="solid")
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=300, height=290, bg=co3, relief="solid")
frameBaixo.grid(row=2, column=0)

# Título
app_ = Label(frameCima, text="Budget", compound=LEFT, padx=5,
             relief=FLAT, anchor=NW, font=("Verdana", 20), bg=co1, fg=co4)
app_.place(x=0, y=5)

# Logo
try:
    app_img = Image.open("logo.jpeg")
    app_img = app_img.resize((40, 40), Image.LANCZOS)  # Melhor qualidade na redimensionação
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(frameCima, image=app_img, compound=LEFT,
                     padx=5, relief=FLAT, anchor=NW, bg=co1)
    app_logo.place(x=150, y=5)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

# Linha separadora
l_linha = Label(frameCima, width=295, height=1, anchor=NW,
                font=("Verdana", 1), bg=co3, fg=co1)
l_linha.place(x=0, y=47)


# Frame do Meio

_valor_quantia = Label(frameMeio, text="Renda Mensal?", height=1, anchor=NW,
                        font=("Ivy 10"), bg=co1, fg=co4)
_valor_quantia.place(x=7, y=15)

e_valor_quantia = Entry(frameMeio, width=10, font=("Ivy 14"), justify="center", relief="solid")
e_valor_quantia.place(x=10, y=40)


def calcular():
    renda_mensal = float(e_valor_quantia.get())
    vlr_50_porcento = (50/100) * renda_mensal
    vlr_30_porcento = (30/100) * renda_mensal
    vlr_20_porcento = (20/100) * renda_mensal
    
    l_necessidades["text"] = "R${:,.2f}".format(vlr_50_porcento)
    l_necessidades["text"] = "R${:,.2f}".format(vlr_30_porcento)
    l_necessidades["text"] = "R${:,.2f}".format(vlr_20_porcento)

botao_calcular = Button(frameMeio, anchor=NW, text="Calcular".upper(),overrelief=RIDGE,
                        font=("ivy 9"), bg=co1, fg=co0, command=calcular)
botao_calcular.place(x=150, y=40)

#Frame baixo

l_nome = Label(frameBaixo, text="Numeros de 50/30/20 %", padx=10, width=35,
               height=1, anchor=NW, font=("Verdana 11"), bg=co3, fg=co1)
l_nome.place(x=0, y=0)


l_total_necessidades = Label(frameBaixo, text="Necessidades", height=1, anchor=E,
                            font=("Verdana 10"), bg=co1, fg=co4)
l_total_necessidades.place(x=10, y=40)



l_necessidades = Label(frameBaixo, width=22, height=1, anchor=NW,
                            font=("Verdana 11"), bg=co1, fg=co4)
l_necessidades.place(x=10, y=75)


l_total_desejos = Label(frameBaixo, text="Desejos", height=1, anchor=E,
                            font=("Verdana 10"), bg=co9, fg=co0)
l_total_desejos.place(x=10, y=115)


l_desejos = Label(frameBaixo, width=22, height=1, anchor=NW,
                            font=("Verdana 12"), bg=co1, fg=co4)
l_desejos.place(x=10, y=145)


l_total_poupanca = Label(frameBaixo, text="Poupança", height=1, anchor=E,
                            font=("Verdana 10"), bg=co9, fg=co0)
l_total_poupanca.place(x=10, y=185)

l_poupanca = Label(frameBaixo, width=22, height=1, anchor=NW,
                            font=("Verdana 12"), bg=co1, fg=co4)
l_poupanca.place(x=10, y=215)


# Loop da janela
janela.mainloop()

