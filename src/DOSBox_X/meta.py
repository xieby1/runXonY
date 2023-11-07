from data import *
from DOSBox.meta import *

Transor("DOSBox-X",
    {  HG("",
        Metaface(IsasUSR(isas), {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR_PVL)}),
        term=Term.V2B,
    ) for isas,kernel in zip(
        [Isa_MODERN_WINDOWSs, Isa_MODERN_MACOSs, Isa_LINUXs, Isa_BSDs],
        [Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX, Kernel.BSD])},
    Date(2011), Date.today(), color="#113466", parent=DOSBox,
)
