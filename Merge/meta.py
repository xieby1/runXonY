from data import *

Merge = Transor("Merge",
    {  HG("",
        Metaface({(Isa.I386, Up.USR)}, {Kernel.SCO_UNIX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.I386, Up.USR_PVL)})
    )},
    Date(1985,10,9), Date(2000),
    feat="run DOS/Windows 3.1",
    desc="https://en.wikipedia.org/wiki/Merge_(software)"
)
