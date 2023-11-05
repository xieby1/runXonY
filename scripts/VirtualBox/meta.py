from data import *
from IntelVT.meta import *

VirtualBox = Transor("VirtualBox",
    {  HG("",
        Metaface(IsasUSR({isa}), {Kernel.WINDOWS, Kernel.LINUX, Kernel.MACOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR_PVL({isa})),
    ) for isa in [Isa.X86, Isa.X86_64]},
    Date(2007,1,17), Date.today(), color="#2F61B4", dev=Dev.ORACLE,
    desc="https://en.wikipedia.org/wiki/VirtualBox",
)
Connector(IntelVT, VirtualBox, Date(2007,1,17))
