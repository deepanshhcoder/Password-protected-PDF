# PyPDF2
from PyPDF2 import PdfWriter, PdfReader
import getpass

pdfwriter=PdfWriter()
pdf=PdfReader("D:/py/password_protected_pdf/d1.pdf")
for page_num in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_num])
    
    
password=getpass.getpass(prompt="enter password: ")    
pdfwriter.encrypt(password)

with open("new.pdf","wb") as file:
    pdfwriter.write(file)
    