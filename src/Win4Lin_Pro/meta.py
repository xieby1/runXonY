from data import *
from Win4Lin.meta import *
from QEMU_sys.meta import *

Win4Lin_Pro = Transor("Win4Lin Pro",
    {  HG("",
        Metaface(),
        Metaface(),
    )},
    Date(2005), Date(2010,3), parent=Win4Lin,
    desc="https://en.wikipedia.org/wiki/Win4Lin",
)
Connector(QEMU_sys, Win4Lin_Pro, Date(2005))
