from PIL import ImageFont, ImageDraw, Image
import pytesseract
import os
import numpy as np
import re
import cv2 # OpenCV
from dotenv import load_dotenv

load_dotenv()

fonte = f"{os.getenv("url_calibri")}"

texto_completo = ''

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract.exe'

projeto = f"{os.getenv("url_artigo")}\\artigo"

caminho = [os.path.join(projeto, f) for f in os.listdir(projeto)]
titulo = []

def caixa_texto(resultado, img, cor = (255, 100, 0)):
  x = resultado['left'][i]
  y = resultado['top'][i]
  w = resultado['width'][i]
  h = resultado['height'][i]

  cv2.rectangle(img, (x, y), (x+w, y+h), cor, 2)

  return x, y, img

def escreve_texto(texto, x, y, img, fonte, cor =(50, 50, 255), tamanho_texto=15):
  fonte = ImageFont.truetype(fonte, tamanho_texto)
  img_pil = Image.fromarray(img)
  draw = ImageDraw.Draw(img_pil)
  draw.text((x, y - tamanho_texto), texto, font = fonte, fill = cor)
  img = np.array(img_pil)
  return img


def OCR_processa(texto, config_tesseract):
    texto = pytesseract.image_to_string(img, lang='por', config=config_tesseract)
    return texto

#Começo do cod

num_ocorrencias = 0 # OCORRENCIA DE REPETIÇAO DE TERMO_BUSCA

for imagem in caminho:

    img = cv2.imread(imagem)
    if img is None:
        print("Erro ao carregar a imagem. Verifique o caminho.")
    else:

        padrao_data = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
        datas = []
        rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        config_tesseract = r'C:\Program Files\Tesseract\tessdata --psm 6'

        resultado = pytesseract.image_to_data(rgb, lang='por', config=config_tesseract, output_type= pytesseract.Output.DICT)

        ###### TRATAMENTO DE IMAGEM PRO EXPORT
        nome_imagem = os.path.split(imagem)[-1]
        titulo.append(nome_imagem)
        nome_divisao = '===================\n' + str(nome_imagem)
        texto_completo = texto_completo + nome_divisao + '\n'
        texto = OCR_processa(rgb, config_tesseract)
        texto_completo = texto_completo + texto

        # EXPOSIÇAO DE IMAGENS // TRATAMENTO
        img_copia = rgb.copy()
        for i in range(len(resultado['text'])):
            confianca = int(resultado['conf'][i])
            if confianca > 30:
                texto = resultado['text'][i]

                # if not texto.isspace() and len(texto)>1: #TERMO PADRÃO\


                termo_busca = 'learning'
                if termo_busca.lower() in texto.lower():
                    x, y, img = caixa_texto(resultado, img_copia)
                    img_copia = escreve_texto(texto, x, y, img_copia, fonte)
                    num_ocorrencias+= 1
                    

        cv2.imshow("imagem", img_copia)
        # ARMAZENANDO OS RESULTADOS

        novo_nome_imagem = 'OCR_' + nome_imagem
        nova_imagem = 'Img/' + str(novo_nome_imagem)
        cv2.imwrite(nova_imagem, img)

        cv2.waitKey(0)
cv2.destroyAllWindows()
#fim do cod


#SALVA OS TEXTOS LIDOS EM ARQUIVO EXTERNOS
nome_txt = 'resultados_ocr.txt'
with open(nome_txt, 'w', encoding='utf-8') as f:
    f.write(texto_completo)


#FILTRO DE PESQUISA POR PALAVRA
termo_pesquisa = 'learning'

with open(nome_txt) as f:
    secoes = [secao.strip() for secao in f.read().split('===================') if secao.strip()]
    
for title, secao in enumerate(secoes):
    ocorrencias = [i.start() for i in re.finditer(termo_pesquisa.upper(), secao.upper())]
    print("===========\n" + str(titulo[title]))
    print(f"Ocorrências: {termo_pesquisa}:{len(ocorrencias)}\n")
print(f"\n {num_ocorrencias}")