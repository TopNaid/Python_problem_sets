from fpdf import FPDF

class ShirtificatePDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, "CS50 Shirtificate", 0, new_x='LMARGIN', new_y='NEXT', align="C")

def main():
    user_input = input("Name: ")
    user_input += " took CS50"

    pdf = ShirtificatePDF()
    pdf.add_page()

    # Add shirt image centered
    img_width = 150
    pdf.image("shirtificate.png", x=(210 - img_width) / 2, y=40, w=img_width)

    # Set font for the user's name
    pdf.set_font("helvetica", "", 22)
    pdf.set_text_color(255, 255, 255)

    # Center the user's name text on the shirt
    text_width = pdf.get_string_width(user_input)
    pdf.text(x=(210 - text_width) / 2, y=95, text=user_input)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
