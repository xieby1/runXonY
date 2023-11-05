from data import *
from VMwareWorkstation.meta import *

Transor("VMware Player",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
    ) for kernel in [Kernel.WINDOWS, Kernel.LINUX]},
    Date(2008,6,6), Date.today(), color="#FFE839", dev=Dev.VMWARE, parent=VMwareWorkstation,
    desc="https://en.wikipedia.org/wiki/VMware_Workstation_Player",
)
