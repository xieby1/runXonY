from data import *
from Xen.meta import *

Transor("MagiXen",
    {  HG("",
        Metaface({(Isa.ITANIUM, Up.USR_PVL)}),
        Metaface({(Isa.IA32, Up.USR_PVL)}),
    )},
    Date(2007), dev=Dev.HP, parent=Xen,
    desc="2007: MagiXen: Combining Binary Translation and Virtualization",
)
