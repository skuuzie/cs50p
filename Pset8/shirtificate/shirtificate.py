from fpdf import FPDF


class Shirtificate(FPDF):

    # Set the header/title "CS50 Shirtificate"
    def header(self):
        self.ln(15)

        self.set_font("helvetica", "", 48)

        self.cell(0, 15, self.title, new_x="LMARGIN", new_y="NEXT", align="C")

        self.ln(25)

    # Make the shirtificate with name as input
    def make_shirt(self, name):
        self.add_page()

        self.image("shirtificate.png", x=0)

        self.set_y(135)
        self.set_font("helvetica", "", 32)
        self.set_text_color(255, 255, 255)

        self.cell(None, None, f"{name} took CS50", center=True)


def main():
    name = input("Name: ")

    pdf = Shirtificate()

    pdf.set_title("CS50 Shirtificate")
    pdf.make_shirt(name)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
