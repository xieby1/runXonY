from data import *

Transor("WSL",
    {  HG("",
        Metaface({(isa, Up.USR)}, {Kernel.WINDOWS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}),
    ) for isa in Isa_MODERN_WINDOWSs},
    Date(2016,8,2), Date.today(), color="#0C2AAE", dev=Dev.MICROSOFT,
    desc="https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux",
)
