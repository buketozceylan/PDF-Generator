#Coding exercise for learning PDF Generation, document type to document type convertion

from fpdf import FPDF

pdf = FPDF(orientation='P', format='A4') #Generate a file that is in A4 format and Portrait orientation (L for Lanscape)
pdf.add_page() #For adding page

pdf.set_font('Arial', 'B', 16)
pdf.cell(w=0, h=12, txt="Hello World!", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hello World!", align="L", ln=1, border=1)

pdf.output("test.pdf") #create the test.pdf file




