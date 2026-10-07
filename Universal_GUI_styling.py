import tkinter as tk
from openpyxl.styles import Border, Side


LARGE_FONT= ("Verdana", 12)
THIN = Side(border_style="thin", color="00000000")

TOP_CELL = Border(top=THIN, left=THIN, right=THIN)
BOTTOM_CELL = Border(left=THIN, right=THIN, bottom=THIN)
LEFT_CELL = Border(top=THIN, left=THIN, bottom=THIN)
RIGHT_CELL = Border(top=THIN, right=THIN, bottom=THIN)

COLUMN = Border(left=THIN, right=THIN)
ROW = Border(top=THIN, bottom=THIN)

L_SIDE = Border(left=THIN)
R_SIDE = Border(right=THIN)
T_SIDE = Border(top=THIN)
B_SIDE = Border(bottom=THIN)

TL_CORNER = Border(top=THIN, left=THIN)
TR_CORNER = Border(top=THIN, right=THIN)
BL_CORNER = Border(left=THIN, bottom=THIN)
BR_CORNER = Border(right=THIN, bottom=THIN)
