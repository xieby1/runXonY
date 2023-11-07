from data import *

Transor("IA-32 EL",
    {  HG("",
        Metaface({(Isa.IA64, Up.USR)}, {kernel}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.IA32, Up.USR)}, {kernel}),
    ) for kernel in [Kernel.LINUX, Kernel.WINDOWS]},
    Date(2003), Date.today(),
)
