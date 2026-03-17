from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable


class Divider(HRFlowable):
    def __init__(self):
        super().__init__(
            width="100%",
            thickness=1,
            color=colors.HexColor("#cccccc"),
            spaceAfter=4 * mm,
            spaceBefore=4 * mm,
        )
