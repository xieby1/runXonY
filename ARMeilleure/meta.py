from data import *
from Ryujinx.meta import *

Transor("ARMeilleure",
    {  HG("",
        Metaface(IsasUSR({Isa.X86_64}), {Kernel.WINDOWS, Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.ARM64, Up.USR)}),
    )},
    Date(2019,8,9), Date.today(), color="#FF5F55", parent=Ryujinx,
    feat="Framework",
    desc="https://github.com/Ryujinx/Ryujinx/",
)
