# Processamento de Imagens OCR com Python

Este projeto utiliza as capacidades de processamento de imagens do Python com Tesseract OCR, OpenCV e outras bibliotecas. O objetivo é extrair texto de imagens, destacar certos termos nas imagens e registrar os resultados para análise posterior.
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.5-brightgreen)
![Pytesseract](https://img.shields.io/badge/Pytesseract-0.3.10-blue)


## Funcionalidades

- **Extração de Texto com OCR**: Utiliza `pytesseract` para extrair texto de imagens em português.
- **Realce de Imagens**: Destaca e marca regiões de interesse nas imagens onde certas palavras são detectadas.
- **Pesquisa e Análise de Texto**: Permite pesquisar termos específicos no texto extraído e registra as ocorrências.
- **Exportação de Imagens**: Salva as imagens processadas com as regiões de interesse destacadas.
- **Exportação de Texto**: O texto extraído é salvo em um arquivo `.txt` para uso posterior.

## Configuração

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/gccarvalho1/opencv-ocr.git
    cd opencv-ocr
    ```

2. **Instale as dependências**:
    Use o `pip` para instalar as bibliotecas Python necessárias.
    ```bash
    pip install -r requirements.txt
    ```

3. **Instale o Tesseract**:
    Baixe e instale o [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) no seu sistema. Configure o caminho do `tesseract_cmd` no script da seguinte forma:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract.exe'
    ```

4. **Configuração de variáveis de ambiente**:
    Crie um arquivo `.env` com a seguinte estrutura:
    ```bash
    url_artigo=caminho_para_pasta_de_imagens
    url_calibri=caminho_para_fonte_calibri
    ```

## Como Funciona

1. **Pré-processamento de Imagens**:
   - O script lê todas as imagens de uma pasta especificada e as processa utilizando OpenCV e `pytesseract`.
   
2. **Detecção de Texto**:
   - O texto é extraído das imagens usando o OCR do Tesseract, e os resultados são armazenados em um formato estruturado. O script também busca padrões específicos (ex: datas) e um termo-alvo (ex: "learning").

3. **Realce de Texto**:
   - Para cada ocorrência do termo de pesquisa, o script destaca a caixa delimitadora do texto detectado na imagem e a anota com uma fonte especificada.

4. **Exportação de Resultados**:
   - As imagens processadas são salvas com as áreas de texto realçadas, e um arquivo de texto é gerado contendo todo o texto extraído com as seções marcadas.

## Exemplo

Aqui está um exemplo de uma imagem antes e depois do reconhecimento de texto e do realce:

### Imagem Original

![Imagem Original](/artigo/Aula5-Visao.png)

### Imagem Processada

![Imagem Processada](/Img/OCR_Aula5-Visao.png)


Na imagem processada, você verá as caixas delimitadoras ao redor do termo detectado "learning" e os respectivos rótulos na imagem.

## Uso

Para executar o script e processar imagens:

1. Defina as variáveis de ambiente no arquivo `.env` (para o caminho da pasta de imagens e o caminho da fonte).
2. Execute o script:
    ```bash
    py leitorOCR.py
    ```

O script irá:
- Ler as imagens da pasta especificada.
- Detectar o texto utilizando OCR.
- Destacar o termo pesquisado nas imagens.
- Salvar as imagens processadas e o texto extraído.

## Saída

- **Imagens Processadas**: Salvas na pasta `Img/`.
- **Arquivo de Texto**: O texto extraído é salvo no arquivo `resultados_ocr.txt`, estruturado com títulos e os resultados do OCR para cada imagem.
