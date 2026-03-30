from typing import Optional

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas

from core.pdf.fonts import FONT_NAME, register_fonts

register_fonts()


class NewsletterHeader:
    def __init__(self, title: str = "BSSM NEWSLETTER", logo_path: Optional[str] = None):
        self.title = title
        self.logo_path = logo_path

    def draw(self, canvas: Canvas, doc):
        page_width, page_height = A4
        margin = 72
        y = page_height - margin + 4 * mm

        canvas.saveState()

        if self.logo_path:
            canvas.drawImage(
                self.logo_path,
                margin,
                y - 2 * mm,
                width=24 * mm,
                height=12 * mm,
                preserveAspectRatio=True,
                mask="auto",
            )
            text_x = margin + 28 * mm
        else:
            text_x = margin

        canvas.setFillColor(colors.HexColor("#1a1a2e"))
        canvas.setFont(FONT_NAME, 16)
        canvas.drawCentredString(page_width / 2, y + 4 * mm, self.title)

        canvas.setStrokeColor(colors.HexColor("#1a1a2e"))
        canvas.setLineWidth(1)
        canvas.line(margin, y - 4 * mm, page_width - margin, y - 4 * mm)

        canvas.restoreState()


class NewsletterFooter:
    def draw(self, canvas: Canvas, doc):
        page_width, _ = A4
        margin = 72
        y = margin - 8 * mm

        canvas.saveState()
        canvas.setFillColor(colors.HexColor("#cccccc"))
        canvas.rect(margin, y + 5 * mm, page_width - 2 * margin, 0.5, fill=1, stroke=0)

        canvas.setFont(FONT_NAME, 8)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawCentredString(page_width / 2, y, f"- {doc.page} -")
        canvas.restoreState()
