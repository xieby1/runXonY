from data import *
from Xen.meta import *

Transor("Qubes OS",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
        Metaface({(Isa.X86_64, Up.USR)}),
    )},
    Date(2013,9,3), Date.today(), color="#3874D8", dev=Dev.INVISIBLE_THINGS_LAB, parent=Xen,
    desc="https://en.wikipedia.org/wiki/Qubes_OS",
)
