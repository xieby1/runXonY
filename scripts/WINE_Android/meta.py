from data import *
from WINE.meta import *

Transor("WINE-Android",
    {  HG(isa.name,
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    ) for isa in Isa_MODERN_ANDROIDs},
    Date(2014,2), Date.today(), color="#800000", parent=WINE,
    desc="https://wiki.winehq.org/Android",
)
