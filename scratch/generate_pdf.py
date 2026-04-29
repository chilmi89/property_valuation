from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'Penjelasan Kode SVR Valuasi Properti', border=False, ln=1, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Halaman {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Read the documentation file
doc_path = '/home/syelha/.gemini/antigravity/brain/6fedaad1-a7da-40da-a06e-1e8bebe251fd/penjelasan_kode.md'
with open(doc_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line:
        pdf.ln(5)
        continue
    
    if line.startswith('# '):
        pdf.set_font('helvetica', 'B', 16)
        pdf.multi_cell(0, 10, line[2:])
    elif line.startswith('## '):
        pdf.set_font('helvetica', 'B', 14)
        pdf.multi_cell(0, 10, line[3:])
    elif line.startswith('### '):
        pdf.set_font('helvetica', 'B', 12)
        pdf.multi_cell(0, 8, line[4:])
    elif line.startswith('```'):
        pdf.set_font('courier', '', 9)
        pdf.set_fill_color(240, 240, 240)
        # We don't want to start code block with the backticks
        continue
    elif line.startswith('* '):
        pdf.set_font('helvetica', '', 10)
        pdf.multi_cell(0, 6, '  • ' + line[2:])
    else:
        # Check if inside code block (simple heuristic)
        # If the font is courier, it's a code block
        if pdf.font_family == 'courier':
            pdf.multi_cell(0, 5, line, fill=True)
        else:
            pdf.set_font('helvetica', '', 10)
            pdf.multi_cell(0, 6, line)

output_pdf = '/home/syelha/Documents/pns_2026/kelompok/SalesHouse/Penjelasan_Kode_Valuasi_SVR.pdf'
pdf.output(output_pdf)
print(f"PDF generated: {output_pdf}")
