from data import *
from ExaGear_Strategies.meta import *

Transor("ExaGear",
    {  HG("",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64}), {Kernel.LINUX}),
    )},
    Date(2020), Date.today(), parent=ExaGear_Strategies, dev=Dev.ELTECH_HUAWEI,
)
