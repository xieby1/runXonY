from data import *
from QEMU_sys.meta import *

Transor("Limbo",
    {  HG("",
        Metaface(IsasUSR(Isa_MODERN_ANDROIDs), {Kernel.LINUX_ANDROID}, {Syslib.DEFAULT}, {Lib.ANY}, {Sysapp.ANY}, {App.ANDROID_RUNTIME}, {Rtlib.ANY}),
        Metaface(),
    )},
    Date(2016), Date(2022), color="#383838", parent=QEMU_sys,
)
