from data import *

VMware_Workstation = Transor("VMware Workstation",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX, Kernel.WINDOWS}, {Syslib.WINDOWS}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR_PVL)}),
    )},
    Date(1999,5,15), Date.today(), "#F38C00", dev=Dev.VMWARE,
)
