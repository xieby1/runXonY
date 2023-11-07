from data import *
from MAMBO_X64.meta import *
from KVM.meta import *

HyperMAMBO_X64 = Transor("HyperMAMBO-X64",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM32, Up.USR_PVL)}),
    )},
    Date(2017), parent=MAMBO_X64, dev=Dev.MANCHESTER,
    desc="2017: HyperMAMBO-X64: Using Virtualization to Support High-Performance Transparent Binary Translation",
)
Connector(KVM, HyperMAMBO_X64, Date(2017))
