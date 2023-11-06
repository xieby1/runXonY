from data import *
from LLVM.meta import *

Transor("McSema",
    {  HG("",
        Metaface({(Isa.LLVM, Up.USR)}, {Kernel.LINUX}),
        Metaface(IsasUSR({Isa.X86, Isa.X86_64, Isa.AARCH64}), {Kernel.LINUX}),
        term=Term.STATIC_BINARY_TRANSLATOR,
    )},
    Date(2019), Date(2022,4,26), color="#9C1B45", parent=LLVM,
    desc='''
        https://github.com/lifting-bits/mcsema
        2019: DECOMPILING BINARIES INTO LLVM IR USING MCSEMA AND DYNINST
    ''',
)
