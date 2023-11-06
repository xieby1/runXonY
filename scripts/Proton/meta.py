from data import *
from WINE.meta import *

Transor("Proton",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2018,8,21), Date.today(), parent=WINE, dev=Dev.VALVE,
    desc="https://github.com/ValveSoftware/Proton",
)
