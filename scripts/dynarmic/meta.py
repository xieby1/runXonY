from data import *
from citra.meta import *

dynarmic = Transor("dynarmic",
    {  HG("",
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.ANY}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface(IsasUSR({Isa.ARM64, Isa.ARM32})),
    )},
    Date(2016,7,1), Date.today(),
    feat="Framework",
)
Connector(dynarmic, citra, Date(2016,9,2))
