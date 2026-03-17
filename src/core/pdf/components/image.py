from reportlab.lib.units import mm
from reportlab.platypus import Flowable, Image
from reportlab.platypus.para import Paragraph


class ImageBlock(Flowable):
    def __init__(self, path: str, caption: str = "", max_width: float = 400):
        super().__init__()
        self._path = path
        self._caption_text = caption
        self._max_width = max_width

    def wrap(self, available_width, available_height):
        width = min(self._max_width, available_width)
        self._image = Image(self._path, width=width)
        self._image.wrap(available_width, available_height)
        self._width = available_width
        self._height = self._image.drawHeight + (6 * mm if self._caption_text else 0)
        return self._width, self._height

    def draw(self):
        from src.core.pdf.styles import NewsletterStyleSheet
        styles = NewsletterStyleSheet()
        x = (self._width - self._image.drawWidth) / 2
        self._image.drawOn(self.canv, x, 6 * mm if self._caption_text else 0)
        if self._caption_text:
            caption = Paragraph(self._caption_text, styles.caption)
            caption.wrap(self._width, 6 * mm)
            caption.drawOn(self.canv, 0, 0)
