from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'Penjelasan Kode SVR Valuasi Properti', border=False, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Halaman {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

doc_path = '/home/syelha/.gemini/antigravity/brain/6fedaad1-a7da-40da-a06e-1e8bebe251fd/penjelasan_kode.md'
with open(doc_path, 'r') as f:
    lines = f.readlines()

in_code_block = False

for line in lines:
    line = line.rstrip() # Keep indentation but remove trailing newline
    if not line.strip():
        pdf.ln(5)
        continue
    
    if line.startswith('# '):
        pdf.set_font('helvetica', 'B', 16)
        pdf.multi_cell(0, 10, line[2:], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    elif line.startswith('## '):
        pdf.set_font('helvetica', 'B', 14)
        pdf.multi_cell(0, 10, line[3:], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    elif line.startswith('### '):
        pdf.set_font('helvetica', 'B', 12)
        pdf.multi_cell(0, 8, line[4:], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    elif line.startswith('```'):
        in_code_block = not in_code_block
        if in_code_block:
            pdf.set_font('courier', '', 9)
            pdf.set_fill_color(240, 240, 240)
        else:
            pdf.set_font('helvetica', '', 10)
        continue
    elif line.startswith('* '):
        pdf.set_font('helvetica', '', 10)
        pdf.multi_cell(0, 6, '  - ' + line[2:], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    else:
        if in_code_block:
            # Handle very long code lines by slicing or wrapping
            pdf.multi_cell(0, 5, line, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        else:
            pdf.set_font('helvetica', '', 10)
            pdf.multi_cell(0, 6, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

output_pdf = '/home/syelha/Documents/pns_2026/kelompok/SalesHouse/Penjelasan_Kode_Valuasi_SVR.pdf'
pdf.output(output_pdf)
print(f"PDF generated: {output_pdf}")
