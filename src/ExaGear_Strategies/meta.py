from data import *
from WINE.meta import *

ExaGear_Strategies = Transor("ExaGear Strategies",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64}), {Kernel.NO_SYSCALL}, {Syslib.WINDOWS}),
    )},
    Date(2014), Date(2020), dev=Dev.ELTECH_RUSSIA,
    desc="https://4pda.to/forum/index.php?showtopic=992239",
)
Connector(ExaGear_Strategies, WINE, Date(2014))
