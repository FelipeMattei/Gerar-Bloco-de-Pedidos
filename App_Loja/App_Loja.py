from tkinter import *
from tkinter import ttk

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

       
def colocar_texto(imagem,entrada1,x,y,tamanho):
    
    escrever = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype("App_Loja/CAMBRIA.TTC", tamanho)
    escrever.text((x,y), entrada1, font=fonte,  fill=(0,0,0))

    return imagem

def colocar_texto_float(imagem,entrada,x,y,tamanho):

    escrever = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype("App_Loja/CAMBRIA.TTC", tamanho)
    entrada_str = str(entrada)
    escrever.text((x,y), entrada_str, font=fonte,  fill=(0,0,0))

    return imagem


def calcular_final():

    try:
        limpar_resultados()

        soma_total=0

        for i in range(9):

            qtd = entrada_quant_iten[i].get()
            val = entrada_valor_iten[i].get()

            qtd = float(qtd) if qtd else 0
            val = float(val) if val else 0

            produto = qtd * val

            resultados[i].config(text=f"Resultado R$:{produto}")

            soma_total += produto

        resultado_final.config(text=f"Valor total R$:{soma_total}")

    except ValueError:

        resultado_final.config(text="Por favor, insira valores válidos!")


def limpar_resultados():
    for label in resultados:
        label.config(text="")      
        
    
def botao():

    imagem =  Image.open('App_Loja/Vieira_nota.jpg')

    entrada1 = entrada_tipop.get()
    colocar_texto(imagem, entrada1, 800, 75, 35)
   
    entrada2 = entrada_datap.get()
    colocar_texto(imagem, entrada2, 800, 250, 35)

    entrada3 = entrada_nome.get()
    colocar_texto(imagem, entrada3, 140, 305, 35)

    entrada4 = entrada_end.get()
    colocar_texto(imagem, entrada4, 120, 350, 35)

    entrada5 = entrada_fone.get()
    colocar_texto(imagem, entrada5, 800, 350, 35)

    entrada6 = entrada_cpf.get()
    colocar_texto(imagem, entrada6, 100, 398, 35)
    

    # entrada7 = entrada_quant_iten[0].get()
    # colocar_texto_float(imagem, entrada7, 50, 493, 35)
    # entrada8 = entrada_quant_iten[1].get()
    # colocar_texto_float(imagem, entrada7, 50, 530, 35)

    entrada = []
    for i in range(9):

        entradas = entrada_quant_iten[i].get()
        entrada.append(entradas)
        colocar_texto_float(imagem, entrada[i] ,50,493+(37*i),35)

    calcular_final()


    imagem.save("Imagem_edit.jpg")


tela = Tk()
tela.title("Gerar Nota")
tela.geometry("800x500+600+350")
tela.iconbitmap("App_Loja/icon.ico")

tela.resizable(True,True)

Label(tela, text= "Informações Pedido:").grid(row=0, sticky=W)

Label(tela, text = "Tipo Pedido: ").grid(row=1, sticky=W)
entrada_tipop = Entry(tela)
entrada_tipop.grid(row=1, column=1)

Label(tela, text = "Data Pedido: ").grid(row=2, sticky=W)
entrada_datap = Entry(tela)
entrada_datap.grid(row=2, column=1)

Label(tela, text= "\nInformações Comprador:").grid(row=3, sticky=W)

Label(tela, text = "Nome: ").grid(row=4, sticky=W)
entrada_nome = Entry(tela)
entrada_nome.grid(row=4, column=1)

Label(tela, text = "Endereço: ").grid(row=5, sticky=W)
entrada_end = Entry(tela)
entrada_end.grid(row=5, column=1)

Label(tela, text = "Fone: ").grid(row=6, sticky=W)
entrada_fone = Entry(tela)
entrada_fone.grid(row=6, column=1)

Label(tela, text = "CPF: ").grid(row=7, sticky=W)
entrada_cpf = Entry(tela)
entrada_cpf.grid(row=7, column=1)

Label(tela, text = "\nInformações Itens: ").grid(row=8, sticky=W)

###    Laço de repetição para criar vários Labels, que seriam as linhas e colunas para colocar os produtos.

entrada_quant_iten = []
entrada_valor_iten = []
resultados = []


for contador in range(9):
    
    Label(tela, text = "Quantidade: ").grid(row=(9+contador), column=0, sticky=W)
    quant_iten = Entry(tela)
    quant_iten.grid(row=(9+contador), column=1)
    entrada_quant_iten.append(quant_iten)
    
    Label(tela, text = " Nome Item: ").grid(row=(9+contador), column=2, sticky=W)
    entrada_nome_iten = Entry(tela)
    entrada_nome_iten.grid(row=(9+contador), column=3)

    Label(tela, text = " Valor Unidade R$: ").grid(row=(9+contador), column=4, sticky=W)
    valor_iten = Entry(tela)
    valor_iten.grid(row=(9+contador), column=5)
    entrada_valor_iten.append(valor_iten)

    resultado_produto = Label(tela, text="")
    resultado_produto.grid(row=(9+contador), column=6, sticky=W)
    resultados.append(resultado_produto)


Label(tela, text = "\nFinalizar: ").grid(row=22, sticky=W)

resultado_final = Label(tela, text="")
resultado_final.grid(row=23, column=2, sticky=W)


botaosalvar = Button(tela, text="Salvar", command=botao)
botaosalvar.grid(row=24, column=3)

tela.mainloop()