import os
from time import sleep
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import shutil

# informando o nome do aqruivo que ira ser usado

diretorio = os.listdir (r'C:\Users\25605\Desktop\demonstrativo')
list_dir = r"C:/Users/25605/Desktop/demonstrativo/"
print(diretorio)
print(list_dir)

for item in diretorio:
    

    # Caminho do diretorio + o arquivo informado
    pdf_file_path = (str(list_dir)+str(item))
    print(pdf_file_path)

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
            destino = Path(r"\\srvcid27\RPA_ARQUIVOS\CHAVE_FGTS\ORIGEM\\")
            shutil.move(origem_download, destino)

    print('#########################')
    print('# 'f'{pdf.numPages} '+'Páginas divididas #')
    print('#########################')
