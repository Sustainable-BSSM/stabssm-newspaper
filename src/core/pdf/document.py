from typing import Optional

from reportlab.platypus import BaseDocTemplate

from core.pdf.frame import BSSMNewsLatterFrame
from core.pdf.header_footer import NewsletterFooter, NewsletterHeader


class NewsletterDocument:
    def __init__(
        self,
        filename: str,
        layout: BSSMNewsLatterFrame,
        title: str = "BSSM NEWSLETTER",
        header: Optional[NewsletterHeader] = None,
        footer: Optional[NewsletterFooter] = None,
        logo_path: Optional[str] = None,
    ):
        self._header = (
            header
            if header is not None
            else NewsletterHeader(title=title, logo_path=logo_path)
        )
        self._footer = footer if footer is not None else NewsletterFooter()

        layout.page_template.onPage = self._draw_fixed_elements
        self._doc = BaseDocTemplate(filename, pageTemplates=[layout.page_template])
        self._story = []

    def _draw_fixed_elements(self, canvas, doc):
        self._header.draw(canvas, doc)
        self._footer.draw(canvas, doc)

    def write(self, *flowables) -> "NewsletterDocument":
        self._story.extend(flowables)
        return self

    def write_each(self, items, sep=None) -> "NewsletterDocument":
        for i, item in enumerate(items):
            self._story.append(item)
            if sep is not None and i < len(items) - 1:
                self._story.append(sep)
        return self

    def build(self):
        self._doc.build(self._story)
