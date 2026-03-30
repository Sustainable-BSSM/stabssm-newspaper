from typing import List

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Flowable, Paragraph

from core.pdf.fonts import FONT_NAME
from core.pdf.styles import NewsletterStyleSheet


class FooterBanner(Flowable):
    def __init__(self, lines: List[str]):
        super().__init__()
        self._lines = lines

    def wrap(self, available_width, available_height):
        self._width = available_width
        styles = NewsletterStyleSheet()
        self._paragraphs = []
        total_height = 4 * mm

        for line in self._lines:
            para = Paragraph(line, styles.body)
            para.wrap(self._width - 20 * mm, available_height)
            self._paragraphs.append(para)
            total_height += para.height + 2 * mm

        self._height = total_height + 4 * mm
        return self._width, self._height

    def draw(self):
        self.canv.setFillColor(colors.HexColor("#d32f2f"))
        self.canv.rect(0, 0, self._width, self._height, fill=1, stroke=0)

        self.canv.setFillColor(colors.white)
        y = self._height - 6 * mm
        for para in self._paragraphs:
            para.drawOn(self.canv, 10 * mm, y - para.height)
            y -= para.height + 2 * mm
