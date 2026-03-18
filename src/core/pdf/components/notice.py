from reportlab.lib.units import mm
from reportlab.platypus import Flowable, Paragraph

from core.pdf.styles import NewsletterStyleSheet


class NoticeBlock(Flowable):
    def __init__(self, text: str):
        super().__init__()
        self._text = text

    def wrap(self, available_width, available_height):
        styles = NewsletterStyleSheet()
        self._para = Paragraph(self._text, styles.notice)
        self._para.wrap(available_width - 8 * mm, available_height)
        self._width = available_width
        self._height = self._para.height + 6 * mm
        return self._width, self._height

    def draw(self):
        from reportlab.lib import colors
        self.canv.setFillColor(colors.HexColor("#e8f4fd"))
        self.canv.roundRect(0, 0, self._width, self._height, radius=4, fill=1, stroke=0)
        self._para.drawOn(self.canv, 4 * mm, 3 * mm)
