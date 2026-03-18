from reportlab.platypus import Flowable, Paragraph
from core.pdf.styles import NewsletterStyleSheet


class ArticleBlock(Flowable):
    def __init__(self, title: str, body: str, styles: NewsletterStyleSheet):
        super().__init__()
        self._title = Paragraph(title, styles.article_title)
        self._body = Paragraph(body, styles.body)

    def wrap(self, available_width, available_height):
        self._title.wrap(available_width, available_height)
        self._body.wrap(available_width, available_height)
        self._height = self._title.height + self._body.height
        self._width = available_width
        return self._width, self._height

    def draw(self):
        y = self._height - self._title.height
        self._title.drawOn(self.canv, 0, y)
        self._body.drawOn(self.canv, 0, 0)
