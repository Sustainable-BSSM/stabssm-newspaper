from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_NAME = "Pretendard"

_registered = False


def register_fonts():
    global _registered
    if _registered:
        return
    pdfmetrics.registerFont(
        TTFont(FONT_NAME, "/Users/comodoflow/Library/Fonts/PretendardVariable.ttf")
    )
    _registered = True
