from fpdf import FPDF

def create_pdf(filename):
    name = "gustav valbour relei"

    pdf = FPDF('P', 'pt', (1675, 2175))
    pdf.add_page()
    pdf.set_font("arial", "B", 16)
    pdf.image("descarga.png", 0, 0)
    pdf.cell(40, 10, f"nombre del paciente: {name}")

    pdf.output("new.pdf", "F")

if __name__ == "__main__":
    create_pdf("new.pdf")