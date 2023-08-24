from fpdf import FPDF

def create_pdf(filename):
    name = "gustav valbour relei"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("arial", "B", 16)
    pdf.cell(40,10, f"nombre del paciente: {name}")

    pdf.image("izqlogo.png", 0, 30)
    pdf.image("goblin.png", 0, 100)

    pdf.output("new.pdf", "F")

if __name__ == "__main__":
    create_pdf("new.pdf")