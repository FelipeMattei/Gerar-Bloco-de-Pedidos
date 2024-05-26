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

def calcular_final(quantidade,valor):

    for contador in range(len(quantidade)):

        quantidade_float = float(quantidade[contador])
        valor_float = float(valor[contador])

        soma = quantidade_float * valor_float
        soma_str = str(soma)

        Label(tela, text=f"Valor total R$:{soma_str}").grid(row=(9+contador), column=7, sticky=W)

        soma_total = soma_total + soma


    
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

    calcular_final(entrada_quant_iten,entrada_valor_iten)

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


for contador in range(9):

    Label(tela, text = "Quantidade: ").grid(row=(9+contador), column=0, sticky=W)
    quant_iten = Entry(tela)
    entrada_quant_iten.append(quant_iten)
    entrada_quant_iten[contador].grid(row=(9+contador), column=1)
    entrada_quant_iten[contador] = entrada_quant_iten[contador].get()
        

    Label(tela, text = " Nome Item: ").grid(row=(9+contador), column=2, sticky=W)
    entrada_nome_iten = Entry(tela)
    entrada_nome_iten.grid(row=(9+contador), column=3)

    Label(tela, text = " Valor Unidade R$: ").grid(row=(9+contador), column=4, sticky=W)
    valor_iten = Entry(tela)
    entrada_valor_iten.append(valor_iten)
    entrada_valor_iten[contador].grid(row=(9+contador), column=5)
    entrada_valor_iten[contador] = entrada_valor_iten[contador].get()



# if soma_total != 0:
#     str(soma_total)
#     Label(tela, text = "\nFinalizar: ").grid(row=22, sticky=W)
#     Label(tela, text=f"Total da compra:{soma_total}").grid(row=23)



botaosalvar = Button(tela, text="Salvar", command=botao)
botaosalvar.grid(row=24, column=3)

tela.mainloop()