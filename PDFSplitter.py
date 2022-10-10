import os
from time import sleep
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import shutil

pdf_file_path = () # Caminho do arquivo

# Retirando a extensão ".PDF" e substituindo por nada
#file_base_name = pdf_file_path.replace('.pdf', '')

# Caminho de saída
output_folder_path = os.path.join(os.getcwd(), 'Output')

pdf = PdfFileReader(pdf_file_path)

# Pecorrendo cada página do PDF
for page_num in range(pdf.numPages):
    pdfWriter = PdfFileWriter()
    pdfWriter.addPage(pdf.getPage(page_num))

    numero_da_pagina = page_num + 1

    # Criando um novo PDF para cada página - Com o mesmo nome do principal + o numero correspondente da página
    with open(os.path.join(output_folder_path, f'{item}_pagina_{numero_da_pagina}.pdf'), 'wb') as f:
        pdfWriter.write(f)
        f.close()
        # Verifica se o PDF foi gerado
        check = 'OK'
    # Caso tenha sido, ele vai mover esse PDF para outro diretório
    if check == 'OK':
        origem_download = Path(output_folder_path, f'{item}_pagina_{numero_da_pagina}.pdf')
        destino = Path() # Caminho da pasta para onde o arquivo sera movido
        shutil.move(origem_download, destino)

print('#########################')
print('# 'f'{pdf.numPages} '+'Páginas divididas #')
print('#########################')
