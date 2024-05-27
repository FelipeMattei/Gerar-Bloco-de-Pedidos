from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

       
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
    global soma_total
    global resultados_nume

    try:
        limpar_resultados()

        resultados_nume = []
        soma_total=0

        for i in range(19):

            qtd = entrada_quant_iten[i].get()
            val = entrada_valor_iten[i].get()

            qtd = float(qtd) if qtd else 0
            val = float(val) if val else 0

            produto = qtd * val
            produto = round(produto, 2)

            resultados[i].config(text=f"R$:{produto}")
            resultados_nume.append(produto)

            soma_total += produto

        resultado_final.config(text=f"Valor total R$:{soma_total}")
        
    except ValueError:

        resultado_final.config(text="Por favor, insira valores válidos!")


def limpar_resultados():
    
    for label in resultados:
        label.config(text="") 
  

def salvar_pdf(imagem):
        resposta = messagebox.askyesno("Salvar como PDF", "Você quer salvar a imagem como PDF?")
        if resposta:
            caminho_pdf = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF files", "*.pdf")],title="Salvar PDF como")
            if caminho_pdf:
                c = canvas.Canvas(caminho_pdf, pagesize=A4)
                c.drawImage(imagem, 0, 0, width=A4[0], height=A4[1])
                c.showPage()
                c.save()
                
                messagebox.showinfo("Sucesso", "Imagem salva como PDF com sucesso!")
        else:
            messagebox.showinfo("Continuar", "Você escolheu não salvar como PDF. Continue editando a imagem.")


def botao():

    imagem =  Image.open('App_Loja/Vieira_nota.png')

    entrada1 = entrada_tipop.get()
    colocar_texto(imagem, entrada1, 800, 73, 35)
   
    entrada2 = entrada_datap.get()
    colocar_texto(imagem, entrada2, 800, 247, 35)

    entrada3 = entrada_nome.get()
    colocar_texto(imagem, entrada3, 140, 302, 35)

    entrada4 = entrada_end.get()
    colocar_texto(imagem, entrada4, 120, 347, 35)

    entrada5 = entrada_fone.get()
    colocar_texto(imagem, entrada5, 800, 347, 35)

    entrada6 = entrada_cpf.get()
    colocar_texto(imagem, entrada6, 100, 395, 35)

    entrada_qtd = []
    for i in range(19):
        entradas_qtd = entrada_quant_iten[i].get()
        entrada_qtd.append(entradas_qtd)
        colocar_texto_float(imagem, entrada_qtd[i] ,50,493+(37*i),35)
    
    entrada_nm = []
    for i in range(19):
       entradas_nm = entrada_nome_iten[i].get()
       entrada_nm.append(entradas_nm)
       colocar_texto(imagem,entrada_nm[i], 200,493+(37*i),35)

    entrada_vlr = []
    for i in range(19):
        entradas_vlr = entrada_valor_iten[i].get()
        entrada_vlr.append(entradas_vlr)
        colocar_texto_float(imagem,entrada_vlr[i], 800,493+(37*i),35)

    calcular_final()
    texto_resultado = []

    for i in range(19):
        textos = resultados_nume[i]
        texto_resultado.append(textos)
        colocar_texto_float(imagem, texto_resultado[i],950,493+(37*i),35)

    entrada7 = soma_total
    colocar_texto_float(imagem,entrada7, 950,1205,35)

    imagem_editada = "App_Loja/Nota_edit.png"
    imagem.save(imagem_editada)

    salvar_pdf(imagem_editada)


tela = Tk()
tela.title("Gerar Nota")
tela.iconbitmap("App_Loja/icon.ico")
tela.geometry("+550+200")

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
entrada_nome_iten = []




for contador in range(19):
    
    Label(tela, text = "Quantidade: ").grid(row=(9+contador), column=0, sticky=W)
    quant_iten = Entry(tela)
    quant_iten.grid(row=(9+contador), column=1)
    entrada_quant_iten.append(quant_iten)
    
    Label(tela, text = " Nome Item: ").grid(row=(9+contador), column=2, sticky=W)
    nome_iten = Entry(tela)
    nome_iten.grid(row=(9+contador), column=3)
    entrada_nome_iten.append(nome_iten)

    Label(tela, text = " Valor Unidade R$: ").grid(row=(9+contador), column=4, sticky=W)
    valor_iten = Entry(tela)
    valor_iten.grid(row=(9+contador), column=5)
    entrada_valor_iten.append(valor_iten)

    resultado_produto = Label(tela, text="")
    resultado_produto.grid(row=(9+contador), column=6, sticky=W)
    resultados.append(resultado_produto)


Label(tela, text = "\nFinalizar: ", font=(12)).grid(row=31, sticky=W)

resultado_final = Label(tela, text="", font=(12), bg="#FFFFFF")
resultado_final.grid(row=31, column=5, sticky=W)

botaosalvar = Button(tela, text="Salvar", command=botao, width=15, height=3, bg= "#FFFFFF")
botaosalvar.grid(row=33, column=2)


tela.mainloop()