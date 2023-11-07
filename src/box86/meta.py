from data import *

box86 = Transor("box86",
    {  HG("",
        Metaface({(Isa.ARM32, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
    )},
    Date(2018), Date.today(), color="#B5E853",
    feat="lib warp",
    desc="https://github.com/ptitSeb/box86",
)
