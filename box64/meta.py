from data import *
from box86.meta import *

Transor("box64",
    {  HG("DynaRec",
        Metaface({(Isa.ARM64, Up.USR)}, {Kernel.LINUX}, {Syslib.DEFAULT}, {Lib.ANY}),
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
        perfs=[
            Perf(3763.83/10024.33, Benchmark.COREMARK, Date(2023,1,15),
                 "box64 0.1.8, x86_64 on raspberrypi4, gcc 11.3.0"),
        ],
    ), HG("without-DynaRec",
        Metaface(IsasUSR({Isa.ARM64, Isa.LA64, Isa.RISCV64, Isa.POWERPC64, Isa.X86_64}), {Kernel.LINUX}),
        Metaface({(Isa.X86_64, Up.USR)}, {Kernel.LINUX}),
        term=Term.USER_LEVEL_BINARY_TRANSLATOR_WITH_LIB_PASS_THROUGH,
    )},
    Date(2020,12,1), Date.today(), color="#B5E853", parent=box86,
    desc="https://github.com/ptitSeb/box64",
)
