from tkinter import *
from tkinter import ttk

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

       
def colocar_texto_string(imagem,entrada1,x,y,tamanho):
    
    escrever = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype("App_Loja/CAMBRIA.TTC", tamanho)
    escrever.text((x,y), entrada1, font=fonte,  fill=(0,0,0))

    return imagem


def colocar_texto_float(imagem,entrada2,x,y,tamanho):

    escrever = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype("App_Loja/CAMBRIA.TTC", tamanho)
    escrever.text((x,y), entrada2, font=fonte,  fill=(0,0,0))

    return imagem
    
    

def botao():

    imagem =  Image.open('App_Loja/Vieira_nota.jpg')

    entrada1 = entrada_tipop.get()
    colocar_texto_string(imagem, entrada1, 800, 75, 35)
   
    entrada2 = entrada_datap.get()
    colocar_texto_string(imagem, entrada2, 800, 250, 35)

    entrada3 = entrada_nome.get()
    colocar_texto_string(imagem, entrada3, 140, 305, 35)

    entrada4 = entrada_end.get()
    colocar_texto_string(imagem, entrada4, 120, 350, 35)

    entrada5 = entrada_fone.get()
    colocar_texto_string(imagem, entrada5, 800, 350, 35)

    entrada6 = entrada_cpf.get()
    colocar_texto_string(imagem, entrada6, 100, 398, 35)

    entrada7 = entrada_quant_iten.get()
    colocar_texto_float(imagem,entrada7, 40, 492, 35)
    
    entrada8 = entrada_nome_iten.get()
    colocar_texto_string(imagem, entrada8, 160, 492, 35)

    entrada9 = entrada_valor_iten.get()
    colocar_texto_float(imagem, entrada9, 790, 492, 35)

    entrada7_float = float(entrada7)
    entrada9_float = float(entrada9)
    valor_total = entrada7_float * entrada9_float
    valor_total_str = str(valor_total)
    
    Label(tela, text = f" Valor Total: R$ {valor_total}").grid(row=9, column=6, sticky=W)
    colocar_texto_float(imagem, valor_total_str, 940, 492, 35)

    imagem.save("Imagem_edit.jpg")
    

tela = Tk()
tela.title("Gerar Nota")
tela.geometry("800x300+600+350")
tela.iconbitmap("App_Loja/icon.ico")

#tela.minsize(width=500,height=300)
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

Label(tela, text = "Quantidade: ").grid(row=9, column=0, sticky=W)
entrada_quant_iten = Entry(tela)
entrada_quant_iten.grid(row=9, column=1)

Label(tela, text = " Nome Item: ").grid(row=9, column=2, sticky=W)
entrada_nome_iten = Entry(tela)
entrada_nome_iten.grid(row=9, column=3)

Label(tela, text = " Valor Unidade R$: ").grid(row=9, column=4, sticky=W)
entrada_valor_iten = Entry(tela)
entrada_valor_iten.grid(row=9, column=5)

Label(tela, text = "\nFinalizar: ").grid(row=10, sticky=W)



botaosalvar = Button(tela, text="Salvar", command=botao)
botaosalvar.grid(row=11, column=3)

tela.mainloop()