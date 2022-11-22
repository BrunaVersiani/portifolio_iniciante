import PyPDF2
pdf = open("Quem_sou.pdf", "rb")
ler = PyPDF2.PdfFileReader(pdf)
pagina = ler.getPage(0)
print(pagina.extractText())

'''Extrair textos de arquivos PDF é muito útil, e pode ser usado no dia a dia.'''