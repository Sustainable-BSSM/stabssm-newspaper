from reportlab.lib.units import mm
from reportlab.platypus import Flowable, Paragraph
from typing import Optional

from core.pdf.styles import NewsletterStyleSheet


class SectionHeader(Flowable):
    def __init__(self, title: str, subtitle: Optional[str] = None):
        super().__init__()
        self._title = title
        self._subtitle = subtitle

    def wrap(self, available_width, available_height):
        styles = NewsletterStyleSheet()
        self._title_para = Paragraph(self._title, styles.section_title)
        self._title_para.wrap(available_width, available_height)
        self._width = available_width
        self._height = self._title_para.height + 2 * mm

        if self._subtitle:
            self._subtitle_para = Paragraph(self._subtitle, styles.section_subtitle)
            self._subtitle_para.wrap(available_width, available_height)
            self._height += self._subtitle_para.height + 1 * mm

        return self._width, self._height

    def draw(self):
        y = self._height - self._title_para.height - 1 * mm
        self._title_para.drawOn(self.canv, 0, y)

        if self._subtitle:
            y -= self._subtitle_para.height + 1 * mm
            self._subtitle_para.drawOn(self.canv, 0, y)
