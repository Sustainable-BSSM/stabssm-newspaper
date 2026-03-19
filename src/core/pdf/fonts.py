from pathlib import Path

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_NAME = "Pretendard"
_FONT_PATH = Path(__file__).parent / "PretendardVariable.ttf"

_registered = False


def register_fonts():
    global _registered
    if _registered:
        return
    pdfmetrics.registerFont(TTFont(FONT_NAME, str(_FONT_PATH)))
    _registered = True
