from data import *
from WINE.meta import *

Transor("WineX",
    set(),
    Date(2000,12,27), Date(2016), "#800000", dev=Dev.TRANSGAMING_NVIDIA,
    feat="Support DirectX",
    desc='''
        Mail from wine-devel: 2004-August.txt: 22697
        https://web.archive.org/web/20010331041916/http://www.transgaming.com/news.php
    ''',
    parent=WINE,
    renames=[
        Rename("Cedega", Date(2004,6,22), "https://en.wikipedia.org/wiki/Cedega_(software)"),
        Rename("GameTree Linux", Date(2011,2,28), ""),
    ],
)
