from data import *

Anbox = Transor("Anbox",
    {  HG("",
        Metaface({(isa, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(isa, Up.USR)}, {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}),
    ) for isa in [Isa.X86_64, Isa.ARM64]},
    Date(2016,4,11), Date.today(), color="#009688", license="GPL3",
)
