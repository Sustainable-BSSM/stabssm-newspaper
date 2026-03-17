from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm

from src.core.pdf.fonts import FONT_NAME, register_fonts

register_fonts()


class NewsletterStyleSheet:
    def __init__(self):
        base = getSampleStyleSheet()

        self.title = ParagraphStyle(
            "NewsletterTitle",
            parent=base["Title"],
            fontName=FONT_NAME,
            fontSize=24,
            leading=30,
            textColor=colors.HexColor("#1a1a2e"),
            spaceAfter=6 * mm,
        )

        self.article_title = ParagraphStyle(
            "ArticleTitle",
            parent=base["Heading1"],
            fontName=FONT_NAME,
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#16213e"),
            spaceBefore=4 * mm,
            spaceAfter=2 * mm,
        )

        self.body = ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName=FONT_NAME,
            fontSize=10,
            leading=15,
            textColor=colors.HexColor("#333333"),
            spaceAfter=3 * mm,
        )

        self.caption = ParagraphStyle(
            "Caption",
            parent=base["Normal"],
            fontName=FONT_NAME,
            fontSize=8,
            leading=12,
            textColor=colors.HexColor("#888888"),
            alignment=1,  # center
            spaceAfter=3 * mm,
        )

        self.notice = ParagraphStyle(
            "Notice",
            parent=base["Normal"],
            fontName=FONT_NAME,
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#1a1a2e"),
            backColor=colors.HexColor("#e8f4fd"),
            spaceAfter=3 * mm,
        )
