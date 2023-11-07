from data import *
from QEMU_sys.meta import *

Transor("UTM",
    {  HG("",
        Metaface({(Isa.AARCH64, Up.USR)}, {Kernel.IOS}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(),
    )},
    Date(2019), Date.today(), color="#1D63EA", parent=QEMU_sys,
)
