from data import *

Transor("VisUAL",
    {  HG("",
        Metaface(IsasUSR(isas), {kenerl}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM, Up.USR)}),
    ) for isas,kenerl in zip(
        [Isa_MODERN_WINDOWSs, Isa_MODERN_MACOSs, Isa_LINUXs],
        [Kernel.WINDOWS, Kernel.MACOS, Kernel.LINUX]
    )},
    Date(2015), Date.today(), color="#3A9878",
    feat="visualization",
    desc="https://salmanarif.bitbucket.io/visual/about.html",
)
