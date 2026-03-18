from reportlab.platypus import BaseDocTemplate

from core.pdf.frame import BSSMNewsLatterFrame
from core.pdf.header_footer import NewsletterFooter, NewsletterHeader


class NewsletterDocument:
    def __init__(
            self,
            filename: str,
            layout: BSSMNewsLatterFrame,
            title: str,
            issue: str,
            date: str,
    ):
        self._header = NewsletterHeader(title=title, issue=issue, date=date)
        self._footer = NewsletterFooter()

        layout.page_template.onPage = self._draw_fixed_elements
        self._doc = BaseDocTemplate(filename, pageTemplates=[layout.page_template])

    def _draw_fixed_elements(self, canvas, doc):
        self._header.draw(canvas, doc)
        self._footer.draw(canvas, doc)

    def build(self, story: list):
        self._doc.build(story)
