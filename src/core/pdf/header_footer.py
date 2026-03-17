from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas


class NewsletterHeader:
    def __init__(self, title: str, issue: str, date: str):
        self.title = title
        self.issue = issue
        self.date = date

    def draw(self, canvas: Canvas, doc):
        page_width, page_height = A4
        margin = 72
        y = page_height - margin + 4 * mm

        canvas.saveState()
        canvas.setFillColor(colors.HexColor("#1a1a2e"))
        canvas.rect(margin, y, page_width - 2 * margin, 1, fill=1, stroke=0)

        canvas.setFont("Helvetica-Bold", 16)
        canvas.setFillColor(colors.HexColor("#1a1a2e"))
        canvas.drawString(margin, y + 4 * mm, self.title)

        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawRightString(page_width - margin, y + 4 * mm, f"{self.issue}  |  {self.date}")
        canvas.restoreState()


class NewsletterFooter:
    def draw(self, canvas: Canvas, doc):
        page_width, _ = A4
        margin = 72
        y = margin - 8 * mm

        canvas.saveState()
        canvas.setFillColor(colors.HexColor("#cccccc"))
        canvas.rect(margin, y + 5 * mm, page_width - 2 * margin, 0.5, fill=1, stroke=0)

        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawCentredString(page_width / 2, y, f"- {doc.page} -")
        canvas.restoreState()
