from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame, PageTemplate


class BSSMNewsLatterFrame:
    page_width, page_height = A4
    margin = 72

    def __init__(self):
        self.frame = Frame(
            x1=self.margin,
            y1=self.margin,
            width=self.page_width - 2 * self.margin,
            height=self.page_height - 2 * self.margin,
        )
        self.page_template = PageTemplate(
            id="A4",
            frames=[self.frame],
            pagesize=A4,
        )
